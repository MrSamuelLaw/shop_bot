#!urs/bin/env python3

from sympy import Symbol, solve
from typing import List
from math import sqrt, pi

class SymbolCollection():
    def __init__(self, symbol_names: List[str]):
            """
            takes a list of variable names, convertes them to
            sympy Symbol's thus allowing them to be accessed
            via dot notation.
            """
            # create symbolic objects from parameter names
            for name in symbol_names:
                setattr(self, f'{name}', Symbol(f'{name}'))

    def __str__(self):
        return str(self.__dict__)

    def update(self, symbol_obj, value):
        """
        takes a symbol object
        """
        if not hasattr(self, symbol_obj):
            raise ValueError(
                f"{symbol_obj} not found in this SymbolCollection..."
            )
        setattr(self, symbol_obj, value)


class Endmill():
    def __init__(self, *, diameter, flute_number):
        self.diameter = float(diameter)
        self.flute_number = int(str(flute_number))


class MillFNS():

    def __init__(self, RPM_MAX: int, IPM_MAX: int):
        self.RPM_MAX = RPM_MAX
        self.IPM_MAX = IPM_MAX

    def define_endmill(self, *, diameter, flute_number, shape):
        self.em = Endmill(
            diameter = diameter,
            flute_number = flute_number
        )
        self.em.shape = shape

    def define_manufacture_parameters(self, **kwargs):
        """
        Only 4 kwargs are needed. The rest will be
        calculated.

        self.define_tool must be called prior to defining
        manufactures parameters

        kwargs:
            IPT: float, inches per tooth, aka chipload

            RPM: int, rotations per minute

            IPM: float, inches per minute

            adoc: float, scaler to multiply by diameter to determine
                cut depth. For example, 0.50 = 50% axial depth of cut

            rdoc: float, scaler to multiply by diameter to determine
                cut stepover. For example, 0.50 = 50% tool stepover

            MRR: float, material removal rate

        Example call
            self.define_manufacture_parameters(
                IPT=0.005,
                RPM=10_000,
                rdoc=0.5
                adoc=1
            )
        """
        if not hasattr(self, 'em'):
            raise AttributeError("cannot define parameters without tool being defined")
        tool = self.em

        # set parameter values if given
        c = SymbolCollection(['IPT', 'RPM', 'n', 'IPM', 'adoc', 'rdoc', 'MRR'])
        for k in kwargs:
            c.update(k, kwargs[k])
        c.n = tool.flute_number

        # convert rdoc and adoc from percent to length
        c.rdoc = (c.rdoc * tool.diameter)
        c.adoc = (c.adoc * tool.diameter)

        # define equations
        eq1 = (c.IPM / (c.RPM * c.n)) - c.IPT
        eq2 = (c.rdoc * c.adoc * c.RPM * c.IPT * c.n) - c.MRR

        # generate solution
        sol = solve([eq1, eq2])
        for s in sol:
            c.update(str(s), sol[s])

        # solve for effective chip thickness
        if c.rdoc < (0.5*tool.diameter):
            c.chip_thickness = 2*c.IPT*sqrt((tool.diameter * c.rdoc) - \
                            (c.rdoc*c.rdoc)/tool.diameter)
        else:
            c.chip_thickness = c.IPT

        self.manufacture_parameters = c

    def get_manufacture_parameter_defs(self):
        return {
            'IPT': 'float, inches per tooth, aka chipload',

            'RPM': 'int, rotations per minute',

            'IPM': 'float, inches per minute',

            'adoc': 'float, scaler to multiply by diameter to determine'
                'cut depth. For example, 0.50 = 50% axial depth of cut',

            'rdoc': 'float, scaler to multiply by diameter to determine'
                'cut stepover. For example, 0.50 = 50% tool stepover',

            'MRR': 'float, material removal rate'
        }

    def get_feeds_n_speeds(self, rdoc, adoc):
        # validate type
        rdoc = float(rdoc)
        adoc = float(adoc)
        # raname variables for easy reading
        c = self.manufacture_parameters
        tool = self.em

        # convert rdoc and adoc from percent to length
        rdoc = (rdoc * tool.diameter)
        adoc = (adoc * tool.diameter)

        # calculate rpms
        if rdoc < 0.5*tool.diameter:
            ipt_adj = (c.chip_thickness * tool.diameter)/(2 * sqrt((tool.diameter * rdoc) - (rdoc*rdoc)))
        else:
            ipt_adj = c.IPT
        rpm = c.MRR/(rdoc*adoc*tool.flute_number*ipt_adj)

        # adjust rpms if to high
        if rpm > self.RPM_MAX:
            mrr = c.MRR*self.RPM_MAX/rpm
        else:
            mrr = c.MRR
        rpm = mrr/(rdoc*adoc*tool.flute_number*ipt_adj)

        # solve for surface speed based on rpm
        sfm = rpm*tool.diameter*pi/12

        # solve for feed using effective ipt
        ipm = ipt_adj*rpm*tool.flute_number

        # adjust feed rate if above max
        if ipm > self.IPM_MAX:
            ipm = self.IPM_MAX
            rpm = ipm/(ipt_adj*tool.flute_number)
            sfm = rpm*tool.diameter*pi/12

        # generate warnings
        warnings = []
        if ipm > 200:
            warnings.append("warning, high feed rate may lead to machine shaking")
        if ((rdoc/tool.diameter) < 0.1):
            warnings.append("warning, low stepover may cause chip thinning may occure, causing poor surface finish")
        if mrr < (0.5*c.MRR):
            warnings.append("warning, tool may vibrate due to low material removal rate (MMR)")
        if sfm < 400:
            warnings.append("warning, low surface speed may cause tearout")

        speeds_n_feeds = {
            'RPM': (rpm, 'rotations per minute'),
            'IPM': (ipm, 'inches per minute'),
            'SFM': (sfm, 'surface inches per minute'),
            'IPT_adj': (ipt_adj, 'inches per tooth'),
            'IPT_eff': (c.chip_thickness, 'inches per tooth'),
            'adoc': (adoc, 'inches'),
            'rdoc': (rdoc, 'inches'),
            'MRR': (mrr, 'inches^3')
        }

        return (warnings, speeds_n_feeds)
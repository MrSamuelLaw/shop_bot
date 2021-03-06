#!/usr/bin/env python


import logging


class bolt_pattern():

    _units = None
    unit_dict = {"in": "G20", "mm": "G21"}

    def __init__(self):
        self._logger = logging.getLogger('log')
        self._logger.info('bolt_pattern object instantiated')

    def get_rect_gcode(self, units, x, y, depth):
        """
        generate rectangle where each corner is
        a spot to drill shallow, in order to mark where bolts
        should be placed to hold work down.
        """

        self._logger.debug('generating rect gcode')
        self._set_units(units)
        rect = self._set_rect(x, y)
        if self._units is not None:
            safe_z = self._z_retract()
            gcode = '(Rectangle Grid GCode)\n'  # title
            gcode += 'G90 {} F50.00\n'.format(self.unit_dict[self._units])  # safety line
            gcode += 'G00 X0.0 Y0.0 Z{0:.2f}\n'.format(safe_z)  # move to zero
            gcode += 'TR,12000\nC6\n'  # turn on spindle to 12000 RPM w/usr confirm
            gcode += 'G04 P2\n'  # pause for two seconds

            for coordinate in rect:  # generate cutting code
                x, y = coordinate
                gcode += 'G00 X{0:.3f}, Y{1:.3f} F300.00\n'.format(x, y)  # go to x,y
                gcode += 'G01 Z{0:.3f} F50.00\n'.format(-depth)  # proceed to z depth
                gcode += 'G01 Z{0:.3f}\n'.format(safe_z)  # retract

            gcode += 'M05\n'  # turn spindle off
            gcode += 'M02'  # end of file
            return gcode

    def _z_retract(self):
        """
        retract on the Z axis
        """

        if self._units == 'in':
            return 1.00
        elif self._units == 'mm':
            return 25.4

    def _set_units(self, units):
        """
        set units
        """

        if units.lower() not in self.unit_dict.keys():
            logging.debug("unit not valid")
            return -3
        else:
            self._units = units.lower()
            logging.debug("units set to {}".format(self._units))
            return 2

    def _set_rect(self, x, y):
        """
        define width and height of the rectangle

        x = width
        y = height
        """

        a = (0, 0)
        b = (0, y)
        c = (y, x)
        d = (x, 0)
        rect = [a, b, c, d]
        return rect

    def _set_depth(self, depth):
        """
        depth to drill in inches
        """
        return depth

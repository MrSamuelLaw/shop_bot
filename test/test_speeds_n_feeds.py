#!/usr/bin/env python3

import unittest
from feeds_n_speeds import MillFNS, Endmill, SymbolCollection

class test_MillFNS(unittest.TestCase):

    def setUp(self):
        self.calc = MillFNS(IPM_MAX=300, RPM_MAX=18_000)

    def setTool(self):
        self.calc.define_endmill(
            diameter=0.25,
            flute_number=2,
            shape='ball_nose'
        )

    def setParmeters(self):
        self.calc.define_manufacture_parameters(
                IPT=0.005,
                RPM=15_000,
                rdoc=0.5,
                adoc=1,
        )

    def test_define_tool(self):
        with self.assertRaises(TypeError):
            Endmill(0.5, 2)
        with self.assertRaises(ValueError):
            Endmill(
                diameter=0.5,
                flute_number=2.1
            )
        Endmill(
            diameter=0.5,
            flute_number=2
        )

    def test_define_manufacture_parematers(self):
        with self.assertRaises(AttributeError):
            self.setParmeters()
        self.setTool()
        self.setParmeters()
        for m in self.calc.manufacture_parameters.__dict__.values():
            if not isinstance(m, str):
                m += 0

    def test_get_manufacture_parameter_defs(self):
        count = len(self.calc.get_manufacture_parameter_defs().keys())
        self.assertEqual(count, 6)

    def test_get_feeds_n_speeds(self):
        self.calc.define_endmill(
            diameter=0.25,
            flute_number=2,
            shape='square_nose'
        )

        self.calc.define_manufacture_parameters(
            IPT=0.005,
            rdoc=0.5,
            adoc=1,
            RPM=15_000
        )

        warnings, settings = self.calc.get_feeds_n_speeds(
            rdoc=0.005,
            adoc=1.5,
        )
        self.assertTrue(warnings)
        self.assertTrue(settings)




if __name__ == "__main__":
    unittest.main()
import unittest
from Methods.Rule1 import *
from Methods.Helper import *
from Methods.Rule2 import *
from Methods.Rule3 import *
from Methods.Rule4 import *
from Methods.Erroneous1 import *
from Methods.Erroneous2 import *
from Methods.Erroneous3 import *
from Methods.Erroneous4 import *
from Methods.Erroneous5 import *


class Value_test(unittest.TestCase):
    def setUp(self):
        print("Tests has been Started ")

    def test_rule1(self):

        length = len(rule1())

        if length != 207:
            self.assertFalse(length)

        if length == 0:
            self.assertFalse(length)

        return True

    def test_rule2(self):

        length = len(rule2())

        if length != 14:
            self.assertFalse(length)

        if length == 0:
            self.assertFalse(length)

        return True

    def test_rule3(self):

        length = len(rule3())

        if length != 283986:
            self.assertFalse(length)

        if length == 0:
            self.assertFalse(length)

        return True

    def test_rule4(self):

        length = len(rule4())

        if length != 0:
            self.assertFalse(length)

        if length > 0:
            self.assertFalse(length)

        return True

    def test_erroneous1(self):

        length = len(erroneous1())

        if length != 918:
            self.assertFalse(length)

        if length == 0:
            self.assertFalse(length)

        return True

    def test_erroneous2(self):

        length = len(erroneous2())

        if length != 4:
            self.assertFalse(length)

        if length == 0:
            self.assertFalse(length)

        return True

    def test_erroneous3(self):

        length = len(erroneous3())

        if length != 2187:
            self.assertFalse(length)

        if length == 0:
            self.assertFalse(length)

        return True

    def test_erroneous4(self):

        length = len(erroneous4())

        if length != 4238:
            self.assertFalse(length)

        if length == 0:
            self.assertFalse(length)

        return True

    def test_erroneous5(self):

        length = len(erroneous5())

        if length != 793:
            self.assertFalse(length)

        if length == 0:
            self.assertFalse(length)

        return True

    def tearDown(self):
        print("Test Finished")


if __name__ == "__main__":
    unittest.main()

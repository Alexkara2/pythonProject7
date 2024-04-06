assert 2+2==4
import unittest

class me_test(unittest.TestCase):
    def test(self):
        a=False
        self.assertFalse(a)

test1= me_test()
test1.test()
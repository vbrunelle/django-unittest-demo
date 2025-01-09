import unittest

from anapp.some_semiindependent_module.do_something import some_addition


class MyTestCase(unittest.TestCase):
    def test_do_something(self):
        self.assertEqual(some_addition(1, 2), 3)


if __name__ == '__main__':
    unittest.main()

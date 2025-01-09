import unittest
import os
from django.test import TestCase

# Here it automatically discovers the tests in the some_semiindependent_module directory and runs them as bsic unittests. The results
# of those tests will determine the success or failure of the tests in the anapp directory.

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'djangounittestdemo.settings'

class some_semiindependent_module_tests(TestCase):
    def test_some_semiindependent_module(self):
        suite = load_tests(unittest.defaultTestLoader, None, 'test*.py')
        result = unittest.TextTestRunner().run(suite)
        self.assertTrue(result.wasSuccessful())

def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    file_path = 'some_semiindependent_module'
    # print the absolute file path:
    print(os.path.abspath(file_path))
    for all_test_suite in loader.discover(file_path, pattern=pattern):
        for test_suite in all_test_suite:
            suite.addTests(test_suite)
    return suite

if __name__ == '__main__':
    unittest.main()
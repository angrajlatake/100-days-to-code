import unittest


# this module is used to test cases
# from file_name import function

# create a class with unittest inheritance

class TestFunction(unittest.TestCase):

    def basic_test(self):
        testcase = " "  # enter the input that you want to use
        expected = " "  # enter the output you expect to be printed
        self.assertEquals(funtion(testcase), expected)


# there are differant types of cases. one of them is edge case
unittest.main()  # this command runs the test
# change the file to execute it and then run it in the terminal

# !/usr/bin/env python3
import unittest

from emails import find_email


class EmailsTest(unittest.TestCase):
    def basic_test(self):
        testcase = [None, "Bree", "Campbell"]
        expected = "breee@abc.edu"
        self.assertEqual(find_email(testcase), expected)


if __name__ == '__main__':
    unittest.main()

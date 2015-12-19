import unittest
import HTMLTestRunner
import os
import argparse

# import test files
from logintest import LoginTest
from profiletest import ProfileTest

# get command line arguments
parser = argparse.ArgumentParser(description="All tests suite")
parser.add_argument("--html", action="store_true",
                    help="generates a nice looking HTML test report")
args = parser.parse_args()

# get all test cases from test files
logintests = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
profiletests = unittest.TestLoader().loadTestsFromTestCase(ProfileTest)

# creates test suite
alltests = unittest.TestSuite([
    logintests,
    profiletests
])

if(not args.html):
    unittest.TextTestRunner(verbosity=2).run(alltests)
else:
    # get the current directory
    dir = os.getcwd()
    # open reports file
    outfile = open(dir + "/AllTestReport.html", "w")
    # configure html report
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=outfile,
        title="Test Report",
        description="All test cases for application"
    )
    runner.run(alltests)

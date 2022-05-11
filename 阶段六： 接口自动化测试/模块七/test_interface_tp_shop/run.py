import time
import unittest

from BeautifulReport import BeautifulReport
from tomorrow import threads

from base.utils import init_logging


def load_testcase(testfile):
    modules = unittest.TestLoader().discover('./case', testfile)
    return modules

@threads(10)
def run_testcase(testcase, counts):
    result = BeautifulReport(testcase)
    result.report(counts, '测试报告', filename=f'./report/report{time.strftime("%Y%M%d%h%m%s", time.localtime())}.html')


if __name__ == '__main__':

    modules = load_testcase('test*.py')
    test_lst = [test for suites in modules for tests in suites for test in tests]
    for i in modules:
        run_testcase(i, len(test_lst))
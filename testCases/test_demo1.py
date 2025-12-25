# Any pytest file starts with "test_" or ends with "_test.py" is considered as a test file by pytest framework.
# Any test class starts with "Test" is considered as a test class by pytest framework.
# Any test function starts with "test_" is considered as a test case by pytest framework.
# Any code should be wrapped inside a method or a class.
# Method name should be descriptive to understand the purpose of the method.
#  -k stands for method name execution, -s stands for print statement execution, -v stands for verbose mode.
# To run a specific test case: pytest -v -s test_demo1.py -k test_form_fillup
# To run all the test cases in a file: pytest -v -s test_demo1.py
# To run all the test cases in a folder: pytest -v -s testCases/

# mark: if we want run specific type of test cases like sanity, regression, smoke etc we can use @pytest.mark.<markname>

import pytest


@pytest.mark.usefixtures("setup")  # using setup method from conftest.py file and applying to all the methods in this class
class Test_Demo1:

    @pytest.mark.sanity
    def test_Firstprogram(self):
        print("Hello Seshagiri Thommandru")

    @pytest.mark.regression
    #@pytest.mark.skip
    def test_Addition(self):
        a=5
        b=7
        c=a+b
        assert c==12
        print("Addition is:",c)


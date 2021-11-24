import pytest
import logging


@pytest.fixture(scope='class')
def set_up(request):
    # Initialize tests
    print("CLASS SCOPE: SET UP")

    # Do some activity and set an object to hold the result and share over the scope
    local_variable = "Variable value from class fixture"

    # How to share over the scope
    request.cls.setup_variable = local_variable

    yield
    # logging.info("Cleared everything")
    print("CLASS SCOPE: YIELD")

@pytest.fixture
def func_setup():
    logging.info("FUNCTION FIXTURE: Executed")
    return "REUTRNED: from Function Fixture"

@pytest.mark.usefixtures("set_up")     # This is needed when the fixture scope is class
class Test_Example():
    def test_one(self):
        logging.info("Example1: Test1: Executed")

        # How to utilize the object shared from fixture method
        logging.info(f"Local variable from setup: {self.setup_variable} ")

    def test_two(self):
        logging.info("Example1: Test2: Executed")

# class which doesn't want to run fixture
class Test_Example2():
    # How to utilize fuction scope fixture
    def test_one(self,func_setup):
        # Utilizing the returned value from function fixure
        logging.info(f"{func_setup}") 
        logging.info("Example2: Test1: Executed")

    # test that doesn't want to utilize function scope fixture
    def test_two(self):
        logging.info("Example2: Test2: Executed")
    
'''
How to execute the pytest with log cli option
>pytest -rA -o log_cli=true -o log_cli_level="INFO" test_pytest_fixture.py
'''
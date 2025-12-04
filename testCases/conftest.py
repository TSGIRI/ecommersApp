import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launch Chrome Browser .......")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launch Firefox Browser .......")
    elif browser == "edge":
        driver = webdriver.Edge()
        print("Launch Edge Browser .......")
    else:
        raise ValueError("Unsupported browser")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="Specify the browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# -------------- For pytest HTML Report --------------------------

# hook for adding environment info in html report
def pytest_configure(config):
    config.stash[metadata_key]['Project name'] = 'E-commerce Project, Qafox'
    config.stash[metadata_key]['Test Module Name'] = 'Login Test'
    config.stash[metadata_key]['Tester Name'] = 'Seshagiri Thommandru'

# hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop('Plugins', None)



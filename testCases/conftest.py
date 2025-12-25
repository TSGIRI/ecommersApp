import json
import os

import pytest
from jinja2 import TemplateRuntimeError
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

# import datetime for API testing timestamp
from datetime import datetime

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

# this method is used to add custom command line options to pytest (register command line options for browser)
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

    # add timestamp to report file name
    report_dir = "Reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"{report_dir}/report_{now}.html"

# hook for delete/modify environment info in html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop('Plugins', None)

#
# @pytest.fixture(scope="session", autouse=True)
# def setup_teardown(env):
#     print("\nSetting uo the resource ......")
#     yield
#     print("\nTearing down the resource ......")


@pytest.fixture()
def load_user_data():       # load test data from json file
    base_dir = os.path.dirname(os.path.dirname(__file__))  # move one level up
    folder_name = "TestData"
    filename = "test_data.json"
    json_file_path = os.path.join(base_dir,folder_name, filename)

    #json_file_path = os.path.join(os.path.dirname(__file__), "TestData", "test_data.json")
    print(json_file_path)
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data


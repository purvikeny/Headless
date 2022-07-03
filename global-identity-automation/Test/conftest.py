import os
import platform
import pytest
from selenium import webdriver


# @pytest.fixture(scope="class")
@pytest.fixture(params=["chrome"],scope="class")
def setup(request):

    curr_os = str(platform.system())
    if curr_os == 'Darwin':
        if request.param == "chrome":

            options = webdriver.ChromeOptions()
            # options.headless = True
            # driver = webdriver.Chrome(executable_path=os.path.abspath(
            # os.path.join(os.path.abspath(os.path.dirname(__file__)), "../..")) + "/Drivers/chromedriver", options=options)
            options.add_argument("--disable-single-click-autofill")
            driver = webdriver.Chrome(executable_path=os.path.abspath(
               os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + "/Drivers/chromedriver", options=options)
            # driver = webdriver.Chrome( chromedriver_autoinstaller.install(),options=options)

        if request.param == "firefox":
            driver = webdriver.Firefox(
                executable_path="/Drivers/geko/geckodriver")
        if request.param == "incognito":

            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")

            driver = webdriver.Chrome(executable_path=os.path.abspath(
                os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + "/Drivers/chromedriver",
                                      options=options)

        if request.param == "Edge":
            desired_cap = {
                "os": "OS X",
                "os_version": "Catalina",
                "browser": "Edge",
                "browser_version": "89.0.774.54",
                "browserstack.local": "false",
                "browserstack.selenium_version": "3.141.0"
            }


    elif curr_os == 'Windows':

        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options, executable_path=os.path.abspath(
            os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + "/Drivers/chromedriver.exe")


    elif curr_os == 'Linux':
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--headless")
        options.headless=True
        options.add_argument("--disable-single-click-autofill");
        driver = webdriver.Chrome(executable_path=os.path.abspath(
            os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + "/Drivers/UbuntuDriver/chromedriver", options=options)



    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()


def pytest_addoption(parser):
    # Method to add the option to ini
    parser.addini("rp_uuid", 'help', type="pathlist")
    parser.addini("rp_endpoint", 'help', type="pathlist")
    parser.addini("rp_project", 'help', type="pathlist")
    parser.addini("rp_launch", 'help', type="pathlist")


@pytest.hookimpl()
def pytest_configure(config):
    # Sets the launch name based on the marker selected.
    # ssl._create_default_https_context = ssl._create_unverified_context
    suite = config.getoption("markexpr")
    try:
        config._inicache["rp_uuid"] = "74b74f60-4795-41a9-bda7-6f27e410b66b"
        config._inicache["rp_endpoint"] = "http://172.28.15.36:8080"
        config._inicache["rp_project"] = "identity_provider"

        if suite == "gui_test":
            config._inicache["rp_launch"] = "gui_test"
        elif suite == "api_test":
            config._inicache["rp_launch"] = "api_test"

    except Exception as e:
        print(str(e))



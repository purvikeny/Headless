import inspect
import logging
import time

import pytest_check as check
import pytest
import os.path
import os
import platform

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from jproperties import Properties




@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresent(self, linkText):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, linkText)))

    def verifyElementPresent(self, xpathText):
        log = self.getLogging()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, xpathText)))


    def selectOptionByText(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)
        return select.first_selected_option.get_attribute("value")

    def selectOptionByValue(self, locator, valueText):
        select = Select(locator)
        select.select_by_value(valueText)

    def selectOptionByIndex(self, locator, index):
        select = Select(locator)
        select.select_by_index(index)

    def getLogging_backup(self):
        # file = "/Users/diliptripathi/PycharmProjects/IDPAutomation/log.txt"
        file = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + "/log.txt"

        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(file)
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def getLogging(self):
        # file = "/Users/diliptripathi/PycharmProjects/IDPAutomation/log.txt"
        file = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + "/log.txt"
        logging.basicConfig(filename=file, filemode='w', format="%(asctime)s: %(levelname)s: %(name)s :%(message)s",
                            level=logging.DEBUG)
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        return logger

    def pressTab(self, driver):
        action = ActionChains(driver)
        action.send_keys(Keys.TAB).perform()

    def openNewTab(self, driver, Link):

        driver.execute_script("window.open('"+Link+"','new window')")
        time.sleep(3)

    def openNewWindow(self, driver,newWindowLink,Link):
        driver.delete_all_cookies()
        driver.execute_script("window.open('"+newWindowLink+"','" + Link + "','new window')")

    def assertForValidation1(self, actualvalidationmessage, expectedvalidationmessage, validationname):
        log = self.getLogging()
        try:
            check.is_in(actualvalidationmessage, expectedvalidationmessage, validationname)
            assert actualvalidationmessage in expectedvalidationmessage
        except Exception as e:
            log.error("' " + expectedvalidationmessage + " ' " + " expected message not found.")

    def assertForValidation(self, actualvalidationmessage, expectedvalidationmessage, validationname):
        log = self.getLogging()
        try:
            check.is_in(actualvalidationmessage, expectedvalidationmessage, validationname)
            assert actualvalidationmessage in expectedvalidationmessage
        except Exception as e:
            log.error("' " + expectedvalidationmessage + " ' " + " expected message not found.")



    def assertForValidatingText(self, actualvalidationmessage, expectedvalidationmessage, validationfailuremessage):
        log = self.getLogging()
        try:
            assert actualvalidationmessage == expectedvalidationmessage
        except Exception as e:
            log.error(validationfailuremessage)
            self.driver.get_screenshot_as_file(os.path.abspath(
                os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + "/Screenshots/screenshot1.png")

            raise


    def readProperties(self):
        configs = Properties()
        log = self.getLogging()

        with open(os.path.abspath(
                os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + "/Testdata/GUI.properties",
                  'rb') as config_file:
            configs.load(config_file)

        return configs

    def readDataProperties(self):
        configs = Properties()
        log = self.getLogging()

        with open(os.path.abspath(
                os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + "/Testdata/Data.properties",
                  'rb') as config_file:
            configs.load(config_file)

        return configs

    def readAuth0DataProperties(self):
        return self.readDataProperties("/Testdata/Auth0_Data.properties")

    def readDataProperties(self, path):
        configs = Properties()
        log = self.getLogging()

        with open(os.path.abspath(
                os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + path,
                  'rb') as config_file:
            configs.load(config_file)

        return configs

    def visitUrl(self, url):
        self.driver.get(url)




    # @pytest.fixture(scope="session")
    # def rp_logger(request):
    #     import logging
    #     # Import Report Portal logger and handler to the test module.
    #    # from pytest_reportportal import RPLogger, RPLogHandler
    #     # Setting up a logging.
    #     logging.setLoggerClass(RPLogger)
    #     logger = logging.getLogger(__name__)
    #     logger.setLevel(logging.DEBUG)
    #     # Create handler for Report Portal.
    #     rp_handler = RPLogHandler(request.node.config.py_test_service)
    #     # Set INFO level for Report Portal handler.
    #     rp_handler.setLevel(logging.INFO)
    #     return logger

    def pressBack(self, driver):
        action = ActionChains(driver)
        action.send_keys(Keys.DELETE).perform()

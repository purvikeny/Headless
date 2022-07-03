import requests
from numpy.ma import var
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class PasswordLessLoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    noThanksLink = (By.XPATH,"//button[contains(text(),'No Thanks')]")
    noThanksLinkXpath = "//button[contains(text(),'No Thanks')]"


    def clickNoThanksLink(self):
        return self.driver.find_element(*PasswordLessLoginPage.noThanksLink).click()

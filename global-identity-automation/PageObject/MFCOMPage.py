import requests
from numpy.ma import var
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    loginWidgetHeading = (By.XPATH,"//img[@class='ca8e2b5d8 cfbe9398e']")


    def clickLogin(self):
        return self.driver.find_element(*LoginPage.loginWidgetHeading).text

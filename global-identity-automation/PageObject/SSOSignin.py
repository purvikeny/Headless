import requests
from numpy.ma import var
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class SSOSignin(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    oktaloginPageHeading = (By.XPATH,"//div[@class='applogin-container']/p")
    oktausername = (By.XPATH,"//input[@id='okta-signin-username']")
    oktaUsernameXpath = "//input[@id='okta-signin-username']"
    oktapassword = (By.XPATH,"//input[@id='okta-signin-password']")
    oktaSubmitbutton = (By.XPATH,"//input[@id='okta-signin-submit']")

    usermenuOktaHomePage = (By.XPATH,"//div[@class='dropdown-menu--button-content']")
    signoutOKtaHomePage = (By.XPATH,"//a[@data-se='topbar--sign-out']")

    unableToSigninErrorMessage = (By.XPATH,"//div[@class='okta-form-infobox-error infobox infobox-error']")
    unableToSigninErrorMessageXpath = "//div[@class='okta-form-infobox-error infobox infobox-error']"

    def getOktaLoginPageHeadingText(self):
        return self.driver.find_element(*SSOSignin.oktaloginPageHeading).text

    def enterUsernameOkta(self, username):
        return self.driver.find_element(*SSOSignin.oktausername).send_keys(username)

    def enterPasswordOkta(self, password):
        return self.driver.find_element(*SSOSignin.oktapassword).send_keys(password)

    def clickSubmitButton(self):
        return self.driver.find_element(*SSOSignin.oktaSubmitbutton).click()


    def clickuserMenuHomePage(self):
        return self.driver.find_element(*SSOSignin.usermenuOktaHomePage).click()

    def clicksignutButtonHomePage(self):
        return self.driver.find_element(*SSOSignin.signoutOKtaHomePage).click()

    def getUnableToSigninErrorMessageOkta(self):
        return self.driver.find_element(*SSOSignin.unableToSigninErrorMessage).text

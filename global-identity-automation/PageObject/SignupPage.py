from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class SignupPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    signupPageHeading = (By.XPATH,"//div[@class='box-container prompt-wrapper customize']/main[1]/section[1]/div[1]/div[1]/header[1]/h1[1]")
    signupPageXpath = "//div[@class='box-container prompt-wrapper customize']/main[1]/section[1]/div[1]/div[1]/header[1]/h1[1]"

    auth0AcceptButton = (By.XPATH,"//button[contains(text(),'Accept')]")
    auth0AcceptButtonXpath = "//button[contains(text(),'Accept')]"
    auth0PageHeadingText = (By.XPATH,"//h1[contains(text(),'Authorize App')]")

    continueButtonSigninPage = (By.XPATH,"//button[@type='submit']")

    emailId = (By.XPATH,"//input[@id='email']")


    def getUnlockUserLinkExpireMessage(self):
        return self.driver.find_element(*SignupPage.signupPageHeading).text

    def enterEmail(self, username):
        return self.driver.find_element(*SignupPage.emailId).send_keys(username)

    def clickContinueButton(self):
        return self.driver.find_element(*SignupPage.continueButtonSigninPage).click()

    def clickAcceptButton(self):
        return self.driver.find_element(*SignupPage.auth0AcceptButton).click()

    def getauth0AuthorizepageHeading(self):
        return self.driver.find_element(*SignupPage.auth0PageHeadingText).text

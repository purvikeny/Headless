import requests
from numpy.ma import var
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    loginWidgetHeading = (By.XPATH,"//img[@class='ca8e2b5d8 cfbe9398e']")
    # loginHeadingText = (By.XPATH,"//h1[@class='c721a6d7b cb9685887']")
    # loginHeadingTextXpath = "//h1[@class='c721a6d7b cb9685887']"
    loginHeadingText = (By.XPATH, "//h1[contains(text(),'Log in to your account')]")
    loginHeadingTextXpath ="//h1[contains(text(),'Log in to your account')]"
    # emailTextBox = (By.XPATH,"//input[@class='input cc8bfb9a6 ca8b02616']")
    emailTextBox = (By.XPATH,"//input[@inputmode='email']")
    # emailTextBoxPlaceHolder = (By.XPATH,"//div[@class='c04a6db7a js-required cd604489d c4a3729db']")
    emailTextBoxPlaceHolder = (By.XPATH,"//div[@data-dynamic-label-for='username']")
    submitButton = (By.XPATH,"//button[@class='c6f5e4a52 cfe14b7ad c2b640e68 c0d0f40d8 _button-login-id']")
    signupPageRedirectText = (By.XPATH,"//main[@class='_widget login-id']/section[1]/div[1]/div[1]/div[1]/div[1]/p[1]")
    signupLinkText = (By.XPATH,"//a[@class='ca1a7d858 c247016a1']")
    invalidEmailErrorMessage = (By.XPATH,"//span[@class='ulp-input-error-message']")
    invalidEmailErrorMessageXpath = "//span[@class='ulp-input-error-message']"
    continueButton = (By.XPATH,"//button[@type='submit']")

    configurationIssueHeadingerrorPageHeading = (By.XPATH,"//h3[contains(text(),'Oops!, something went wrong')]")
    configurationIssueHeadingerrorPageHeadingXpath = "//h3[contains(text(),'Oops!, something went wrong')]"


    def getSigninPageWidgetHeadingText(self):
        return self.driver.find_element(*LoginPage.loginWidgetHeading).text

    def getLoginHeadingText(self):
        return self.driver.find_element(*LoginPage.loginHeadingText).text

    def verifyEmailTextBoxisDisplayed(self):
        return self.driver.find_element(*LoginPage.emailTextBox).is_displayed()

    def verifyEmailTextBoxisEnabled(self):
        return self.driver.find_element(*LoginPage.emailTextBox).is_enabled()

    def getEmailTextBoxPlaceholder(self):
        return self.driver.find_element(*LoginPage.emailTextBoxPlaceHolder).text


    def verifycontinueButtonisDisplayed(self):
        return self.driver.find_element(*LoginPage.continueButton).is_displayed()

    def verifycontinueButtonisEnabled(self):
        return self.driver.find_element(*LoginPage.continueButton).is_enabled()

    def getSignupPageRedirectText(self):
        return self.driver.find_element(*LoginPage.signupPageRedirectText).text

    def getSignupLinkText(self):
        return self.driver.find_element(*LoginPage.signupLinkText).text

    def emailTextBoxEnterData(self, username):
        return self.driver.find_element(*LoginPage.emailTextBox).send_keys(username)

    def ClearEmailField(self):
        emailField = self.driver.find_element(*LoginPage.emailTextBox)
        return self.driver.execute_script("arguments[0].value='';", emailField)

    def getEmailText(self):
        return self.driver.find_element(*LoginPage.emailTextBox).get_attribute("value")

    def clickContinueButton(self):
        return self.driver.find_element(*LoginPage.continueButton).click()

    def getInvalidEmailErrorMessage(self):
        return  self.driver.find_element(*LoginPage.invalidEmailErrorMessage).text

    def getClearEmailField(self):
        # return self.driver.find_element(*LoginPage.emailTextBox).clear()
        emailField = self.driver.find_element(*LoginPage.emailTextBox)
        return self.driver.execute_script("arguments[0].value='';", emailField)

    def getEmailTextTooltip(self):
        return self.driver.find_element(*LoginPage.emailTextBox).get_attribute("title")

    def getconfigurationIssueHeadingerrorPageHeading(self):
        return self.driver.find_element(*LoginPage.configurationIssueHeadingerrorPageHeading).text

    def clickSubmitButton(self):
        return  self.driver.find_element(*LoginPage.continueButton).click()



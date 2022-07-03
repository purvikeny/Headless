from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class PasswordPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    emailTextBox = (By.XPATH,"//span[@class='ulp-authenticator-selector-text']")
    passwordTextBox = (By.XPATH, "//input[@id='password']")
    # passwordTextBoxXpath = "//input[@id='password']"
    passwordTextBoxXPATH = "//input[@id='password']"
    continueButton = (By.XPATH,"//button[@class='c6f5e4a52 cfe14b7ad c2b640e68 c0d0f40d8 _button-login-password']")
    submitButton = (By.XPATH,"//button[@type='submit']")
    passwordTextBoxPlaceholder = (By.XPATH,"//div[@class='c04a6db7a js-required cd604489d c5f0818ed']")
    passwordTextBoxPlaceHolder1 = (By.XPATH,"//div[@data-dynamic-label-for='password']")
    # continueButton = (By.XPATH,"//button[@type='submit']")
    forgotPasswordLink = (By.XPATH,"//a[contains(text(),'Forgot password?')]")
    # forgotPasswordLink = (By.XPATH,"//a[@href='/u/reset-password/request/Username-Password-Authentication?state=hKFo2SBvTUl5LXJPLVRRMWhmX19SNEUyV3dWbTRVYWtwMFhUY6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFN5US05RmV2dWNyUFF6MV9CWDNRV1NYblZYdHpoYUdQo2NpZNkgYWhldFRmNEw3bllWaGo5Q1pEZWFaRGxMd2VORWpvUjg']") # editLink = (By.XPATH,"//a[@class='ca1a7d858 c3cd40a9f c9a867157 c247016a1']")
    # editLink = (By.XPATH,"//a[@href='/u/login/identifier?state=hKFo2SBkY0pJSlJtY2Q0VXNQblJKMkpBckZvR1FmeUh2dVdGLaFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIE5ISFcxbHBzUXZnQ2lzejIzbWZJSDNXMDg2VDVEOTVqo2NpZNkgYWhldFRmNEw3bllWaGo5Q1pEZWFaRGxMd2VORWpvUjg']")
    editLinkXpath = "//a[@class='ca1a7d858 c3cd40a9f c9a867157 c247016a1']"
    editLink = (By.XPATH,"//a[contains(text(),'Edit')]")
    editLinkXpath = "//a[contains(text(),'Edit')]"
    incorrectPasswordErrorMessage = (By.XPATH,"//span[@class='ulp-input-error-message']")
    incorrectPasswordErrorMessageXpath = "//span[@id='error-element-password']"

    incorrectPasswordErrorMessage1 = (By.XPATH, "//*[@id='error-element-password']")

    # lockUserErrorMessage = (By.XPATH, "//p[@class='c14a0dfe1 c5f6ab4f5']")
    # lockUserErrorMessageXpath = "//p[@class='c14a0dfe1 c5f6ab4f5']"
    lockUserErrorMessage = (By.XPATH, "//div[@data-error-code='user-blocked']")
    lockUserErrorMessageXpath = "//div[@data-error-code='user-blocked']"



    errorMessagePage = (By.XPATH,"//h3[@class='error-subtitle']")
    errorMessagePageXpath="//h3[@class='error-subtitle']"


    def passwordTextBoxEnterData(self, username):
        return self.driver.find_element(*PasswordPage.passwordTextBox).send_keys(username)

    def doubleClickOnPasswordTextField(self):
        action = ActionChains(self.driver)
        # double click operation and perform
        action.double_click(self.driver.find_element(*PasswordPage.passwordTextBox)).perform()

    def getpasswordTextBoxData(self):
        return self.driver.find_element(*PasswordPage.passwordTextBox).get_attribute('textContent')

    def clickContinueButton(self):
        return  self.driver.find_element(*PasswordPage.submitButton).click()

    def clickSubmitButton(self):
        return  self.driver.find_element(*PasswordPage.submitButton).click()

    def verifypasswordTextFieldisDisplayed(self):
        return self.driver.find_element(*PasswordPage.passwordTextBox).is_displayed()

    def verifyPasswordTextFieldisEnabled(self):
        return self.driver.find_element(*PasswordPage.passwordTextBox).is_enabled()

    def getpasswordTextBoxPlaceholder(self):
        return self.driver.find_element(*PasswordPage.passwordTextBoxPlaceHolder1).text

    def verifycontinueButtonisDisplayed(self):
        return self.driver.find_element(*PasswordPage.submitButton).is_displayed()

    def verifycontinueButtonisEnabled(self):
        return self.driver.find_element(*PasswordPage.submitButton).is_enabled()

    def getForgotPasswordLink(self):
        return  self.driver.find_element(*PasswordPage.forgotPasswordLink).text

    def getEditLink(self):
        return self.driver.find_element(*PasswordPage.editLink).text

    def clickEditLink(self):
        return  self.driver.find_element(*PasswordPage.editLink).click()

    def getIncorrectPasswordErrorMessage(self):
        return  self.driver.find_element(*PasswordPage.incorrectPasswordErrorMessage).text

    def getIncorrectPasswordErrorMessage1(self):
        return  self.driver.find_element(*PasswordPage.incorrectPasswordErrorMessage1).text

    def getEmailTextBoxData(self):
        return self.driver.find_element(*PasswordPage.emailTextBox).text

    def getLockUserErrorMessage(self):
        return self.driver.find_element(*PasswordPage.lockUserErrorMessage).text

    def checkEmailFieldIsEnabled(self, username):
        return  self.driver.find_element(*PasswordPage.emailTextBox).send_keys(username)

    def get429errorMessagePageText(self):
        return  self.driver.find_element(*PasswordPage.errorMessagePage).text






import platform
from datetime import time

import requests
import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class ChangePassword(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    monotypeBrandingImage = (By.XPATH,"//div[@class='m-logo']")
    changePasswordHeading = (By.XPATH,"//div[@class='box-container prompt-wrapper customize']/main[1]/section[1]/div[1]/div[1]/header[1]/h1[1]")
    changePasswordHeadingText = "//div[@class='box-container prompt-wrapper customize']/main[1]/section[1]/div[1]/div[1]/header[1]/h1[1]"

    newPasswordTextBox= (By.XPATH,"//input[@id='password-reset']")
    confirmPasswordTextBox = (By.XPATH,"//input[@id='re-enter-password']")

    confirmPasswordPlaceHolder = (By.XPATH,"//div[@data-dynamic-label-for='re-enter-password']")
    resetPasswordButton = (By.XPATH,"//button[@type='submit']")

    passwordWidget = (By.XPATH,"//div[@class='c5c7406ba no-arrow c77aae38f c4fc09425 cb3c94001 c70044673 c6c0df2dd _hide']")

    ########
    # changePasswordConfirmationHeadingText = (By.XPATH,"//div[@class='cefa372c3 c0fa6544d c55fc2594']")
    # changePasswordConfirmationHeadingXpathText = "//div[@class='cefa372c3 c0fa6544d c55fc2594']"

    changePasswordConfirmationcontent = (By.XPATH, "//p[contains(text(),'Your password has been changed successfully.')]")
    changePasswordConfirmationcontentTextXpath = "//p[contains(text(),'Your password has been changed successfully.')]"

    changePasswordConfirmationHeading = (By.XPATH,"//div[@class='box-container prompt-wrapper']/main[1]/section[1]/div[1]/div[1]/section[1]/h1[1]")
    changePasswordConfirmationHeadingXpath = "//div[@class='box-container prompt-wrapper']/main[1]/section[1]/div[1]/div[1]/section[1]/h1[1]"

    passwordPreviouslyUserErrorMessage = (By.XPATH,"//span[@data-error-code='password-previously-used']")
    passwordPreviouslyUserErrorMessageXpath = "//span[@data-error-code='password-previously-used']"

    backToMonotypeFontButton = (By.XPATH,"//a[contains(text(),'Back to Monotype Last_Queries')]")
    backToMonotypeFontButtonXPATH = "//a[contains(text(),'Back to Monotype Last_Queries')]"


    backToMyFontButton = (By.XPATH, "//a[contains(text(),'Back to MyFonts')]")
    backToMyFontButtonXPATH = "//a[contains(text(),'Back to MyFonts')]"

    showPasswordButtonInNewPasswordTextField = (By.XPATH,"//div[@class='box-container prompt-wrapper customize']/main[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[@class='input-wrapper _input-wrapper']/div[1]/button[1]")
    showPasswordButtonXpathInNewPasswordTextField = "//div[@class='box-container prompt-wrapper customize']/main[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[@class='input-wrapper _input-wrapper']/div[1]/button[1]"

    showPasswordButtonInReEnterPasswordTextField = (By.XPATH,
       "//body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]")
    showPasswordButtonXpathInReEnterNewPasswordTextField = "//body/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/main[1]/section[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]"

    def getChangePasswordHeading(self):
        return self.driver.find_element(*ChangePassword.changePasswordHeading).text

    def getnewPasswordTextBox(self):
        return self.driver.find_element(*ChangePassword.newPasswordTextBox).text

    def getnewPasswordTextBox1(self):
        return self.driver.find_element(*ChangePassword.newPasswordTextBox).get_attribute("value")

    def newPasswordEnterData(self, username):
        return self.driver.find_element(*ChangePassword.newPasswordTextBox).send_keys(username)

    def getconfirmPassword(self):
        return self.driver.find_element(*ChangePassword.confirmPasswordTextBox).text

    def getConfirmPasswordTextBox1(self):
        return self.driver.find_element(*ChangePassword.confirmPasswordTextBox).get_attribute("value")

    def confirmPasswordData(self, username):
        return self.driver.find_element(*ChangePassword.confirmPasswordTextBox).send_keys(username)

    def getConfirmPasswordPlaceholder(self):
        return self.driver.find_element(*ChangePassword.confirmPasswordPlaceHolder).text

    def getresetPasswordButtonText(self):
        return self.driver.find_element(*ChangePassword.resetPasswordButton).text

    def clickresetPasswordButtonText(self):
        return self.driver.find_element(*ChangePassword.resetPasswordButton).click()

    def passwordWidgetDisplayed(self):
        return self.driver.find_element(*ChangePassword.resetPasswordButton).get_attribute("data-shown")

    def getchangePasswordConfirmationHeading(self):
        return self.driver.find_element(*ChangePassword.changePasswordConfirmationHeading).text

    def getpasswordPreviouslyUserErrorMessage(self):
        return self.driver.find_element(*ChangePassword.passwordPreviouslyUserErrorMessage).text

    def getBackToMonotypeFontButtonText(self):
        return self.driver.find_element(*ChangePassword.backToMonotypeFontButton).text

    def getBackToMyFontButtonText(self):
        return self.driver.find_element(*ChangePassword.backToMyFontButton).text

    def ClickBackToMonotypeFontButton(self):
        return self.driver.find_element(*ChangePassword.backToMonotypeFontButton).click()

    def ClickBackToMyButton(self):
        return self.driver.find_element(*ChangePassword.backToMyFontButton).click()

    def backToMonotypeFontButtonDisplayed(self):
        return self.driver.find_element(*ChangePassword.backToMonotypeFontButton).is_displayed()


    def backToMonotypeFontButtonEnabled(self):
        return self.driver.find_element(*ChangePassword.backToMonotypeFontButton).is_enabled()

    def backToMyFontButtonDisplayed(self):
        return self.driver.find_element(*ChangePassword.backToMyFontButton).is_displayed()


    def backToMyFontButtonEnabled(self):
        return self.driver.find_element(*ChangePassword.backToMyFontButton).is_enabled()


    def clickShowPasswordButtonInNewPasswordTextField(self):
        return self.driver.find_element(*ChangePassword.showPasswordButtonInNewPasswordTextField).click()

    def clickShowPasswordButtonInReEnterPasswordTextField(self):
        return self.driver.find_element(*ChangePassword.showPasswordButtonInReEnterPasswordTextField).click()


    def getchangePasswordConfirmationContent(self):
        return self.driver.find_element(*ChangePassword.changePasswordConfirmationcontent).text





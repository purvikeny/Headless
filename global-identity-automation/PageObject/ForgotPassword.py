from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class ForgotPasswordPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    # forgotPassword = (By.XPATH,
    #                   "//div[@class='box-container prompt-wrapper customize']/main[1]/section[1]/div[1]/div[1]/div[1]/form[1]/p[1]/a[1]")
    # forgotPasswordXpath = "//div[@class='box-container prompt-wrapper customize']/main[1]/section[1]/div[1]/div[1]/div[1]/form[1]/p[1]/a[1]"

    forgotPassword = (By.XPATH,"//a[contains(text(),'Forgot password?')]")
    forgotPasswordXpath = "//a[contains(text(),'Forgot password?')]"

    emailLabel = (By.XPATH,"//label[@for='email']")
    # forgotPasswordPageHeading = (By.XPATH,"//h1[@class='ce923f90f cf2d2fa04']")
    # forgotPasswordPageHeadingXpath = "//h1[@class='ce923f90f cf2d2fa04']"
    forgotPasswordPageHeading = (By.XPATH, "//h1[contains(text(),'Forgot Your Password?')]")
    forgotPasswordPageHeadingXpath = "//h1[contains(text(),'Forgot Your Password?')]"
    # "//h1[contains(text(),'Forgot Your Password?')]"

    emailTextBox = (By.XPATH,"//input[@id='email']")
    submitButton = (By.XPATH,"//button[@type='submit']")

    forgotPasswordConfirmationPageHeading = (By.XPATH,"//div[@class='box-container prompt-wrapper']/main[1]/section[1]/div[1]/div[1]/section[1]/h1[1]")
    forgotPasswordConfirmationPageHeadingXpath = "//div[@class='box-container prompt-wrapper']/main[1]/section[1]/div[1]/div[1]/section[1]/h1[1]"
    forgotPasswordConfirmationPageContent = (By.XPATH,"//p[contains(text(),'Please check the email address ')]")
    forgotPasswordConfirmationPageContentXpath = "//div[@class='box-container prompt-wrapper']/main[1]/section[1]/div[1]/div[1]/section[1]/div[1]"

    resendEmailButton = (By.XPATH,"//button[@value='resend-email-action']")


    def clickForgotpasswordLink(self):
        return self.driver.find_element(*ForgotPasswordPage.forgotPassword).click()

    def getEmailLabel(self):
        return self.driver.find_element(*ForgotPasswordPage.emailLabel).text

    def getForgotPasswordPageHeading(self):
        return self.driver.find_element(*ForgotPasswordPage.forgotPasswordPageHeading).text

    def getdataFromEmailTextBox(self):
        return self.driver.find_element(*ForgotPasswordPage.emailTextBox).get_attribute('value')

    def enterDataEmailTextBox(self, username):
        return self.driver.find_element(*ForgotPasswordPage.emailTextBox).send_keys(username)

    def getClearEmailField(self):
        emailField = self.driver.find_element(*ForgotPasswordPage.emailTextBox)
        return self.driver.execute_script("arguments[0].value='';", emailField)

    def clickContinueButton(self):
        return self.driver.find_element(*ForgotPasswordPage.submitButton).click()

    def getcontinueButtonText(self):
        return self.driver.find_element(*ForgotPasswordPage.submitButton).text

    def getConfirmationPasswordPageHeading(self):
        return self.driver.find_element(*ForgotPasswordPage.forgotPasswordConfirmationPageHeading).text

    def getforgotPasswordConfirmationPageContent(self):
        return self.driver.find_element(*ForgotPasswordPage.forgotPasswordConfirmationPageContent).text

    def getResendEmailButtonText(self):
        return self.driver.find_element(*ForgotPasswordPage.resendEmailButton).text

    def clickResendEmailButton(self):
        return self.driver.find_element(*ForgotPasswordPage.resendEmailButton).click()





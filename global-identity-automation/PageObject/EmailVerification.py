from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class EmailVerification(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    emailVerfiedHeading = (By.XPATH,"//h1[contains(text(),'Email Verified')]")
    emailVerfiedHeadingXpath = "//h1[contains(text(),'Email Verified')]"

    emailVerifiedErrorPageHeading = (By.XPATH,"//h1[contains(text(),'Error')]")
    emailVerifiedErrorPageHeadingXpath = "//h1[contains(text(),'Error')]"

    emailVerifiedErrorPageHeadingContent = (By.XPATH,"//*[contains(text(),'Your email address could not be verified.')]")

    continueButton = (By.XPATH,"//a[contains(text(),'Continue')]")

    def getEmailVerifiedHeading(self):
        return self.driver.find_element(*EmailVerification.emailVerfiedHeading).text

    def getEmailVerifiedErrorPageHeading(self):
        return self.driver.find_element(*EmailVerification.emailVerifiedErrorPageHeading).text


    def getEmailVerifiedErrorPageContent(self):
        return self.driver.find_element(*EmailVerification.emailVerifiedErrorPageHeadingContent).text

    def getBackToMonotypeFontButtonText(self):
        return self.driver.find_element(*EmailVerification.continueButton).text
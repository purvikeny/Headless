from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class LockUserPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    accountUnlockSuccesfullHeading = (By.XPATH,"//h3[contains(text(),'Account Unblocked')]")
    accountUnlockSuccesfullHeadingXpath = "//h3[contains(text(),'Account Unblocked')]"
    accountUnlockSuccesfullHeadingText = (By.XPATH,
                                          "//div[@class='auth0-lock-confirmation-content']/p[1]/span[contains(text(),'Your account has been unblocked.')]")

    accountUnlockUnSuccesfullHeading = (By.XPATH, "//h3[contains(text(),'Authentication Error')]")
    accountUnlockUnSuccesfullHeadingXpath = "//h3[contains(text(),'Authentication Error')]"

    unlockLinkExpireHeading = (By.XPATH,"//h3[contains(text(),'Authentication Error')]")
    unlockLinkExpireHeadingXpath = "//h3[contains(text(),'Authentication Error')]"

    unlockUserLinkExpireErrorMessage=(By.XPATH,"//div[@class='auth0-lock-confirmation-content']/p[1]/span[1]")
    unlockUserLinkExpireErrorMessageXpath="//div[@class='auth0-lock-confirmation-content']/p[1]/span[1]"

    helpAndsupportLink = (By.XPATH,"//a[@class='footer-group-link has-icon customer-support']")
    helpAndsupportLinkXpath = "//a[@class='footer-group-link has-icon customer-support']"
    supportMonotypeMail = (By.XPATH,"//a[@class='footer-group-link has-icon mail']")
    supportMonotypeMailXpath ="//a[@class='footer-group-link has-icon mail']"



    def getUnlockUserLinkExpireMessage(self):
        return self.driver.find_element(*LockUserPage.unlockUserLinkExpireErrorMessage).text

    def getHelpAndSuportLinkText(self):
        return self.driver.find_element(*LockUserPage.helpAndsupportLink).text

    def getAccountunlocksuccessfulHeading(self):
        return self.driver.find_element(*LockUserPage.accountUnlockSuccesfullHeading).text

    def getSupportmonotypeEmailtext(self):
        return self.driver.find_element(*LockUserPage.supportMonotypeMail).text

    def getUnblockLinkExpire(self):
        return self.driver.find_element(*LockUserPage.unlockLinkExpireHeading).text

    def getUnblockLinkExpireErrorMessage(self):
        return self.driver.find_element(*LockUserPage.unlockUserLinkExpireErrorMessage).text


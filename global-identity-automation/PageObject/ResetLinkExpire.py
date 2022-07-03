import platform
from datetime import time

import requests
import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class ResetPasswordLinkExpire(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    # resetLinkExpireErrorMessage = (By.XPATH,"//div[@class='box-container prompt-wrapper']/main[1]/section[1]/div[1]/div[1]/section[1]/div[1]")
    # resetLinkExpireErrorMessageXpath = "//div[@class='box-container prompt-wrapper']/main[1]/section[1]/div[1]/div[1]/section[1]/div[1]"

    resetLinkExpireErrorMessage = (By.XPATH,"//p[contains(text(),'This link has already been used. To reset your pas')]")
    resetLinkExpireErrorMessageXpath = "//p[contains(text(),'This link has already been used. To reset your pas')]"

    invalidLinkHeading = (By.XPATH,"//div[@class='box-container prompt-wrapper']/main[1]/section[1]/div[1]/div[1]/section[1]/h1[1]")
    invalidLinkHeadingXpath = "//div[@class='box-container prompt-wrapper']/main[1]/section[1]/div[1]/div[1]/section[1]/h1[1]"

    linkExpireHeading = (By.XPATH,"//h1[contains(text(),'Link Expired')]")
    linkExpireHeadingXpath = "//h1[contains(text(),'Link Expired')]"

    likExpireContent = (By.XPATH,"//p[contains(text(),'To reset your password, return to the login page a')]")
    likExpireContentXpath = "//p[contains(text(),'To reset your password, return to the login page a')]"

    def getresetLinkExpireText(self):
        return  self.driver.find_element(*ResetPasswordLinkExpire.resetLinkExpireErrorMessage).text

    def getresetLinkExpireHeading(self):
        return  self.driver.find_element(*ResetPasswordLinkExpire.invalidLinkHeading).text

    def getLinkExpireHeading(self):
        return self.driver.find_element(*ResetPasswordLinkExpire.linkExpireHeading).text

    def getLinkExpireContent(self):
        return self.driver.find_element(*ResetPasswordLinkExpire.likExpireContent).text


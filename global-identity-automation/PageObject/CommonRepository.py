import platform
from datetime import time

import requests
import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class CommonRepository(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    footerHeadingSignIn = (By.XPATH,"//div[@class='footer-copy-text']/p[1]")
    tearmsosuseFooter = (By.LINK_TEXT,"Terms of Use")
    privacyPolicyFooter = (By.LINK_TEXT,"Privacy Policy")
    contactFooter = (By.LINK_TEXT,"Contact")
    demoMobileRightBox = (By.XPATH,"//div[@class='right-box']/a[3]")
    demoTabletRightBox = (By.XPATH,"//div[@class='right-box']/a[2]")
    demoSmallerDesktop = (By.XPATH,"//div[@class='right-box']/a[1]")
    monotypeBrandingImage = (By.XPATH,"//div[@class='m-logo']")


    def clickLoginLink(self):
        return self.driver.find_element(*CommonRepository.loginLink).click()

    def getMonotypeBrandingImage(self):
        monotypeBrandingImageattribute = self.driver.find_element(*CommonRepository.monotypeBrandingImage).get_attribute("alt")
        return monotypeBrandingImageattribute



    def getAllLinksOnAPage(self):
        minstr = "https://www.monotype.com/"
        links = self.driver.find_elements_by_css_selector("a")
        images = self.driver.find_elements_by_css_selector("img")
        log = self.getLogging()
        thisset = set()
        for link in links:
            str1 = str(link.get_attribute('href'))
            if minstr in str1:
                thisset.add(link.get_attribute('href'))

                log.info(link.get_attribute('href'))
        for i in thisset:
            time.sleep(0.5)
            s = requests.get(i)

            if "200" in str(s.status_code):
                log.info(i + " is workng fine ")
            else:
                log.info(i + "  is broken")


    def verifyFooterHeading1(self, page):
        if page in  "SignIN":
            footerheading1 = self.driver.find_element(*CommonRepository.footerHeadingSignIn).text
            if footerheading1 is None:
                result = "None"
        elif page in  "UserProfile":
            footerheading1 = self.driver.find_element(*CommonRepository.footerHeadingSignIn).text
            if footerheading1 is None:
                result = "None"
        elif page in "SignUP":
            footerheading1 = self.driver.find_element(*CommonRepository.footerHeadingSignIn).text
            if footerheading1 is None:
                result = "None"

        elif page in "IDPPAssword":
            footerheading1 = self.driver.find_element(*CommonRepository.footerHeadingSignIn).text
            if footerheading1 is None:
                result = "None"

        elif page in "ResetLinkExpire":
            footerheading1 = self.driver.find_element(*CommonRepository.footerHeadingSignIn).text
            if footerheading1 is None:
                result = "None"


        return footerheading1



    def verifyFooterHeading2(self):
        return self.driver.find_element(*CommonRepository.tearmsosuseFooter).text


    def clicktermsOfUseFooterHeading(self):
        return self.driver.find_element(*CommonRepository.tearmsosuseFooter).click()


    def verifyFooterHeading3(self):
        return self.driver.find_element(*CommonRepository.privacyPolicyFooter).text

    def clickPrivacyPolicyFooterHeading(self):
        return self.driver.find_element(*CommonRepository.privacyPolicyFooter).click()

    def verifyFooterHeading6(self):
        return self.driver.find_element(*CommonRepository.contactFooter).text

    def clickContactFooterHeading(self):
        return self.driver.find_element(*CommonRepository.contactFooter).click()

    def getdemoMobileText(self):
        return self.driver.find_element(*CommonRepository.demoMobileRightBox).text

    def getdemoTabletText(self):
        return self.driver.find_element(*CommonRepository.demoTabletRightBox).text

    def getdemoSmallerDesktop(self):
        return self.driver.find_element(*CommonRepository.demoSmallerDesktop).text




import platform
from datetime import time

import requests
import time
from numpy.ma import var
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
#from PageObjectOld.PasswordPage import PasswordPage
from utilities.BaseClass import BaseClass


class CommonRepository1(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    monotypeBrandingImageSignIn = (By.XPATH, "//img[@alt='Monotype']")
    monotypeBrandingImageUserProfile = (By.XPATH,"//body/div[@id='__next']/div[1]/div[1]/div[1]/div[1]/img[1]")
    monotypeBrandingImageUserProfileXPATH = "//body/div[@id='body-wrapper-userprofile']/div[1]/div[1]/div[1]/img[1]"
    monotypeBrandingImageSignup = (By.XPATH,"//img[@alt='Monotype']")
    MonotypeBrandingImageResetLinkExpire = (By.XPATH, "//img[@alt='Monotype']")
    footerHeadingSignIn = (By.XPATH,"//div[@class='footer']/h2[1]")
    footerHeadingUserProfile = (By.XPATH,"//div[@class='footer']/h2[1]")
    footerHeadingSignUp = (By.XPATH,"//div[@class='footer']/h2[1]")
    footerHeadingIDPPassword = (By.XPATH,"//body/div[3]/div[@class='footer']/h2[1]")
    footerHeadingResetLinkExpirePage = (By.XPATH,"//div[@class='footer']/h2[1]")
    footerHeading1 = (By.XPATH, "// h2[contains(text(), '© 2020 Monotype Imaging Inc.')]")
    trademarkFooterHeading = (By.XPATH,"//a[@class='trademarks']")
    tearmsosuseFooter = (By.XPATH,"//a[@class='termsOfUse']")
    termsandConditionFooter = (By.XPATH, "//a[@class='termsAndConditions']")
    privacyPolicyFooter = (By.XPATH, "//a[@class='privacyPolicy']")
    privacyPolicyFooter1 = (By.XPATH,"//div[@id='body-wrapper-signin']/div[2]/ul[1]/li[4]/a[1]")
    contactFooter = (By.XPATH, "//a[@class='contact']")
    passwordPolicyValidation1 = (By.XPATH, "//span[contains(text(),'8 character')]")
    closeAcceptCookieButton = (By.XPATH, "//button[@class='optanon-alert-box-close banner-close-button']")
    invalidUser404 = (By.XPATH,"//h1[@class='page-title']")
    alreadyAccounterrorMessage = (By.XPATH,"//div[@class='alreadyAccount']")
    trademarkLinks = (By.XPATH,"//*[@class='js-form-item form-item js-form-type-textfield form-type-textfield js-form-item-search form-item-search']")
    bodyTagName = (By.TAG_NAME,"body")
    logOutButton = (By.XPATH, "//a[contains(text(),'Log out')]")
    eightCharacterPasswordPolicy = (By.XPATH,"//li[@data-error-code='password-policy-length-at-least']")
    specialCharacterPasswordPolicy = (By.XPATH, "//li[@data-error-code='password-policy-special-characters']")
    # specialCharacterPasswordPolicy = (By.XPATH, "//span[@class='c599fcc04']")
    lowercasePasswordPolicy = (By.XPATH, "//li[@data-error-code='password-policy-lower-case']")
    upperCasePasswordPolicy = (By.XPATH,"//li[@data-error-code='password-policy-upper-case']")
    numberPasswordPolicy = (By.XPATH,"//li[@data-error-code='password-policy-numbers']")
    countryDropdown = (By.XPATH,"//select[@name='country']")
    somethingWentWrongErrorMessage = (By.XPATH,"//div[@class='form-signin']/h1[1]")
    somethingWentWrongErrorMessageXpath = "//div[@class='form-signin']/h1[1]"
    loginLink =(By.XPATH,"//a[@href='/']")
    loginLinkXpath = "//a[@href='/']"
    ########################

    auth0AcceptButton = (By.XPATH,"//button[@value='accept']")
    auth0AcceptButtonXpath = "//button[@value='accept']"



    def getspecialCharacterPasswordPolicy(self):
        return  self.driver.find_element(*CommonRepository1.specialCharacterPasswordPolicy).get_property('checked')



    def getLowerCaserPasswordPolicy(self):
        return  self.driver.find_element(*CommonRepository1.lowercasePasswordPolicy).get_property('checked')

    def getEightCharacterrPasswordPolicy(self):
        return  self.driver.find_element(*CommonRepository1.eightCharacterPasswordPolicy).get_property('checked')

    def getUpperCasePasswordPolicy(self):
        return  self.driver.find_element(*CommonRepository1.upperCasePasswordPolicy).get_property('checked')

    def getnumberPasswordPolicy(self):
        return  self.driver.find_element(*CommonRepository1.numberPasswordPolicy).get_property('checked')


    def opennewTab1(self):
        return self.driver.execute_script('''window.open("about:blank", "_blank");''')

    def emailTextBoxEnterData(self, valueInText):
        return self.driver.find_element(*CommonRepository1.trademarkLinks).send_keys(valueInText)

    def getMonotypeBrandingImage(self, page):
        if page in  "SignIN":
            monotypeBrandingImageattribute = self.driver.find_element(
                *CommonRepository1.monotypeBrandingImageSignIn).get_attribute("alt")
            if monotypeBrandingImageattribute is None:
                result = "None"

        elif page in "SignUP":
            monotypeBrandingImageattribute = self.driver.find_element(
                *CommonRepository1.monotypeBrandingImageSignup).get_attribute("alt")
            if monotypeBrandingImageattribute is None:
                result = "None"

        elif page in "UserProfile":
            monotypeBrandingImageattribute = self.driver.find_element(
                *CommonRepository1.monotypeBrandingImageUserProfile).get_attribute("alt")
            if monotypeBrandingImageattribute is None:
                result = "None"

        elif page in "ResetLinkExpire":
            monotypeBrandingImageattribute = self.driver.find_element(
                *CommonRepository1.MonotypeBrandingImageResetLinkExpire).get_attribute("alt")
            if monotypeBrandingImageattribute is None:
                result = "None"


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


    def selectdefaultValuefromdropdown(self):
        # select = Select(self.driver.find_element_by_name('communitiesSelfRegPage:theForm:country'))
        select = Select(self.driver.find_element_by_name('country'))

        all_options = [o.get_attribute('value') for o in select.options]

        for x in all_options:
            select.first_selected_option
        return select.first_selected_option.text



    def verifyFooterHeading1(self, page):
        if page in  "SignIN":
            footerheading1 = self.driver.find_element(*CommonRepository1.footerHeadingSignIn).text
            if footerheading1 is None:
                result = "None"
        elif page in  "UserProfile":
            footerheading1 = self.driver.find_element(*CommonRepository1.footerHeadingUserProfile).text
            if footerheading1 is None:
                result = "None"
        elif page in "SignUP":
            footerheading1 = self.driver.find_element(*CommonRepository1.footerHeadingSignUp).text
            if footerheading1 is None:
                result = "None"

        elif page in "IDPPAssword":
            footerheading1 = self.driver.find_element(*CommonRepository1.footerHeadingIDPPassword).text
            if footerheading1 is None:
                result = "None"

        elif page in "ResetLinkExpire":
            footerheading1 = self.driver.find_element(*CommonRepository1.footerHeadingResetLinkExpirePage).text
            if footerheading1 is None:
                result = "None"


        return footerheading1


    def verifyFooterHeading2(self):
        footerHeading2 = self.driver.find_element(*CommonRepository1.trademarkFooterHeading).text
        if footerHeading2 is None:
            result = "None"
        return footerHeading2

    # def clicktrademarkFooterHeading(self):
    #     return self.driver.find_element(*CommonRepository.trademarkFooterHeading).click()
    #
    def clicktrademarkFooterHeading(self):
        trademarkFooterHeading =  self.driver.find_element(*CommonRepository1.trademarkFooterHeading)
        return self.driver.execute_script("arguments[0].click();", trademarkFooterHeading)

    def verifyFooterHeading3(self):
        return self.driver.find_element(*CommonRepository1.tearmsosuseFooter).text


    def clicktermsOfUseFooterHeading(self):
        return self.driver.find_element(*CommonRepository1.tearmsosuseFooter).click()


    def verifyFooterHeading4(self):
        footerHeading4 = self.driver.find_element(*CommonRepository1.termsandConditionFooter).text
        if footerHeading4 is None:
            result = "None"
        return footerHeading4

    def clicktermsAndConditionFooterHeading(self):
        return self.driver.find_element(*CommonRepository1.termsandConditionFooter).click()


    def verifyFooterHeading5(self):
        footerHeading5 = self.driver.find_element(*CommonRepository1.privacyPolicyFooter).text
        if footerHeading5 is None:
            result = "None"
        return footerHeading5

    def clickPrivacyPolicyFooterHeading(self):
        return self.driver.find_element(*CommonRepository1.privacyPolicyFooter).click()


    def verifyFooterHeading6(self):
        footerHeading6 = self.driver.find_element(*CommonRepository1.contactFooter).text
        if footerHeading6 is None:
            result = "None"
        log = self.getLogging()
        log.info(footerHeading6)
        return footerHeading6

    def clickContactFooterHeading(self):
        return self.driver.find_element(*CommonRepository1.contactFooter).click()

    def getPasspolicy1(self):
        return self.driver.find_element(*CommonRepository1.passwordPolicyValidation1).text


    def getPassPolicy1Color(self):
        cssColor = self.driver.find_element(*CommonRepository1.passwordPolicyValidation1).value_of_css_property("color")

        log = self.getLogging()
        log.info(cssColor)
        return cssColor


    def closeAcceptCookie(self):
        return self.driver.find_element(*CommonRepository1.closeAcceptCookieButton).click()

    def getinvalidUserPageHeadingText(self):
        return self.driver.find_element(*CommonRepository1.invalidUser404).text

    def getAlreadyAccountText(self):
        return  self.driver.find_element(*CommonRepository1.alreadyAccounterrorMessage).text


    def clickAuth0Accept(self):
        return self.driver.find_element(*CommonRepository1.auth0AcceptButton).click()

    def getSomethingWentWrongText(self):
        return self.driver.find_element(*CommonRepository1.somethingWentWrongErrorMessage).text

    def clickLoginLink(self):
        return self.driver.find_element(*CommonRepository1.loginLink).click()

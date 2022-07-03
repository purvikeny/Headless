import os
import time

from selenium.webdriver.common.by import By

from Auth0api.Auth0_Api_Methods import Auth0Lib
from PageObject.CommonPOM import CommonRepository1
from PageObject.CommonRepository import CommonRepository
from PageObject.LoginPage import LoginPage
from PageObject.lockUserPage import LockUserPage
from utilities.BaseClass import BaseClass
from utilities.ExcelUtilClass import ExcelUtil
from utilities.HelperClass import Helper
#from utilities.readEmail import Email


class CommonFunctionalityMethods(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    def launchURL(self):
        tenet = 'test'
        applicationName = 'Monotype Last_Queries'
        log = self.getLogging()
        ap = Auth0Lib(self.driver)
        helper = Helper()
        token = ap.get_AccessToken(tenet)
        clientId = ap.getClientID(token, tenet, applicationName)

        clientId = str(helper.getDataFromAuthIni("AUTH0", "ClientIdMTF"))

        # self.driver.get("https://secure-" + tenet + ".monotype.com/authorize?client_id=" + clientId + "&"
        # "scope=openid%20profile%20email&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A4000%2Fapi%2Fauth%2Fcallback"
        # "&nonce=USrwQ2YtH7phEPc2e-VOoEJfsTDcNsgcAFJIoY_Bdt0&state=eyJyZXR1cm5UbyI6Ii9wcm9maWxlIn0"
        # "&code_challenge=-NGtDWDk2nXDayRZ5KJQLOYZmJ_V48Yf-JVj5s1Ydsk&code_challenge_method=S256")

        self.driver.get("https://secure-" + tenet + ".monotype.com/authorize?response_type=code"
        "&client_id=" + clientId + "&return_to=https://accounts-" + tenet + ".monotype.com/api/auth/callback&scope=SCOPE&state=STATE")

        log.info("https://secure-" + tenet + ".monotype.com/authorize?response_type=code"
        "&client_id=" + clientId + "&return_to=https://accounts-" + tenet + ".monotype.com/api/auth/callback&scope=SCOPE&state=STATE")


    def launchURL1(self, tenet, applicationName):
        ap = Auth0Lib(self.driver)
        token = ap.get_AccessToken(tenet)
        log = self.getLogging()
        clientId = ap.getClientID(token, tenet, applicationName)

        log.info("https://secure-" + tenet + ".monotype.com/authorize?response_type=code"
        "&client_id=" + clientId + "&return_to=https://accounts-" + tenet + ".monotype.com/api/auth/callback&scope=SCOPE&state=STATE")

        self.driver.get("https://secure-" + tenet + ".monotype.com/authorize?response_type=code"
        "&client_id=" + clientId + "&return_to=https://accounts-" + tenet + ".monotype.com/api/auth/callback&scope=SCOPE&state=STATE")

    def launchApplication(self, tenet, env):

        helper = Helper()
        log = self.getLogging()
        clientId = helper.getDataFromAuthIni(env, 'ClientId')
        # log.info(clientId)

        # url = "https://secure-" + tenet + ".monotype.com/authorize?response_type=code&client_id=" + clientId + "&state=STATE&redirect_uri=http://myapp-local.monotype.com:3000/api/handlelogin?final_uri=https://www.monotypefonts-beta.com/pages/plans&audience=https://monotypeidp-" + tenet + ".us.auth0.com/api/v2/&scope=openid%20profile%20email&ui_locales=en"
        url = "https://secure-" + tenet + ".monotype.com/authorize?response_type=code&client_id="+clientId+"&state=STATE&redirect_uri=https://secure-test.myfonts.com/api/handlelogin?final_url=abc&audience=https://monotypeidp-test.us.auth0.com/api/v2/&scope=openid%20profile%20email"

        self.driver.get(url)
        self.getLogging().info(url)

    def launchApplicationSignup(self, tenet, env):

        helper = Helper()
        log = self.getLogging()
        clientId = helper.getDataFromAuthIni(env, 'ClientId')
        log.info(clientId)

        # url = "https://secure-" + tenet + ".monotype.com/authorize?response_type=code&client_id=" + clientId + "&state=STATE&redirect_uri=http://myapp-local.monotype.com:3000/api/handlelogin?final_uri=https://www.monotypefonts-beta.com/pages/plans&audience=https://monotypeidp-" + tenet + ".us.auth0.com/api/v2/&scope=openid%20profile%20email&ui_locales=en"
        url = "https://secure-" + tenet + ".monotype.com/authorize?response_type=code&client_id="+clientId+"&state=STATE&redirect_uri=https://secure-test.myfonts.com/api/handlelogin?final_url=abc&audience=https://monotypeidp-test.us.auth0.com/api/v2/&scope=openid%20profile%20email&screen_hint=signup"
        self.driver.get(url)
        self.getLogging().info(url)

    # TvaQVAYJdP6tUMVdoHXdOa3yn5TTSBFw

    def launchSignupURL(self, tenet, applicationName):
        log = self.getLogging()
        ap = Auth0Lib(self.driver)
        token = ap.get_AccessToken(tenet)
        clientId = ap.getClientID(token, tenet, applicationName)

        # URL  = "https://secure-"+tenet+".monotype.com/authorize?client_id="+clientId+"&scope=openid%20profile%20email&response_type=code&redirect_uri=http%3A%2F%2Flocalhost%3A4000%2Fapi%2Fauth%2Fcallback&nonce=USrwQ2YtH7phEPc2e-VOoEJfsTDcNsgcAFJIoY_Bdt0&state=eyJyZXR1cm5UbyI6Ii9wcm9maWxlIn0&code_challenge=-NGtDWDk2nXDayRZ5KJQLOYZmJ_V48Yf-JVj5s1Ydsk&code_challenge_method=S256&screen_hint=signup"
        # log.info(URL)
        URL = "https://secure-" + tenet + ".monotype.com/authorize?response_type=code&client_id=" + clientId + "&return_to=https://accounts-" + tenet + ".monotype.com/api/auth/callback&scope=SCOPE&state=STATE&screen_hint=signup"

        self.driver.get(URL)


    def verifyFooter(self,page):

        commonrepository = CommonRepository(self.driver)
        verifyFooterHeading1 = commonrepository.verifyFooterHeading1(page)

        self.assertForValidation(verifyFooterHeading1, "©2022 Monotype Imaging Inc.",
                                     "2022 Monotype Imaging Inc footer doesn't match with the expected")
        verifyFooterHeading2 = str(commonrepository.verifyFooterHeading2())
        self.assertForValidation(verifyFooterHeading2, "Terms of Use",
                                     "Terms of use footer is not matching with the expected")
        verifyFooterHeading3 = str(commonrepository.verifyFooterHeading3())
        self.assertForValidation(verifyFooterHeading3, "Privacy Policy.", "Privacy policy footer is not matching")
        verifyFooterHeading4 = str(commonrepository.verifyFooterHeading6())
        self.assertForValidation(verifyFooterHeading4, "Contact", " contact footer does't match")


    def verifySideLinks(self):
        log = self.getLogging()

        loginPage = LoginPage(self.driver)
        commonrepository = CommonRepository(self.driver)
        demoMobileText = commonrepository.getdemoMobileText()
        self.assertForValidation(demoMobileText, "Demo - Mobile", "demo mobile text is not present on the screen")

        demoTabletText = commonrepository.getdemoTabletText()
        self.assertForValidation(demoTabletText, "Demo - Tablet", "demo tablet text is not present on the screen")

        demoSmallerDesktop = commonrepository.getdemoSmallerDesktop()
        self.assertForValidation(demoSmallerDesktop, "Demo - Smaller Desktop", "demo smaller desktop text is not present on the screen")

    def verifyLoggedINOnMonotyprFont(self):
        log = self.getLogging()
        fullstring = str(self.driver.current_url)

        substring = "4000"

        if substring in fullstring:
            log.info("Found!")
            self.assertForValidation(substring, "4000", "user is not able to logged in successfully")
        else:
            log.info("user not able to logged in  Found!")

    def verifyLoggedINOnmyfont(self):
        log = self.getLogging()
        fullstring = str(self.driver.current_url)

        substring = "sapient"

        if substring in fullstring:
            log.info("Found!")
            self.assertForValidation(substring, "sapient", "user is not able to logged in successfully")
        else:
            log.info("user not able to logged in  Found!")


    def verifyRedirectOnmonotypeFontPage(self, tenet):
        log = self.getLogging()
        fullstring = str(self.driver.current_url)

        substring = "https://enterprise-"+tenet+".monotype.com/"

        if substring in fullstring:
            log.info("Found!")
            self.assertForValidation(substring, substring, "user is not able to logged in successfully")
        else:
            log.info("user not able to logged in  Found!")


    def passPolicyValidation1(self, Value):

        com = CommonRepository1(self.driver)

        log = self.getLogging()
        time.sleep(5)

        log.info("value parameter is "+Value)

        specialCharaterPassolicy = com.getspecialCharacterPasswordPolicy()
        log.info(" Special character pass validation policy value is "+str(specialCharaterPassolicy))
        self.assertForValidation(str(specialCharaterPassolicy), Value,
                                 "special character pasword policy working fine")
        lowerCasePassPolicy = com.getLowerCaserPasswordPolicy()
        log.info(" Lower character pass validation policy value is " + str(lowerCasePassPolicy))
        self.assertForValidation(str(lowerCasePassPolicy), Value,
                                 "lower case character pasword policy working fine")
        EightCharacterPassPolicy = com.getEightCharacterrPasswordPolicy()
        log.info(" 8 charcter pass validation policy value is " + str(EightCharacterPassPolicy))
        self.assertForValidation(str(EightCharacterPassPolicy), Value,
                                 "8 character pasword policy working fine")
        upperCasePassPolicy = com.getUpperCasePasswordPolicy()
        log.info(" upper character pass validation policy value is " + str(upperCasePassPolicy))
        self.assertForValidation(str(upperCasePassPolicy), Value,
                                 "upper case pasword policy working fine")
        numberPassPolicy = com.getnumberPasswordPolicy()
        log.info(" Number pass validation policy value is " + str(numberPassPolicy))

        self.assertForValidation(str(numberPassPolicy), Value,
                                 "Number pass validation policy working fine")


    def unlockAllUserFirst(self):
        email = Email()
        log = self.getLogging()
        lockUser = LockUserPage(self.driver)
        lockUserURL = email.getLockUserEmail(0)
        log.info(lockUserURL)

        self.openNewTab(self.driver, lockUserURL)

        mainWindow = self.driver.current_window_handle
        childwindow = self.driver.window_handles[1]
        if mainWindow not in childwindow:
            self.driver.switch_to.window(self.driver.window_handles[1])

            log.info(str(self.driver.current_url) + " Link is opening in new tab")
            time.sleep(2)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

        log.info(self.driver.current_url)


    def verifyURL(self, substring):
        log = self.getLogging()
        fullstring = str(self.driver.current_url)

        # substring = "4000"

        if substring in fullstring:
            log.info("Found!")
            # self.assertForValidation(substring, "4000", "user is not able to logged in successfully")
        else:
            log.info("user not able to logged in  Found!")


    def launchMFURL(self, key):

        log = self.getLogging()
        ap = Auth0Lib(self.driver)
        helper = Helper()
        URL = str(helper.getDataFromConfig("AUTH0_Test_MFCOM","MFCOMURL","auth0-api-config.ini"))
        self.driver.get(URL)











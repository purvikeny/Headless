import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
import time
from utilities.BaseClass import BaseClass
from PageObject.HomePage import HomePage


class TestSignupFlow(BaseClass):
    tenet = config.tenet
    applicationName = config.applicationNameMyfont
    authenv = config.environment
    StorePageTitle = (By.XPATH, "//*[text()='Opening soon']")
    EnterUsingStorePasswordBtn = (By.XPATH, "//div[normalize-space()='Enter using password']")
    StorePswrdPageTitle = (By.XPATH,"//*[normalize-space()='Enter store using password:']")
    StorePswrdTextBox = (By.XPATH, "//*[@id='Password']")
    EnterBtn = (By.XPATH, "//Button[contains(text(),'Enter')]")
    HomePageTitle = (By.XPATH, "//div[@class='highlightsection']//h1")
    HomePageSubTitle = (By.XPATH, "//div[@class='highlightsection']//h2")
    #SearchButton = (By.XPATH, "//*[@id='searchButton']")
    SearchButton = (By.XPATH, "//button[@class='aa-SubmitButton search-btn']")
    CookieAcceptButton = (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    SearchBar = (By.XPATH, "//input[@id='autocomplete-0-input']")
    DropDownResultsLocator = "//a[@class='search_item']/div[@class='search__left']"
    TagRightArrow = (By.XPATH, "(//div[@id='next_arrow'])[1]")
    Password = "olyiel"
    word_search = "H"

    # @pytest.mark.skip
    # @pytest.mark.gui
    def test_Signup_Flow(self):
        #Navigate to the URL
         #self.visitUrl("https://qa2-myfonts.myshopify.com/pages/globalsearch")
         self.visitUrl("https://preprod-myfonts.myshopify.com/password")

         homePage = HomePage()
         homePage.EnterStorePassword()
         #Enter using password
         if self.driver.find_element(*TestSignupFlow.StorePageTitle).is_displayed():
             self.driver.find_element(*TestSignupFlow.EnterUsingStorePasswordBtn).click()
             WebDriverWait(self.driver, 10).until(
                EC.visibility_of((self.driver.find_element(*TestSignupFlow.StorePswrdPageTitle))))
             print("Entering Password")
             self.driver.find_element(*TestSignupFlow.StorePswrdTextBox).send_keys(*TestSignupFlow.Password)
             self.driver.find_element(*TestSignupFlow.EnterBtn).click()
             self.visitUrl("https://qa2-myfonts.myshopify.com/pages/globalsearch")
             print(self.driver.title)
         elif self.driver.title is "Global Search Experience":
             print("HomePage is displaying store Password skipped")
         #elif self.driver.find_element(*TestSignupFlow.HomePageTitle).is_displayed():
             #print("HomePage is displaying store Password skipped")


         #Validating HomePage
         #WebDriverWait(self.driver, 20).until(
              #EC.visibility_of((self.driver.find_element(*TestSignupFlow.SearchButton))))

         WebDriverWait(self.driver, 20).until(
            EC.visibility_of((self.driver.find_element(*TestSignupFlow.SearchBar))))
         print("SearchBar Validated")
         print("HomePage Validated")

         WebDriverWait(self.driver, 20).until(
            EC.visibility_of((self.driver.find_element(*TestSignupFlow.SearchButton))))
         print("SearchButton Validated")


         #Entering text in Search Bar
         self.driver.find_element(*TestSignupFlow.SearchBar).send_keys(*TestSignupFlow.word_search)
         time.sleep(10)
         print("searching some text")

         #Checking the data displayed in dropdown
         expectedList = ["Hot Potato","Healing Sunday","Hekson","Heart Grow"
             ,"Handstory","Hockeynight Sans Brush","Hollows","Humber"]

         elem = []
         #elem = self.driver.find_elements_by_xpath(*TestSignupFlow.DropDownResultsLocator)
         elem = self.driver.find_elements_by_xpath("//a[@class='search_item']/div[@class='search__left']")
         i = 0
         for ele in elem:
             assert ele.text == expectedList[i]
             print("Element at position " ,i, " validated")
             i = i+1
         print("validation of drop-down completed")

         #Getting the Tags_Section
         expectedTagList = ["Display", "Authentic", "Cool", "Trend", "Modern", "Sans Serif","Lettering","Logotype"]
         tagEle = self.driver.find_elements_by_xpath("//a[@class ='tags__item']")
         print(len(tagEle))
         j = 0
         for tag in tagEle:
             if j>4:
                self.driver.find_element(*TestSignupFlow.TagRightArrow).click()
                time.sleep(10)
             assert tag.text == expectedTagList[j]
             print(tag.text)
             j = j + 1
         print("tag test")



         # print("validation of tags completed")

         #Clicking on AcceptCookies button
         # WebDriverWait(self.driver, 12).until(
         #     EC.visibility_of((self.driver.find_element(*TestSignupFlow.CookieAcceptButton))))
         # self.driver.find_element(*TestSignupFlow.CookieAcceptButton).click()

         # #Verifying Myfonts Logo
         # print("Validating My Last_Queries Logo")
         # WebDriverWait(self.driver, 12).until(
         #     EC.visibility_of((self.driver.find_element(*TestSignupFlow.myFontsLogo))))




    #     log = self.getLogging()
    #     helper = Helper()
    #     excelUtil = ExcelUtil(self.driver)
    #     commonFunctionalitymethods = CommonFunctionalityMethods(self.driver)
    #     signupPage = SignupPage(self.driver)
    #     passwordPage = PasswordPage(self.driver)
    #     ap = Auth0Lib(self.driver)
    #     emailVerification = EmailVerification(self.driver)
    #     email = Email()
    #     randomstring = helper.getRandomString(5)
    #
    #     emailId = "monotype.serviceAutomation+" + randomstring+ "@gmail.com"
    #     log.info(emailId)
    #     commonFunctionalitymethods.launchSignupURL(TestSignupFlow.tenet, TestSignupFlow.applicationName)
    #     commonFunctionalitymethods.launchApplication(TestSignupFlow.tenet, TestSignupFlow.authenv)
    #
    #     self.verifyElementPresent(signupPage.signupPageXpath)
    #
    #
    #     val = ap.get_User_APi(TestSignupFlow.tenet, ap.get_AccessToken(TestSignupFlow.tenet), emailId)
    #
    # @pytest.mark.skip
    # def test_delete(self):
    #     ap = Auth0Lib(self.driver)
    #     log = self.getLogging()
    #     userId = "auth0|60f87376d2d425006a820d6a"
    #     tenet="pp"
    #     val = ap.get_delete_user(tenet, ap.get_AccessToken(tenet), userId)
    #     log.info(str(val.status_code))
    #     self.assertForValidation(str(val.status_code), "204",
    #                              "user is not deleted successfully")
    #
    # @pytest.mark.skip
    # def test_get_user_info(self):
    #     ap = Auth0Lib(self.driver)
    #     log = self.getLogging()
    #     userId = "auth0|60f87376d2d425006a820d6a"
    #     tenet = "test"
    #     emailId = "testOktaACC@monotype.com"
    #     userResp = ap.get_User_APi(tenet, ap.get_AccessToken(tenet), emailId)
    #
    #     log.info(userResp.json())



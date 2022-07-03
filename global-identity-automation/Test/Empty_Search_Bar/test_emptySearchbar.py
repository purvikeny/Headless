import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
import time
from utilities.BaseClass import BaseClass
from PageObject.InitialLoginPage import InitialLoginPage
from PageObject.EmptySearchPage import EmptySearchPage
from resources.Utilities.GetAlgoliaData import GetAlgoliaData




class TestEmptySearch(BaseClass):
    tenet = config.tenet
    applicationName = config.applicationNameMyfont
    authenv = config.environment
    password = "olyiel"
    word_search = "Ther"
    SearchBar = (By.XPATH, "//input[@id='autocomplete-0-input']")

    # @pytest.mark.skip
    # @pytest.mark.gui
    def test_validate_results(self):
         initialloginpage = InitialLoginPage(self.driver)
         initialloginpage.NavigateToGlobalSearch()
         initialloginpage.LoginUsingPassword("olyiel")

         #Validating elements on homepage
         emptySearchPage = EmptySearchPage(self.driver)
         emptySearchPage.validateGlobalSearchPage()
         emptySearchPage.validateSearchButton()

         #Entering text in Search Bar
         #emptySearchPage.enterTextInSearchbox(*TestEmptySearch.word_search)
         emptySearchPage.enterTextInSearchbox("helv")

         #Checking the data displayed in dropdown
         algoliapage = GetAlgoliaData()
         expectedfonts = algoliapage.getfonts("helv")
         emptySearchPage.validateDropDownFonts(expectedfonts)


         #Getting the Tags_Section
         expectedTagList = algoliapage.gettags("helv")
         convert_to_str = ""
         # traverse in the string
         for i in expectedTagList:
             convert_to_str += i
         expectedTagList = convert_to_str.split("', '")
         emptySearchPage.validateDropDownTags(expectedTagList)



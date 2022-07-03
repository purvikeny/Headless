from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass
import time

class EmptySearchPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    SearchBar = (By.XPATH, "//input[@id='autocomplete-0-input']")
    DropDownResultsLocator = "//a[@class='search_item']/div[@class='search__left']"
    TagRightArrow = (By.XPATH, "(//div[@id='next_arrow'])[1]")
    SearchButton = (By.XPATH, "//button[@class='aa-SubmitButton search-btn']")
    TagRightArrow = (By.XPATH, "(//div[@id='next_arrow'])[1]")


    def validateGlobalSearchPage(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of((self.driver.find_element(*EmptySearchPage.SearchBar))))
        print("SearchBar Validated")
        print("HomePage Validated")

    def validateSearchButton(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of((self.driver.find_element(*EmptySearchPage.SearchButton))))
        print("SearchButton Validated")

    def enterTextInSearchbox(self,word):
        self.driver.find_element(*EmptySearchPage.SearchBar).send_keys(word)
        time.sleep(10)
        print("searching some text")

    def validateDropDownFonts(self,expectedFonts):
        elem = []
        # elem = self.driver.find_elements_by_xpath(*TestSignupFlow.DropDownResultsLocator)
        elem = self.driver.find_elements_by_xpath("//a[@class='search_item']/div[@class='search__left']")
        i = 0
        for ele in elem:
            assert ele.text == expectedFonts[i]
            print(ele.text)
            i = i + 1
        print("validation of drop-down completed")

    def validateDropDownTags(self,expectedTags):
        tagEle = self.driver.find_elements_by_xpath("//a[@class ='tags__item']")
        print(len(tagEle))
        j = 0
        for tag in tagEle:
            #if j > 4:
                #self.driver.find_element(*EmptySearchPage.TagRightArrow).click()
                #time.sleep(10)
            print(tag.text)
            tagnew = expectedTags[j].replace("\"","'")
            print((tag.text).lower(),"compare",tagnew)
            #assert (tag.text).lower() == tagnew
            j = j + 1
        print("tag test")






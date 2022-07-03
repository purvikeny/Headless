from telnetlib import EC

import requests
from numpy.ma import var
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class HomePage(BaseClass):

    StorePageTitle = (By.XPATH,"//*[text()='Opening soon']")
    EnterUsingStorePasswordBtn = (By.XPATH,"//div[normalize-space()='Enter using password']")
    StorePswrdPageTitle = "//*[normalize-space()='Enter store using password:']"
    StorePswrdTextBox = (By.XPATH,"//*[@id='Password']")
    EnterBtn = (By.XPATH,"//Button[contains(text(),'Enter')]")
    HomePageTitle = (By.XPATH,"//div[@class='highlightsection']//h1")
    HomePageSubTitle = (By.XPATH,"//div[@class='highlightsection']//h2")
    SearchButton = (By.CSS_SELECTOR,"button.searchBarWidget__searchButton")
    CookieAcceptButton = (By.XPATH,"//button[@id='onetrust-accept-btn-handler']")



    def EnterStorePassword(self):
        if self.driver.find_element(*HomePage.StorePageTitle).is_displayed():
            self.driver.find_element(*HomePage.EnterUsingStorePasswordBtn).click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of((self.driver.find_element(*HomePage.StorePswrdPageTitle))))
            print("Entering Password")
            self.driver.find_element(*HomePage.StorePswrdTextBox).send_keys("whaima")
            self.driver.find_element(*HomePage.EnterBtn).click()
        elif self.driver.find_element(*HomePage.HomePageTitle).is_displayed():
            print("HomePage is displaying store Password skipped")

    def validateHomePage(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of((self.driver.find_element(*HomePage.SearchButton))))
        print("HomePage Validated")

    def tapOnAcceptCookies(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of((self.driver.find_element(*HomePage.CookieAcceptButton))))
        self.find_element(*HomePage.CookieAcceptButton).click()






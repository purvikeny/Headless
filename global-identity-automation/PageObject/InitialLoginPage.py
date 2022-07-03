from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class InitialLoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver


    GlobalSearchURL = "https://qa2-myfonts.myshopify.com/pages/globalsearch"
    StorePageTitle = (By.XPATH, "//*[text()='Opening soon']")
    EnterUsingStorePasswordBtn = (By.XPATH, "//div[normalize-space()='Enter using password']")
    StorePswrdPageTitle = (By.XPATH, "//*[normalize-space()='Enter store using password:']")
    StorePswrdTextBox = (By.XPATH, "//*[@id='Password']")
    EnterBtn = (By.XPATH, "//Button[contains(text(),'Enter')]")


    # Navigate to the URL
    def NavigateToGlobalSearch(self):
         #self.visitUrl(*InitialLoginPage.GlobalSearchURL)
         self.visitUrl("https://qa2-myfonts.myshopify.com/pages/globalsearch")

    # Enter using password
    def LoginUsingPassword(self,password):
        if self.driver.find_element(*InitialLoginPage.StorePageTitle).is_displayed():
            self.driver.find_element(*InitialLoginPage.EnterUsingStorePasswordBtn).click()
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of((self.driver.find_element(*InitialLoginPage.StorePswrdPageTitle))))
            print("Entering Password")
            self.driver.find_element(*InitialLoginPage.StorePswrdTextBox).send_keys(password)
            self.driver.find_element(*InitialLoginPage.EnterBtn).click()
            self.NavigateToGlobalSearch()
            print(self.driver.title)
        elif self.driver.title is "Global Search Experience":
            print("HomePage is displaying store Password skipped")






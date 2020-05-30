from selenium.webdriver.common.by import By
from selenium import webdriver

class ConfirmPage:
    def __init__(self,driver):
        self.driver = driver

    #driver.find_element_by_xpath("//strong").text
    successmsg = (By.XPATH,"//strong")

    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.successmsg)


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

from PageObjects.Checkout import Checkout


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    shop=(By.CSS_SELECTOR,"a[href*=shop]")
    name=(By.NAME,"name")
    email=(By.NAME,"email")
    password=(By.ID,"exampleInputPassword1")
    checkbox=(By.ID,"exampleCheck1")
    gender=(By.ID,"exampleFormControlSelect1")
    radio=(By.ID,"inlineRadio2")
    bday=(By.XPATH,"//input[@name='bday']")
    submit=(By.CSS_SELECTOR,".btn-success")
    alert=(By.CSS_SELECTOR,".alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = Checkout(self.driver)
        return  checkOutPage
    #driver.find_element_by_css_selector("a[href*=shop]")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def selectCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def Gender(self):
        return  self.driver.find_element(*HomePage.gender)

    def selectRadio(self):
        return self.driver.find_element(*HomePage.radio)

    def clickCalendar(self):
        return  self.driver.find_element(*HomePage.bday)

    def clickSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlert(self):
        return self.driver.find_element(*HomePage.alert)


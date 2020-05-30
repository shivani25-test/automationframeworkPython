

from selenium.webdriver.common.by import By
from selenium import webdriver

from PageObjects.ConfirmPage import ConfirmPage


class Checkout:
    def __init__(self,driver):
        self.driver = driver

    selectprod=(By.XPATH,"//app-card-list[@class='row']/app-card[4]/div/div[2]/button")

    #driver.find_element_by_css_selector(".btn-primary").click()
    checkoutbutton=(By.CSS_SELECTOR,".btn-primary")
    #driver.find_element_by_xpath("//h4").text
    checkprodname = (By.XPATH,"//h4")
    #driver.find_element_by_xpath("//h3/strong").text
    totalamt = (By.XPATH,"//h3/strong")
    #driver.find_element_by_css_selector(".btn-success").click()
    succesbutton=(By.CSS_SELECTOR,".btn-success")
    #driver.find_element_by_css_selector("#country").click()
    clickcountry=(By.CSS_SELECTOR,"#country")
    #driver.find_element_by_xpath("//div[@class='suggestions']/ul[1]/li/a").click()
    selectcountry=(By.XPATH,"//div[@class='suggestions']/ul[1]/li/a")
    #driver.find_element_by_link_text("term & Conditions").click()
    termscondition=(By.LINK_TEXT,"term & Conditions")
    #driver.find_element_by_xpath("//button[@class='btn btn-info']").click()
    closebutton=(By.XPATH,"//button[@class='btn btn-info']")
    #driver.find_element_by_xpath("//input[@value='Purchase']").click()
    purchasebutton=(By.XPATH,"//input[@value='Purchase']")

    def selectProduct(self):
        return self.driver.find_element(*Checkout.selectprod)

    def checkoutButton(self):
        return self.driver.find_element(*Checkout.checkoutbutton)

    def checkProdName(self):
        return self.driver.find_element(*Checkout.checkprodname)

    def totalAmt(self):
        return  self.driver.find_element(*Checkout.totalamt)

    def successButton(self):
        return self.driver.find_element(*Checkout.succesbutton)

    def clickCountry(self):
        return self.driver.find_element(*Checkout.clickcountry)

    def selectCountry(self):
        return self.driver.find_element(*Checkout.selectcountry)

    def termsConditions(self):
        return self.driver.find_element(*Checkout.termscondition)

    def closeButton(self):
        return self.driver.find_element(*Checkout.closebutton)

    def purchaseButton(self):
        self.driver.find_element(*Checkout.purchasebutton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
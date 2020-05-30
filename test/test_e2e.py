from PageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass

#import pytest
#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        self.driver.implicitly_wait(10)
        homepage = HomePage(self.driver)
        checkout = homepage.shopItems()

        #homepage.shopItems().click()
        checkout.selectProduct().click()
        checkout.checkoutButton().click()
        productName=checkout.checkProdName().text
        total_amt=checkout.totalAmt().text
        print(total_amt)
        #log.info("Total amount is " + total_amt)
        log.info("product name is "+productName)
        checkout.successButton().click()
        checkout.clickCountry().click()
        log.info("Sending country name as Ind")
        checkout.clickCountry().send_keys("Ind")
        checkout.selectCountry().click()
        checkout.termsConditions().click()
        checkout.closeButton().click()
        #checkout.purchaseButton().click()
        confirmpage = checkout.purchaseButton()
        succmsg = confirmpage.successMessage().text
        log.info("success msg is "+succmsg)
        assert "Success" in succmsg
        assert  "Blackberry" in productName
        finalAmt=total_amt[2:len(total_amt)]
        log.info("Final amount of "+productName+" is "+finalAmt)
        assert 0 < int(finalAmt)



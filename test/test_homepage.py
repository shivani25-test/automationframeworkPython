import pytest
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import HomePage
from TestDate.test_data_homepage import HomepageTestData
from utilities.BaseClass import BaseClass


class Test_homepage(BaseClass):
    @pytest.mark.smoke
    def test_homepage(self,getdata):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getdata["firstname"])
        log.info("First name is "+getdata["firstname"])
        homepage.getEmail().send_keys(getdata["email"])
        log.info("Email is " + getdata["email"])
        homepage.getPassword().send_keys(getdata["password"])
        homepage.selectCheckbox().click()
        self.selectByText(homepage.Gender(),getdata["gender"])
        log.info("Gender is " + getdata["gender"])
        homepage.selectRadio().click()
        homepage.clickCalendar().click()
        homepage.clickSubmit().click()
        assert "Success" in homepage.getAlert().text
        self.driver.refresh()
        print("msg")



    @pytest.fixture(params=HomepageTestData.getData("tc01"))
    def getdata(self,request):
        return request.param
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://offlintab.firefoxchina.cn/")
        driver.find_element_by_name("q").click()
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("12306")
        driver.find_element_by_id("searchform").submit()
        driver.find_element_by_link_text(u"12306铁道部火车票网上订票唯一官网 - 铁路客户服务中心").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_1 | ]]
        driver.find_element_by_id("fromStationText").click()
        driver.find_element_by_xpath("//div[3]/div/div/div/ul/li[3]/a").click()
        driver.find_element_by_id("toStationText").click()
        driver.find_element_by_xpath("//body").click()
        driver.find_element_by_id("train_date").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='今天'])[1]/following::div[26]").click()
        driver.find_element_by_id("search_one").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | win_ser_2 | ]]
        driver.find_element_by_link_text(u"预订").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

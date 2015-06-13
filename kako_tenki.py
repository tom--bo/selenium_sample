# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, time

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(30)
        self.base_url = "http://www.data.jma.go.jp/"
        self.verificationErrors = []
    
    def test_(self):
        t = 0.5
        driver = self.driver
        driver.get(self.base_url + "/gmd/risk/obsdl/index.php#")
        time.sleep(t)
        y = "1994"
        m = "-1"
        tmp = "0"
        driver.find_element_by_id("buttonDelAll").click()
        time.sleep(t)
        driver.find_element_by_xpath("(//*[@id=\"pr44\"])").click()
        time.sleep(t)
        driver.find_element_by_xpath("(//*[@id=\"stationMap\"]/div[9]/div)").click()
        time.sleep(t)
        driver.find_element_by_id("elementButton").click()
        driver.find_element_by_xpath("//*[@id='aggrgPeriod']/div/div[1]/div[1]/label/span").click()
        time.sleep(t)
        driver.find_element_by_id(u"気温").click()
        driver.find_element_by_id(u"降水量").click()
        driver.find_element_by_id(u"日照時間").click()
        driver.find_element_by_id(u"風向・風速").click()
        driver.find_element_by_id(u"全天日射量").click()
        driver.find_element_by_id(u"現地気圧").click()
        driver.find_element_by_id(u"相対湿度").click()
        driver.find_element_by_id(u"蒸気圧").click()
        time.sleep(t)
        driver.find_element_by_id(u"現地気圧").click()
        driver.find_element_by_id("periodButton").click()
        Select(driver.find_element_by_name("iniy")).select_by_visible_text(y)
        Select(driver.find_element_by_name("endy")).select_by_visible_text(y)
        time.sleep(t)
        Select(driver.find_element_by_name("inim")).select_by_visible_text("1")
        Select(driver.find_element_by_name("inid")).select_by_visible_text("1")
        time.sleep(t)
        Select(driver.find_element_by_name("endm")).select_by_visible_text("2")
        Select(driver.find_element_by_name("endd")).select_by_visible_text("1")
        time.sleep(t)
        driver.find_element_by_css_selector("#csvdl > img.rollover").click()
        time.sleep(t*10)
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

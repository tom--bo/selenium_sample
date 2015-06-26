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
        prefectures = [11, 19, 14, 31, 33, 32, 35, 34, 36, 54, 55, 56, 41, 42, 40, 45, 43, 44, 49, 46, 48, 50, 52, 51, 57, 60, 53, 64, 65, 61, 62, 63, 69, 66, 68, 67, 81, 72, 71, 73, 74, 82, 85, 84, 83, 86, 87, 88, 91, 99]
        part_of_pre = [1, 19, 9, 7, 37, 21, 31, 25, 26, 9, 11, 19, 21, 17, 11, 21, 1, 9, 7, 5, 37, 19, 49, 7, 1, 7, 27, 1, 21, 19, 7, 39, 5, 9, 9, 29, 19, 3, 5, 9, 9, 13, 9, 21, 13, 11, 29, 25, 15, 1]
        start_m_arr = [1,2,3,4,5,6,7,8,9,10,11,12]
        start_d_arr = [1,2,2,2,2,2,2,2,2,2,2,2]
        end_m_arr =   [2,3,4,5,6,7,8,9,10,11,12,12]
        end_d_arr =   [1,1,1,1,1,1,1,1,1,1,1,31]
        t = 0.5

        driver = self.driver
        for p in range(0,len(prefectures)):
            print(str(p)+"start")
            driver.get(self.base_url + "/gmd/risk/obsdl/index.php#")
            time.sleep(t)

            driver.find_element_by_id("buttonDelAll").click()
            time.sleep(t)
            driver.find_element_by_xpath("(//*[@id=\"pr" + str(prefectures[p]) + "\"])").click()
            time.sleep(t)
            driver.find_element_by_xpath("(//*[@id=\"stationMap\"]/div[" + str(part_of_pre[p]) + "]/div)").click()
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
            for y in range (1995, 2015):
                Select(driver.find_element_by_name("iniy")).select_by_visible_text(str(y))
                Select(driver.find_element_by_name("endy")).select_by_visible_text(str(y))
                time.sleep(t)
                for i in range(0,12):
                    Select(driver.find_element_by_name("inim")).select_by_visible_text(str(start_m_arr[i]))
                    Select(driver.find_element_by_name("inid")).select_by_visible_text(str(start_d_arr[i]))
                    Select(driver.find_element_by_name("endm")).select_by_visible_text(str(end_m_arr[i]))
                    Select(driver.find_element_by_name("endd")).select_by_visible_text(str(end_d_arr[i]))
                    time.sleep(t)
                    driver.find_element_by_css_selector("#csvdl > img.rollover").click()
                    time.sleep(t)
                time.sleep(t*4)

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

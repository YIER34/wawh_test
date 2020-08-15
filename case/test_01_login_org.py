#coding=utf-8
from time import sleep
from appium import webdriver
from appiumtools import find_element, assert_element_exist,connect

import unittest

class Test_login(unittest.TestCase):
    #driver = connect()
    
    def setUp(self):
        # 配置链接
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '6.0.1',  # 安卓系统的版本号：adb shell getprop ro.build.version.release
            'deviceName': 'OPPO R9s',  # 手机/模拟器的型号：adb shell getprop ro.product.model
            'appPackage': 'com.fs.wawh',
            'appActivity': '.activities.SplashActivity',
            'unicodeKeyboard': True,  # 为了支持中文
            'resetKeyboard': True,  # 设置成appium自带的键盘
            "noReset": True}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    
    def test_01_login_org(self):
        """
        组织账户登录
        """
        mine = ("text", "我的")
        login_regist_bot = ("text", "登录/注册")
        login_tpye_password = ("id","com.fs.wawh:id/tv_login_type")
        username = ("id","com.fs.wawh:id/user_login_id")
        password = ("id","com.fs.wawh:id/user_login_password")
        login_bot = ("id","com.fs.wawh:id/btn_login")
        search_key = ("text", "惠州市社会组织总会")
        sleep(3)
        find_element(self.driver, mine).click()
        find_element(self.driver, login_regist_bot).click()
        find_element(self.driver, login_tpye_password).click()
        find_element(self.driver, username).clear()
        find_element(self.driver, username).send_keys("13700001010")
        find_element(self.driver, password).send_keys("qwe123456")
        find_element(self.driver, login_bot).click()

        assert assert_element_exist(self.driver, search_key) == True
        sleep(3)
        self.driver.close_app()
        print("登录成功")
        
    '''
    def test_login_com(self):
        """
        企业账户登录
        """
        mine = ("text", "我的")
        login_regist_bot = ("text", "登录/注册")
        login_tpye_password = ("id","com.fs.wawh:id/tv_login_type")
        username = ("id","com.fs.wawh:id/user_login_id")
        password = ("id","com.fs.wawh:id/user_login_password")
        login_bot = ("id","com.fs.wawh:id/btn_login")
        search_key = ("text", "久生企业管理集团有限公司")

        find_element(self.driver, mine).click()
        find_element(self.driver, login_regist_bot).click()
        find_element(self.driver, login_tpye_password).click()
        find_element(self.driver, username).clear()
        find_element(self.driver, username).send_keys("13700001058")
        find_element(self.driver, password).send_keys("qwe123456")
        find_element(self.driver, login_bot).click()
        

        assert assert_element_exist(driver, search_key) == True
        sleep(3)
        driver.close_app()
        print("登录成功")
    '''
if __name__=="__main__":
    unittest.main()
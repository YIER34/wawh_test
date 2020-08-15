#coding=utf-8
from time import sleep
from appium import webdriver
from appiumtools import find_element, assert_element_exist,connect
from public import swipeUp,swipeDown
import unittest

class Test_Logout(unittest.TestCase):
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
    def test_logout(self):
        """
        退出登录
        """
        mine = ("text", "我的")
        setting = ("text", "设置")
        logout = ("id","com.fs.wawh:id/btn_login")
        logout_sure = ("id","com.fs.wawh:id/btn_right")

       
        find_element(self.driver, mine).click()
        # 滑动页面至设置
        sleep(1)
        swipeUp(self.driver,500,1)
        find_element(self.driver, setting).click()
        find_element(self.driver, logout).click()
        find_element(self.driver, logout_sure).click()

        # 滑动页面至登录/注册
        sleep(2)
        swipeDown(self.driver,500,1)

        # 判断是否已退出登录
        login_regist_bot = ("text", "登录/注册")
        assert assert_element_exist(self.driver, login_regist_bot) == True
        sleep(3)
        #self.driver.close_app()
        print("退出登录成功")
        self.driver.quit()
if __name__=="__main__":
    unittest.main()

  
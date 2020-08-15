
#coding=utf-8
from time import sleep
from appium import webdriver
from appiumtools import find_element, assert_element_exist,connect
from public import swipeUp,swipeDown
import unittest
@unittest.skip
class Test_Join_Action(unittest.TestCase):
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
    def test_join_action(self):
        """
        企业账号报名活动
        """
        index = ("text", "首页")
        my_org = ("id","com.fs.wawh:id/logo")
        action = ("id","com.fs.wawh:id/action_item_logo")
        apply = ("id", "com.fs.wawh:id/tv_release")
        name = ("id","com.fs.wawh:id/et_name")
        phone = ("id","com.fs.wawh:id/et_phone")
        apply_join = ("id","com.fs.wawh:id/tv_join")



        find_element(self.driver, index).click()
        find_element(self.driver, my_org).click()
        find_element(self.driver, action).click()
        find_element(self.driver, apply).click()
        find_element(self.driver, name).send_keys("林生")
        find_element(self.driver, phone).send_keys("13427906733")
        find_element(self.driver, apply_join).click()


        # 判断是否成功报名活动
        succeed = ("text", "已报名活动")
        assert assert_element_exist(self.driver, succeed) == True
        sleep(3)
        self.driver.close_app()
        print("已报名活动")

if __name__=="__main__":
    unittest.main()

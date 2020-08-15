#coding=utf-8
from time import sleep
from appium import webdriver
from appiumtools import find_element, assert_element_exist,connect
from public import swipeUp,swipeDown
import unittest
@unittest.skip
class Test_Add_Org(unittest.TestCase):
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
    def test_add_org(self):
        """
        企业账号加入组织
        """
        index = ("text", "首页")
        go_see = ("id", "com.fs.wawh:id/go_see")
        menu = ("id","com.fs.wawh:id/actionSure")
        join_org = ("id","com.fs.wawh:id/org_join")
        apply_join = ("id","com.fs.wawh:id/submit")

        find_element(self.driver, index).click()
        find_element(self.driver, go_see).click()
        find_element(self.driver, menu).click()
        find_element(self.driver, join_org).click()
        find_element(self.driver, apply_join).click()

        # 判断是否提交申请成功
        succeed = ("text", "提交成功")
        assert assert_element_exist(self.driver, succeed) == True

        sleep(3)
        self.driver.close_app()
        print("申请加入组织提交成功")

if __name__=="__main__":
    unittest.main()



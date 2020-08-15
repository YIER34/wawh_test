#coding=utf-8
from time import sleep
from appium import webdriver
from appiumtools import find_element, assert_element_exist,connect
from appium.webdriver.common.touch_action import TouchAction
import unittest
import datetime
from public import swipeUp,swipeDown


class Test_Add_Address(unittest.TestCase):
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
    def test_add_address(self):
        """
        新增地址
        """
        mine = ("text", "我的")
        address_manage = ("text", "地址管理")
        add_address = ("id","com.fs.wawh:id/my_address_add_button")
        address_name = ("id","com.fs.wawh:id/add_address_name_edit")
        address_phone = ("id","com.fs.wawh:id/add_address_phone_edit")
        address_postal_code = ("id","com.fs.wawh:id/add_address_postal_code_text")
        address_area = ("id","com.fs.wawh:id/add_address_address_show_text")
        area_sure = ("id","com.fs.wawh:id/btn_sure")
        address_detailed = ("id","com.fs.wawh:id/add_address_detailed_address_edit")
        address_save = ("id","com.fs.wawh:id/add_address_save_button")


        find_element(self.driver, mine).click()  # 我的
        # 滑动页面至地址管理
        sleep(1)
        swipeUp(self.driver,500,1)
        find_element(self.driver, address_manage).click() # 地址管理
        find_element(self.driver, add_address).click() # 新增收货地址

        add_address_name = 'huang'
        find_element(self.driver, address_name).send_keys(add_address_name) # 姓名
        find_element(self.driver, address_phone).send_keys('13700001010') # 联系电话
        find_element(self.driver, address_postal_code).send_keys('518000') # 邮政编码
        find_element(self.driver, address_area).click() # 所在区域
        find_element(self.driver, area_sure).click() # 确认区域
        find_element(self.driver, address_detailed).send_keys('天安数码城天吉大厦CD座4楼4D1、4D2室') # 详细地址
        find_element(self.driver, address_save).click() # 保存

        # 判断是否新增成功
        list_address_name = ("text",add_address_name)
        assert assert_element_exist(self.driver, list_address_name) == True

        self.driver.close_app()

        print("新增地址成功")
if __name__=="__main__":
    unittest.main()
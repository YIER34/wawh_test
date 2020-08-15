#coding=utf-8
from time import sleep
from appium import webdriver
from appiumtools import find_element, assert_element_exist,connect
import unittest
import datetime
from public import swipeUp,swipeDown
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@unittest.skip
class Test_Remove_Attention(unittest.TestCase):
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
    def test_remove_attention(self):
        """
        组织账号取消关注企业
        """
        mine = ("text","我的")
        my_attention = ("id","com.fs.wawh:id/user_my_attention_title")
        go_see_botton = ("id","com.fs.wawh:id/go_see")
        attention_status_botton = ("id","com.fs.wawh:id/attention_status") 
        attention_him_count = ("id","com.fs.wawh:id/attention_him_count")

        sleep(1)
        find_element(self.driver,mine).click()  # 我的
        find_element(self.driver,my_attention).click() # 我的关注
        find_element(self.driver,go_see_botton).click() # 点击去看看
        before_count = find_element(self.driver,attention_him_count).text # 关注他的列表数量
        find_element(self.driver,attention_status_botton).click() # 点击取消关注


        # 下拉刷新页面
        sleep(1)
        swipeDown(self.driver,500,1)
        sleep(5)
        after_count = find_element(self.driver,attention_him_count).text

        # 判断关注数-1
        differ_count = int(before_count) - int(after_count)
        assert differ_count == 1

        self.driver.close_app()
        print("取消关注成功")
        '''
        limit_message = '取消关注成功'
        message = '//*[@text=\'{}\']'.format(limit_message)
        toast_element = WebDriverWait(self.driver,4).until(lambda x:x.find_element_by_xpath(message))
        '''
        
if __name__=="__main__":
    unittest.main()


        
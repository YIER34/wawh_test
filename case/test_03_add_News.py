#coding=utf-8
from time import sleep
from appium import webdriver
from appiumtools import find_element, assert_element_exist,connect
from appium.webdriver.common.touch_action import TouchAction
import unittest
import datetime
from public import swipeUp

@unittest.skip
class Test_Add_News(unittest.TestCase):
    #driver = connect() #配置链接
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
    def test_add_news(self):
        """
        组织账号发布资讯
        """
        # 获取设备分辨率,此设备为 1080*1920
        size = self.driver.get_window_size()
        x = (size['width'])
        y = (size['height'])
        # 获取实时发布时间作为标题
        time = datetime.datetime.now().strftime
        news_dt = time('%Y-%m-%d %H:%M:%S')
        news_title_text = "发布资讯测试"+news_dt

        mine = ("text", "我的")
        home_page_bot = ("id","com.fs.wawh:id/btn_home_page")
        fab_up = ("id","com.fs.wawh:id/fab_up") 
        release_news_bot = ("id","com.fs.wawh:id/btn_release_actions") 
        news_title = ("id","com.fs.wawh:id/et_register_content")

        find_element(self.driver, mine).click()
        find_element(self.driver, home_page_bot).click()
        find_element(self.driver, fab_up).click()
        find_element(self.driver, release_news_bot).click()
        find_element(self.driver, news_title).send_keys(news_title_text)
        
        # 资讯类型  700 447 1030 510
        sleep(1)
        self.driver.tap([(x*0.65,y*0.24),(x*0.95,y*0.26)], 100)
        sleep(1)
        # 955 1230  1020 1260
        self.driver.tap([(x*0.88,y*0.64),(x*0.93,y*0.65)], 100)
        sleep(1)
       
        # 分类 700 597  1030 660
        self.driver.tap([(x*0.65,y*0.32),(x*0.95,y*0.34)], 100)
        sleep(1)
        self.driver.tap([(x*0.88,y*0.64),(x*0.93,y*0.65)], 100)

        # 资讯图片
        add_photo =  ("id","com.fs.wawh:id/add_photo")
        image = ("id","com.fs.wawh:id/image_view_album_image")
        image_select = ("id","com.fs.wawh:id/image_view_image_select")
        add_image = ("id","com.fs.wawh:id/menu_item_add_image")
        find_element(self.driver, add_photo).click()
        find_element(self.driver, image).click()
        find_element(self.driver, image_select).click()
        find_element(self.driver, add_image).click()

        # 资讯介绍
        news_content = ("id","com.fs.wawh:id/et_info")
        find_element(self.driver, news_content).send_keys("利用生活实践经验引入教学生活处处有数学。教学时,在观察中讲理旦罚测核爻姑诧太超咖论,从实践中引入概念,增加学生对概念的理解和兴趣。")

        # 发布资讯
        release_news = ("id","com.fs.wawh:id/tv_commit")
        find_element(self.driver, release_news).click()

        # 判断是否发布成功
        succeed = ("text", "提交成功")
        assert assert_element_exist(self.driver, succeed) == True

        self.driver.close_app()
        print("发布资讯成功")

if __name__=="__main__":
    unittest.main()
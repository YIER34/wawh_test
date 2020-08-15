#coding=utf-8
from time import sleep
from appium import webdriver
from appiumtools import find_element, assert_element_exist,connect
from appium.webdriver.common.touch_action import TouchAction
import unittest
import datetime
from public import swipeUp


@unittest.skip
class Test_02_Add_Ation(unittest.TestCase):
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
    def test_02_add_ation(self):
        """
        组织账号发布活动
        """
        # 获取设备分辨率,此设备为 1080*1920
        size = self.driver.get_window_size()
        x = (size['width'])
        y = (size['height'])
        # 获取实时发布时间作为标题
        time = datetime.datetime.now().strftime
        action_dt = time('%Y-%m-%d %H:%M:%S')
        ation_title_text = "发布活动测试"+action_dt

        mine = ("text", "我的")
        home_page_bot = ("id","com.fs.wawh:id/btn_home_page")
        fab_up = ("id","com.fs.wawh:id/fab_up") 
        release_ations_bot = ("id","com.fs.wawh:id/btn_release_news") 
        ation_title = ("id","com.fs.wawh:id/et_register_content")

        find_element(self.driver, mine).click()
        find_element(self.driver, home_page_bot).click()
        find_element(self.driver, fab_up).click()
        find_element(self.driver, release_ations_bot).click()
        find_element(self.driver, ation_title).send_keys(ation_title_text)


        join_time = ("id","com.fs.wawh:id/tv_join_time")
        time_int = int(time('%d'))
        time_str = str(time_int)
        join_start_time = ("text",time_str)
        start_time_ok = ("id","com.fs.wawh:id/tv_ok")
        ation_time = ("id","com.fs.wawh:id/tv_activity_time")
        ation_start_time = ("text", time_str)

        # 报名时间
        find_element(self.driver, join_time).click()
        find_element(self.driver, join_start_time).click()
        sleep(1)
        self.driver.tap([(x*0.88,y*0.64),(x*0.93,y*0.65)], 100)
        sleep(1)
        swipeUp(self.driver,1000,1)
        sleep(1)
        find_element(self.driver, join_start_time).click()
        sleep(1)
        self.driver.tap([(x*0.88,y*0.64),(x*0.93,y*0.65)], 100)
        sleep(1)
        find_element(self.driver, start_time_ok).click()

        # 活动时间
        find_element(self.driver, ation_time).click()
        find_element(self.driver, ation_start_time).click()
        sleep(1)
        self.driver.tap([(x*0.88,y*0.64),(x*0.93,y*0.65)], 100)
        sleep(1)
        swipeUp(self.driver,1000,1)
        sleep(1)
        find_element(self.driver, ation_start_time).click()
        sleep(1)
        self.driver.tap([(x*0.88,y*0.64),(x*0.93,y*0.65)], 100)
        sleep(1)
        find_element(self.driver, start_time_ok).click()


        action_locate_sure =  ("id","com.fs.wawh:id/btn_sure")
        action_locate_detail =  ("id","com.fs.wawh:id/et_locate_detail")
        host_unit = ("text", "请输入举办单位")
        action_cost = ("text", "请输入活动费用")
        action_num = ("text", "请输入报名人数")
        join_limit_num = ("text", "请输入报名限制人数")

        # 活动地点
        sleep(1)
        self.driver.tap([(x*0.65,y*0.46),(x*0.95,y*0.47)], 100)
        find_element(self.driver, action_locate_sure).click()

        # 详细地址
        find_element(self.driver, action_locate_detail).send_keys("香密湖街道办天安数码城天吉大厦")

        # 举办单位
        find_element(self.driver, host_unit).send_keys("深圳市壹办公科技股份有限公司")

        # 活动费用
        find_element(self.driver, action_cost).send_keys("80")
        # 活动人数
        find_element(self.driver, action_num).send_keys("50")

        # 滑动页面
        sleep(1)
        swipeUp(self.driver,500,1)

        # 报名限制人数
        find_element(self.driver, join_limit_num).send_keys("3")

        # 活动图片
        add_photo =  ("id","com.fs.wawh:id/add_photo")
        image = ("id","com.fs.wawh:id/image_view_album_image")
        image_select = ("id","com.fs.wawh:id/image_view_image_select")
        add_image = ("id","com.fs.wawh:id/menu_item_add_image")
        find_element(self.driver, add_photo).click()
        find_element(self.driver, image).click()
        find_element(self.driver, image_select).click()
        find_element(self.driver, add_image).click()

        # 活动介绍
        action_content = ("id","com.fs.wawh:id/et_activity_content")
        find_element(self.driver, action_content).send_keys("利用生活实践经验引入教学生活处处有数学。教学时,在观察中讲理旦罚测核爻姑诧太超咖论,从实践中引入概念,增加学生对概念的理解和兴趣。")

        # 发布活动
        release_action = ("id","com.fs.wawh:id/tv_commit")
        find_element(self.driver, release_action).click()

        # 判断是否发布成功
        succeed = ("text", "提交成功")
        assert assert_element_exist(self.driver, succeed) == True

        self.driver.close_app()
        print("发布活动成功")

if __name__=="__main__":
    unittest.main()
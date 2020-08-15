from selenium.webdriver.support.ui import WebDriverWait
from appium import webdriver
import time
def connect():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '6.0.1',   # 安卓系统的版本号：adb shell getprop ro.build.version.release
        'deviceName':'OPPO R9s',      # 手机/模拟器的型号：adb shell getprop ro.product.model
        'appPackage':'com.fs.wawh',
        'appActivity':'.activities.SplashActivity',
        'unicodeKeyboard':True,                      # 为了支持中文
        'resetKeyboard':True,                        # 设置成appium自带的键盘
        "noReset": True,
        # 'uiautomationName':'uiautomator2'
        }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
    time.sleep(5)


def find_element(driver, locator, timeout=30):
    """
        方法名：显式等待：查找元素
        参数：
            driver：手机的把柄
            locator:元素定位的方式
                格式：
                    - find_element_by_id: ("id", "value")
                    - find_element_by_xpath: ("xpath","value")
                    - find_element_by_accessbility_id：("aid","value")
                    - find_element_by_android_uiautomator: ("text", "Search")
            timeout: 超时时间，默认30秒
        返回值：
            - 找到了元素：返回元素
            - 没有找到元素：直接报错：timeout错误
    """
    if locator[0] == "aid":
        locator = ("accessibility id", locator[1]) # 把自定义的aid变成了原生支持的方式
    if locator[0] == "text":
        locator = ("-android uiautomator", 'new UiSelector().text("{}")'.format(locator[1]))
    
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))


def assert_element_exist(driver, locator, timeout=30):
    """
        判断元素是否存在
        参数：
            driver：手机的把柄
            locator:元素定位的反视
                格式：
                    - find_element_by_id: ("id", "value")
                    - find_element_by_xpath: ("xpath","value")
                    - find_element_by_accessbility_id：("aid","value")
                    - find_element_by_android_uiautomator: ("text", "Search")
            timeout: 超时时间，默认30秒
        返回值：
            - 找到了元素：返回元素
            - 没有找到元素：直接报错：timeout错误
    """
    try:
        find_element(driver, locator, timeout)
        return True
    except:
        return False


    

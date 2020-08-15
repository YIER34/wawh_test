from selenium.webdriver.support.ui import WebDriverWait


def find_element(driver, locator, timeout=60):
    """
        动态查找元素方法
        参数：
            driver： 浏览器的把柄
            locator：元素定位的方式：自己规定的
                - ("id", "username")
                - ("name", "username")
                - ("class name", "username")
                - ("xpath", "username")
                - ("css selector", "username")
                - ("link text", "username")
                - ("partial link text", "username")
            timeout：超时时间
        返回值：
            - 找到元素，返回元素
            - 没有找到元素，直接报错
    """    
    return WebDriverWait(driver, timeout).until(lambda s: s.find_element(*locator))


def assert_element_exist(driver, locator, timeout=60):
    """
        判断元素是否存在
        参数：
            driver： 浏览器的把柄
            locator：元素定位的方式：自己规定的
                - ("id", "username")
                - ("name", "username")
                - ("class name", "username")
                - ("xpath", "username")
                - ("css selector", "username")
                - ("link text", "username")
                - ("partial link text", "username")
            timeout：超时时间
        返回值：
            - 元素存在返回True
            - 元素不存在就返回False
    """
    try:
        find_element(driver, locator, timeout)
        return True
    except:
        return False
    



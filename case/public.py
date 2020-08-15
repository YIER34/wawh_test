# -*- coding: utf-8 -*-
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

def swipeUp(driver,t,n):
    '''向上滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * 0.75
    y2 = l['height'] * 0.35
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipeDown(driver,t,n):
    '''向下滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * 0.35
    y2 = l['height'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x1, y2,t)

def swipLeft(driver, t=500, n=1):
    '''向左滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.75
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)

def swipRight(driver, t=500, n=1):
    '''向右滑动屏幕'''
    l = driver.get_window_size()
    x1 = l['width'] * 0.25
    y1 = l['height'] * 0.5
    x2 = l['width'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x2, y1, t)


def find_toast(driver, message):
    try:
        #ec =expected_conditions
       # message = '//*[@text=\'{}\']'.format(message)
        element = WebDriverWait(driver,10,0.02).until(EC.presence_of_element_located((By.XPATH,message)))
        #_logger.debug("Get Toast : [%s]" % element)
        print('GET TOAST.....')
        return True
    except Exception as e:
        print("Get Toast Error : ",)
       # _logger.debug("Get Toast : [%s and %s]" % (element, e))
        return False
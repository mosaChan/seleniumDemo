# -*- coding:utf-8 -*-
import time
import  os
import configparser
from selenium import webdriver
from baseSetting.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()

class BrowserEngine(object):
    #获得文件的父目录
    #dir = os.path.dirname(os.path.abspath('.'))

    def __init__(self,driver):
        self.driver = driver

    #从配置文件config.ini中获取信息并返回driver
    def open_browser(self,driver):
        #configparser用来读取配置文件信息的包
        config = configparser.ConfigParser()
        #获取config.ini当前路径
        file_path = os.path.dirname(os.path.abspath('.')+'/config/config.ini')
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("You had select %s browser." %browser)

        url = config.get("testServer","URL")
        logger.info("The test server url is: %s" %url)

        if browser == "Firefos":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome()
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie()
            logger.info("Starting IE browser.")

        driver.maximize_window()
        logger.info("Maximize the current window")
        driver.get(url)
        logger.info("Open url:%s" %url)
        driver.implicitly_wait(3)
        logger.info("Set implicitly wait 3 seconds.")
        return driver

    def quit_browser(self):
        self.driver.quit()
        logger.info("Close and quit the browser")
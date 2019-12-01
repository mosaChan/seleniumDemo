# coding=utf-8

import time
import os.path
from baseSetting.logger import Logger
import sys
# coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os.path
from baseSetting.logger import Logger
import sys
import importlib
importlib.reload(sys)

logger = Logger(logger="BasePage").getlog()

class BasePage(object):
    #selenium常用动作封装

    def __init__(self,driver):
        self.driver = driver

    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for % seconds" %seconds)

    def find_element(self,selector):
        try:
            element = self.driver.find_element_by_xpath(selector)
            logger.info("Had find the element \' %s \' successful " % element.text)
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: %s" % e)

        return element

    def s_input(self,selector,text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("input %s into inputbox" %text)
        except NameError as e:
            logger.error("Failed to type input box with %s" %e)

    def s_clear(self,selector):
        el = self.find_element(selector)
        try:
            el.send_keys(Keys.CONTROL+'a')
            el.send_keys(Keys.DELETE)
            logger.info("Clear text in input box before typiing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" %e)

    def s_click(self,selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("the element %s was clicked." %el.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" %e)

    def get_text(self,selector):
        logger.info("Current element text is %s" % self.find_element(selector).text)

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" % seconds)
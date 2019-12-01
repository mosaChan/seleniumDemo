#  coding=utf-8
from baseSetting.base_page import BasePage

class HomePage(BasePage):
    baidu_inputbox = '//*[@id="kw"]'
    baidu_searchbox= '//*[@id="su"]'
    baidu_result='//*[@id="2"]/h3/a'

    #返回文本
    def get_search_text(self):
        self.get_text(self.baidu_result)
        return self.find_element(self.baidu_result).text

    #输入动作
    def input_selenium(self,text):
        self.s_input(self.baidu_inputbox,text)
        self.sleep(1)

    #点击动作
    def click_baidu(self):
        self.s_click(self.baidu_searchbox)
        self.sleep(1)
from selenium import webdriver

import time

class My_bot:
    def __init__(self):
        self.link_site = 'https://192.168.110.10:8001/portal/'
        self.site_map = {}

        self.driver = webdriver.Chrome(executable_path= 'C:\\chromedriver_win32\\chromedriver.exe')
        self.driver.maximize_window()
        
    def abri_site(self):
        time.sleep(2)
        self.driver.get(self.link_site)
        time.sleep(10)


ibot = My_bot()
ibot.abri_site()
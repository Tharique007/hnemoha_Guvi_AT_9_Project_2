from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import Data


class Test_guvi_AT_9_project_2_check:
    url = "https://opensource-demo.orangehrmlive.com/"
    def __init__(self):
        #self.url=url
        self.driver=webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)

c = Test_guvi_AT_9_project_2_check()
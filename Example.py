from selenium import webdriver
from selenium.webdriver.common.by import By


class testcass1:

    def test1_lamda_playground():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.google.com/")
        print("Title:", driver.title)
import pytest
from selenium import webdriver
from config import *


# c_path = r"C:\Users\AS064243\OneDrive - Cerner Corporation\Documents\Learning\pytestframework\pytestframework\drivers\chromedriver.exe"

class DriverInit:

    @pytest.fixture(scope="class", autouse=True)
    def driver_Init(self, request):
        if browser.lower() == "chrome":
            driver = webdriver.Chrome(executable_path=c_path)

        elif browser.lower() == "firefox":
            driver = webdriver.Firefox(executable_path=f_path)

        driver.get(url)
        driver.maximize_window()
        driver.maximize_window()
        request.cls.driver = driver

        yield
        driver.quit()

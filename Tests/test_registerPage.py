import random
from config import *
from POM.register_page import RegisterPage
from Generic_lib.base_fixture import DriverInit

#the entire program will be considered as test module
class TestRegister(DriverInit):  #inheriting fixture class from base_fixture
    # Driver_obj = DriverInit

    #the function will be considered as test Case
    def test_register(self):

        try:
            R_obj = RegisterPage(self.driver)
            # R_obj = RegisterPage(self.driver, url)
            # R_obj.launchURL()
            R_obj.click_register_link()
            R_obj.click_female_radio_button()
            R_obj.enter_first_name()
            R_obj.enter_last_name()
            R_obj.enter_last_name()
            R_obj.enter_email()
            R_obj.enter_password()
            R_obj.confirm_password()
            R_obj.click_register_button()

        except Exception as error_msg:
            prefix_random = random.randint(10, 9999999)
            prefix_random=str(prefix_random)
            self.driver.save_screenshot(screenshots_path+ "ss1.png"+prefix_random)
            raise error_msg

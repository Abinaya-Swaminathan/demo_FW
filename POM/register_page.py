# from config import driver,url
from Generic_lib.web_utils import Generic

class RegisterPage():

    g_obj = Generic()
    login_credentials = g_obj.read_excel()

    def __init__(self, driver):
        # def __init__(self, driver, url):
        self.driver = driver
        # self.url = url

    # def launchURL(self):  # its been given in base_fixture.py so commented here.
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()

    def click_register_link(self):
        self.driver.find_element("link text", "Register").click()

    def click_male_radio_button(self):
        self.driver.find_element("id", "gender-male").click()

    def click_female_radio_button(self):
        self.driver.find_element("id", "gender-female").click()

    def enter_first_name(self):
        # if len(self.login_credentials["firstname"])==5:
        #     self.driver.find_element("id", "FirstName").send_keys(self.login_credentials["firstname"])
        # else:
        #     raise ValueError

        assert len(self.login_credentials["firstname"])==5, "firstname doesnot have 5 characters"
        self.driver.find_element("id", "FirstName").send_keys(self.login_credentials["firstname"])

    def enter_last_name(self):
        self.driver.find_element("id", "LastName").send_keys(self.login_credentials["lastname"])

    def enter_email(self):
        self.driver.find_element("id", "Email").send_keys(self.login_credentials["email"])

    def enter_password(self):
        self.driver.find_element("id", "Password").send_keys(self.login_credentials["password"])

    def confirm_password(self):
        self.driver.find_element("id", "ConfirmPassword").send_keys(self.login_credentials["password"])

    def click_register_button(self):
        self.driver.find_element("id", "register-button").click()




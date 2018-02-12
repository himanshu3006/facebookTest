
from robot.api import logger
from robotpageobjects import Page
from Utility import *


class facebooktest(Page):
    selectors = {
        "email": "xpath=//input[@id='email']",
        "password":"xpath=//input[@id='pass']",
        "login": "xpath=//input[@id='u_0_2']",
    }

    def __init__(self, *args, **kwargs):
        Page.__init__(self)
        self.Utility_obj = Utility()

    def login_facebook(self,email,password):
        # enter email and password
        self.input_text("Enter email", email)
        self.input_text("Enter password", password)
        # click on Login button
        self.click_button("Login button")
        # to display Successfully Login message in Log
        logger.info("Successfully Login")
        return self


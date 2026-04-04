from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # These are locators used to find elements on the login page.
    # By.ID, By.XPATH, and By.LINK_TEXT are different Selenium locator strategies.
    login_link = (By.LINK_TEXT, "Log in")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    login_button = (By.XPATH, "//input[@value='Log in']")

    def __init__(self, driver): # super().__init__(driver) calls the constructor of BasePage.
        super().__init__(driver)

    def click_login(self): #This method clicks on the "Log in" link.
        self.click(self.login_link)

    def enter_email(self, email):  # This method enters the email into the email field.
        self.enter_text(self.email, email)

    def enter_password(self, password):  # This method enters the password into the password field.
        self.enter_text(self.password, password)

    def click_login_button(self):  ## This method clicks the final login button.
        self.click(self.login_button)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # Wait until the element is visible
    # First clear any existing text inside the field
    def enter_text(self,locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    # Enter the new text into the field
    def get_text(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text # Wait until the element is visible and return its text

    def is_visible(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    # Wait until the element becomes visible
    # This returns the WebElement if found
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time


class LoginPage(BasePage):
    def __init__(self, driver):
        """Initialize the LoginPage with a specific login URL."""
        super().__init__(driver)
        self.url = "https://automaticityacademy.ngrok.app/login"

    # Locators
    EMAIL_INPUT = (By.ID, "email") # Email input field
    PASSWORD_INPUT = (By.ID, "password")  # Password input field
    SIGN_IN_BUTTON = (By.XPATH, "//span[contains(text(), 'Sign in')]/ancestor::button") # Sign-in button
    ERROR_MESSAGES = (By.CSS_SELECTOR, "p.text-sm.text-red-600") # Selector for error messages

    # Actions
    def open(self):
        """Opens the login page."""
        self.open_url(self.url)

    def enter_email(self, email):
        """Enters email into the email input field."""
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Enters password into the password input field."""
        self.enter_text(self.PASSWORD_INPUT, password)

    def submit(self):
        """Clicks the sign-in button to submit the login form."""
        self.click_element(self.SIGN_IN_BUTTON)

    def get_all_error_messages(self):
        """Returns a list of all displayed error messages."""
        return [el.text for el in self.find_elements(self.ERROR_MESSAGES)]

    def error_message_exists(self, expected_message):
        """Checks if a specific error message is present among displayed messages."""
        return expected_message in self.get_all_error_messages()

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    URL = "https://automaticityacademy.ngrok.app/register"

    # Locators
    USERNAME_INPUT = (By.ID, "username") # Username input field
    EMAIL_INPUT = (By.ID, "email") # Email input field
    PASSWORD_INPUT = (By.ID, "password") # Password input field
    REGISTER_BUTTON = (By.XPATH, "//span[text()='Register']") # Register button
    ERROR_MESSAGES = (By.CLASS_NAME, "text-red-600") # Error message elements
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Log in now!')]") # Login link

    # Actions
    def submit(self):
        """Clicks the register button to submit the form."""
        self.click_element(self.REGISTER_BUTTON)

    def open(self):
        """Opens the registration page."""
        self.open_url(self.URL)

    def enter_username(self, username):
        """Enters a username into the username input field."""
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_email(self, email):
        """Enters an email into the email input field."""
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Enters a password into the password input field."""
        self.enter_text(self.PASSWORD_INPUT, password)

    def get_all_error_messages(self):
        """Finds and returns a list of all displayed error messages."""
        return [el.text for el in self.find_elements(self.ERROR_MESSAGES)]

    def is_on_register_page(self):
        """Checks if the user is on the registration page by verifying the presence of the register button."""
        return self.is_element_visible(self.REGISTER_BUTTON)

    def is_on_login_page(self):
        """Checks if the user has been redirected to the login page."""
        return self.is_element_visible((By.XPATH, "//h1[contains(text(), 'Welcome Back!')]"))

    def is_element_visible(self, locator, timeout=10):
        """Checks if a specific element is visible on the page within the given timeout."""
        try:
            return self.wait_for_element(locator, timeout) is not None
        except:
            return False



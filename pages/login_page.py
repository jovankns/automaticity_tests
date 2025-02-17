from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://automaticityacademy.ngrok.app/login"

    # Locators
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    SIGN_IN_BUTTON = (By.XPATH, "//span[contains(text(), 'Sign in')]/ancestor::button")
    ERROR_MESSAGES = (By.CSS_SELECTOR, "p.text-sm.text-red-600")

    # Actions
    def open(self):
        self.open_url(self.url)

    def enter_email(self, email):
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def submit(self):
        self.click_element(self.SIGN_IN_BUTTON)
        # time.sleep(2)  # Dodato čekanje kako bi stranica imala vremena da se učita

    def get_all_error_messages(self):
        """Vraća listu svih prikazanih error poruka."""
        return [el.text for el in self.find_elements(self.ERROR_MESSAGES)]

    def error_message_exists(self, expected_message):
        """Proverava da li određena poruka postoji među prikazanim error porukama."""
        return expected_message in self.get_all_error_messages()

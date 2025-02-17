from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegisterPage(BasePage):
    URL = "https://automaticityacademy.ngrok.app/register"

    # Locators
    USERNAME_INPUT = (By.ID, "username")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    REGISTER_BUTTON = (By.XPATH, "//span[text()='Register']")
    ERROR_MESSAGES = (By.CLASS_NAME, "text-red-600")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Log in now!')]")

    # Actions
    def submit(self):
        self.click_element(self.REGISTER_BUTTON)

    def open(self):
        """Otvara register stranicu."""
        self.open_url(self.URL)

    def enter_username(self, username):
        """Unosi korisničko ime."""
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_email(self, email):
        """Unosi email."""
        self.enter_text(self.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Unosi lozinku."""
        self.enter_text(self.PASSWORD_INPUT, password)


    def get_all_error_messages(self):
        """Pronalazi sve prikazane error poruke."""
        return [el.text for el in self.find_elements(self.ERROR_MESSAGES)]

    def is_on_register_page(self):
        """Proverava da li je korisnik na register stranici."""
        return self.is_element_visible(self.REGISTER_BUTTON)

    def is_on_login_page(self):
        """Proverava da li je korisnik preusmeren na login stranicu."""
        return self.is_element_visible((By.XPATH, "//h1[contains(text(), 'Welcome Back!')]"))

    def is_element_visible(self, locator, timeout=10):
        """Proverava da li je element vidljiv."""
        try:
            return self.wait_for_element(locator, timeout) is not None
        except:
            return False

    # def get_all_error_messages(self):
    #     """Pronalazi sve prikazane error poruke. Čeka da se pojave pre nego što ih pročita."""
    #     self.wait_for_element(self.ERROR_MESSAGES, timeout=5)  # Čekamo poruke ako nisu odmah vidljive
    #     return [el.text.strip() for el in self.find_elements(self.ERROR_MESSAGES)]


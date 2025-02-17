from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Eksplicitno čekanje do 10 sekundi

    def open_url(self, url):
        """Otvara zadatu URL adresu"""
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        """Čeka da se element pojavi i vraća ga"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Element {locator} nije pronađen!")
            return None

    def find_elements(self, locator, timeout=10):
        """Čeka da se svi elementi pojave i vraća ih kao listu."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            print(f"Elementi {locator} nisu pronađeni!")
            return []

    def click_element(self, locator):
        """Klikne na element ako postoji"""
        element = self.find_element(locator)
        if element:
            element.click()

    def enter_text(self, locator, text):
        """Unosi tekst u polje"""
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)

    def wait_for_element(self, locator, timeout=10):
        """Čeka da se element pojavi na stranici."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f" Element {locator} nije pronađen!")
            return None

    def wait_for_url_contains(self, text, timeout=10):
        """Čeka da URL sadrži određeni tekst (korisno za proveru preusmeravanja)."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(text))
            return True
        except TimeoutException:
            print(f"URL nije promenjen na očekivani ({text}) u zadatom vremenu.")
            return False

    def is_element_visible(self, locator, timeout=10):
        """Proverava da li je element vidljiv na stranici."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Element {locator} nije vidljiv!")
            return False
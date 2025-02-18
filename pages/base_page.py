from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Explicit wait up to 10 seconds

    def open_url(self, url):
        """Opens the given URL."""
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        """Waits for an element to appear and returns it."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Element {locator} not found!")
            return None

    def find_elements(self, locator, timeout=10):
        """Waits for all matching elements to appear and returns them as a list."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator)
            )
        except TimeoutException:
            print(f"Elements {locator} not found!")
            return []

    def click_element(self, locator):
        """Waits for an element to be present on the page."""
        element = self.find_element(locator)
        if element:
            element.click()

    def enter_text(self, locator, text):
        """Finds an input field, clears it, and enters the given text."""
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(text)

    def wait_for_element(self, locator, timeout=10):
        """Waits for an element to be present on the page."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f" Element {locator} not found!")
            return None

    def wait_for_url_contains(self, text, timeout=10):
        """Waits until the URL contains the specified text (useful for redirects)."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_contains(text))
            return True
        except TimeoutException:
            print(f"URL did not change to expected value ({text}) within timeout.")
            return False

    def is_element_visible(self, locator, timeout=10):
        """Checks if an element is visible on the page."""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Element {locator} is not visible!")
            return False

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    DASHBOARD_INDICATOR = (By.ID, "products-container")

    def is_dashboard_loaded(self):
        """Čeka da se dashboard učita proverom glavnog kontejnera proizvoda."""
        return self.is_element_visible(self.DASHBOARD_INDICATOR)

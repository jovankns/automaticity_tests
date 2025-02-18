from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DashboardPage(BasePage):
    # Locator for the main products container, indicating that the dashboard has loaded
    DASHBOARD_INDICATOR = (By.ID, "products-container")

    def is_dashboard_loaded(self):
        """Waits for the dashboard to load by checking the visibility of the main products container."""
        return self.is_element_visible(self.DASHBOARD_INDICATOR)

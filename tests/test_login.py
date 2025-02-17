import pytest
from pytest_bdd import scenarios, given, when, then
from pytest_bdd import parsers
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

# scenarios("../features/login.feature")

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@given("the user is on the login page", target_fixture="login_page")
def open_login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page

@when("the user enters valid credentials")
def enter_valid_credentials(login_page, config):
    login_page.enter_email(config["valid_user"]["email"])
    login_page.enter_password(config["valid_user"]["password"])
    login_page.submit()

@when("the user enters a valid email but leaves the password empty")
def enter_valid_email_empty_password(login_page, config):
    login_page.enter_email(config["valid_user"]["email"])
    login_page.enter_password("")
    login_page.submit()

@when("the user submits an empty form")
def submit_empty_form(login_page):
    login_page.submit()

@when("the user enters an invalid email")
def enter_invalid_email(login_page, config):
    login_page.enter_email(config["invalid_email"]["email"])
    login_page.submit()

@when("the user enters incorrect credentials")
def enter_incorrect_credentials(login_page):
    """Unosi validan email ali pogrešnu lozinku i šalje formu."""
    login_page.enter_email("validuser@example.com")  # Validan email
    login_page.enter_password("WrongPassword123")  # Pogrešna lozinka
    login_page.submit()


@then("the user should be redirected to the dashboard")
def verify_dashboard_loaded(driver):
    # Čekamo da se dashboard učita
    assert DashboardPage(driver).is_dashboard_loaded(), "Dashboard did not load."

    # Proveravamo da li je URL tačan
    assert "dashboard" in driver.current_url, f"Expected 'dashboard' in URL, but found {driver.current_url}"


@then(parsers.parse('the error message "{message}" should be displayed'))
def check_single_error_message(login_page, message):
    """Proverava da li bilo koja error poruka sadrži očekivani tekst."""
    all_errors = login_page.get_all_error_messages()

    # # Debug ispis
    # print(f"\n🔍 PRONADJENE ERROR PORUKE: {all_errors}")
    # print(f"📝 OČEKIVANA ERROR PORUKA: {message}")

    # Proveravamo da li neka error poruka sadrži očekivanu poruku
    assert any(message in error for error in all_errors), f"Expected: {message}, but found: {all_errors}"
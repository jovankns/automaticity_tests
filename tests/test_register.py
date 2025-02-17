import pytest
import time
from pytest_bdd import scenarios, given, when, then, parsers, scenario
from pages.dashboard_page import DashboardPage
from pages.register_page import RegisterPage

scenarios("../features/register.feature")

@pytest.fixture
def register_page(driver):
    return RegisterPage(driver)

@pytest.fixture
def unique_user():
    timestamp = str(int(time.time()))  # Generiše jedinstveni broj baziran na vremenu
    return {
        "username": f"testuser{timestamp}",
        "email": f"test{timestamp}@mail.com",
        "password": "123456"
    }

# @scenario("../features/register.feature", "Register with empty fields")
# def test_register_with_empty_fields():
#     pass

@given("the user is on the register page")
def user_on_register_page(register_page):
    register_page.open()

@when("the user submits an empty register form")
def user_submits_empty_form(register_page):
    register_page.submit()

@when(parsers.parse('the user enters "{username}" as username'))
def enter_username(register_page, username):
    register_page.enter_username(username)

@when(parsers.parse('the user enters "{email}" as email'))
def enter_email(register_page, email):
    register_page.enter_email(email)

@when(parsers.parse('the user enters "{password}" as password'))
def enter_password(register_page, password):
    register_page.enter_password(password)

@when("the user clicks the Register button")
def click_register(register_page):
    register_page.submit()

@when("the user enters a unique username")
def enter_unique_username(register_page, unique_user):
    register_page.enter_username(unique_user["username"])

@when("the user enters a unique email")
def enter_unique_email(register_page, unique_user):
    register_page.enter_email(unique_user["email"])

@then(parsers.parse('the error message "{message}" should be displayed'))
def check_error_message(register_page, message):
    all_errors = register_page.get_all_error_messages()
    # print(f"\nDEBUG: Očekivana poruka: {message}")
    # print(f"DEBUG: Pronađene poruke: {all_errors}")
    assert message in all_errors, f"Expected error '{message}' not found in {all_errors}"

@when(parsers.parse('the user enters the following registration details:\n| Username | Email | Password |\n| {username} | {email} | {password} |'))
def enter_registration_details(register_page, username, email, password):
    register_page.enter_username(username)
    register_page.enter_email(email)
    register_page.enter_password(password)
    register_page.submit()

# @then(parsers.parse('the error message "{message}" should be displayed'))
# def check_error_message(register_page, message):
#     all_errors = register_page.get_all_error_messages()
#     assert message in all_errors, f"Expected error '{message}' not found. Found errors: {all_errors}"

@then("the user should be redirected to the dashboard")
def check_dashboard_redirect(driver):
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_dashboard_loaded(), f"Not redirected to dashboard! Current URL: {driver.current_url}"
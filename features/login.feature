Feature: Login functionality
  Background:
    Given the user is on the login page

  Scenario: Successful login
    When the user enters valid credentials
    Then the user should be redirected to the dashboard

  Scenario: Login with both fields empty
    When the user submits an empty form
    Then the error message "The email field is required." should be displayed
    And the error message "The password field is required." should be displayed

  Scenario: Login with invalid email
    When the user enters an invalid email
    Then the error message "The email field must be a valid email address." should be displayed
    And the error message "The password field is required." should be displayed

  Scenario: Login with empty password
    When the user enters a valid email but leaves the password empty
    Then the error message "The password field is required." should be displayed

  Scenario: Login with incorrect credentials
    When the user enters incorrect credentials
    Then the error message "The email address or password you entered is invalid" should be displayed

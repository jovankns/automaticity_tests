Feature: Registration functionality

  Background:
    Given the user is on the register page

  Scenario: Register with empty fields
    When the user submits an empty register form
    Then the error message "The username field is required." should be displayed
    And the error message "The email field is required." should be displayed
    And the error message "The password field is required." should be displayed

   Scenario: Register with invalid values in all fields
    When the user enters "1" as username
    And the user enters "1" as email
    And the user enters "1" as password
    And the user clicks the Register button
    Then the error message "The username has already been taken." should be displayed
    And the error message "The email field format is invalid." should be displayed
    And the error message "The password field must be at least 6 characters." should be displayed

   Scenario: Register with existing username
    When the user enters "1" as username
    And the user enters "validemail@mail.com" as email
    And the user enters "123456" as password
    And the user clicks the Register button
    Then the error message "The username has already been taken." should be displayed

  Scenario: Register with invalid email format
    When the user enters "validusername" as username
    And the user enters "1" as email
    And the user enters "123456" as password
    And the user clicks the Register button
    Then the error message "The email field format is invalid." should be displayed

  Scenario: Register with too short password
    When the user enters "validusername" as username
    And the user enters "validemail@mail.com" as email
    And the user enters "1" as password
    And the user clicks the Register button
    Then the error message "The password field must be at least 6 characters." should be displayed

  Scenario: Successful registration
    When the user enters a unique username
    And the user enters a unique email
    And the user enters "123456" as password
    And the user clicks the Register button
    Then the user should be redirected to the dashboard

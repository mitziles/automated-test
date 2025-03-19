Feature: Login to the application

  Scenario: User logs in with valid credentials
    Given User opens login page
    When Introduce credentials
    Then Login successful

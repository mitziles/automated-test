Feature: User Login

  Scenario Outline: Login with multiple users
    Given User opens login page
    When Introduce credentials with username "<email>" and password "<password>"
    Then Login successful

    Examples:
      | email               | password        |
      | example_email       | example_pass    |
      | example_email       | example_pass    |
      | example_email       | example_pass    |



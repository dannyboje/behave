Feature: Demo1 for various key words used in Behave

  Background: Repeat few steps for every scenario
    Given Start web server
    And Connect required database
    And Launch web application

  Scenario: User Registration functionality check
    Given Launch browser
    When I register with valid credentials
    Then User registration should be successful

  Scenario: Login functionality check
    Given Launch browser
    When I login with valid credentials
    Then Login should be successful
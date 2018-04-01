Feature: search product feature

  Scenario: search product using desktop website
    Given I launch a browser on desktop PC
    When I search for any product
    Then Relevant search results should be shown
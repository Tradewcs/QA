@web
Feature: Google Web Browsing
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  Scenario: Basic Google Search
    Given the Google home page is displayed
    When the user searches for "chess"
    Then results are shown for "chess"
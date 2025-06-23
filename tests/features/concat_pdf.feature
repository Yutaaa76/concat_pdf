Feature: Concatenate PDF files
  Scenario: Concatenate two valid PDF files
    Given two valid PDF files
    When I concatenate them
    Then the output PDF should have 2 pages

  Scenario: Concatenate with a missing PDF file
    Given one valid PDF file and one missing PDF file
    When I concatenate them
    Then the output PDF should not exist or should have at most 1 page

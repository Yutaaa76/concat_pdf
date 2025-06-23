Feature: PDF Manipulation
  Scenario: Concatenate two valid PDF files
    Given two valid PDF files
    When I concatenate them
    Then the output PDF should have 2 pages

  Scenario: Concatenate with a missing PDF file
    Given one valid PDF file and one missing PDF file
    When I concatenate them
    Then the output PDF should not exist or should have at most 1 page

  Scenario: Split a PDF into single-page PDFs
    Given two valid PDF files
    When I split the first PDF
    Then the output should be single-page PDFs

  Scenario: Extract the first page from a PDF
    Given two valid PDF files
    When I extract the first page from the first PDF
    Then the extracted PDF should have 1 page

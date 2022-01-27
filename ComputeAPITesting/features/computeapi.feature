# Created by Alex Hromockyj
Feature: Verify the Compute API GET Request Response corresponds to the query variables


  @smoke @regression   # multiple tags can be used in order to group test cases and run specific groups
  Scenario Outline:
    Given the Compute API (endpoint)
    When a user hits the endpoint
    Then the status code response should be 200


  @smoke @regression
  Scenario Outline:
    Given the Compute API (endpoint) and the compute resource
    When a user hits the endpoint with <num1>, <num2>, <operator> and <expected_result>
    Then the response should contain the computation of the numbers and the status code should be 200
    Examples:
      | num1 | num2 | operator | expected_result |
      | 5    |  5   |   +      | 10              |
      | 21039 | 31892 | *      | 670975788       |
      | 98    | 3892  | -      |-3794            |
      | 10000 | 25    | ~      | 400             |







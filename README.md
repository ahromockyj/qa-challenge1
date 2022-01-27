# BackEndAutomation
BDD Testing Framework - Behave with Python:

Test cases are developed following the Given, When, Then template and implementation of each step in that template. In order to run the test cases please use the following command:

behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureResults


Allure Report can be invoked once the results are generated using the following command:

allure serve "path to the AllureResults folder"


import requests
import allure_behave
from behave import *
from utilities.configurations import *
from utilities.resources import *
from utilities import payload


@given('the Compute API (endpoint)')
def step_impl(context):
    context.url = getConfig()['API']['endpoint']


@when('a user hits the endpoint')
def step_impl(context):
    context.response = requests.get(url=context.url)
    context.json_response = context.response.json()


@then('the status code response should be {statusCode:d}')
def step_impl(context, statusCode):
    assert context.response.status_code == statusCode


@given('the Compute API (endpoint) and the compute resource')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.compute()


@when('a user hits the endpoint with {num1}, {num2}, {operator} and {expected_result}')
def step_impl(context, num1, num2, operator, expected_result):
    context.response = requests.get(url=context.url.format(num1, operator, num2))
    context.json_response = context.response.json()
    context.result = expected_result


@then('the response should contain the computation of the numbers and the status code should be {statusCode:d}')
def step_impl(context, statusCode):
    assert statusCode == context.json_response['Status Code']
    assert context.json_response['Result'] == context.result

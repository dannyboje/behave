from behave import *


@given('I launch a browser on desktop PC')
def step_impl(context):
    print('Desktop browser is launched')


@when('I search for any product')
def step_impl(context):
    print('Backend system still searching for your product')


@then('Relevant search results should be shown')
def step_impl(context):
    print('Here are the search results you are looking for')
from behave import *


@Given('Start web server')
def step_impl(context):
    print('background - Web browser started')


@given('Connect required database')
def step_impl(context):
    print('background - Connected to required database')


@given('Launch web application')
def step_impl(context):
    print('background - Web application Launched')


@given('Launch Browser')
def step_impl(context):
    print('Browser Launched')


@when('I register with valid credentials')
def step_impl(context):
    print('Registration completed with valid credentials')


@then('User registration should be successful')
def step_impl(context):
    print('User registration successful\n\n')


@when('I login with valid credentials')
def step_impl(context):
    print('Login attempted with valid credentials')


@then('Login should be successful')
def step_impl(context):
    print('Login is successful\n\n')

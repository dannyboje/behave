from behave import *


@given('Some precondition specific to this scenario')
def step_impl(context):
    print('precondition set up')


@when('I perform some action')
def step_impl(context):
    print('perform action 1')


@when('I perform some additional action')
def step_impl(context):
    print('perform additional action')


@then('Expected results should be shown')
def step_impl(context):
    print('Expected results are shown')


@then('Unwanted results should not be shown')
def step_impl(context):
    print('Unwanted results removed\n\n\n')


@given('Consider mobile device with OS type as "{os_type}"')
def step_impl(context, os_type):
    print('Considered following mobile device with OS type as' + os_type)


@when('I perform mobile os specific action')
def step_impl(context):
    print('Performed mobile OS specific action')


@then('Respective os specific "{preferred_browser}" browser should be launched')
def step_impl(context, preferred_browser):
    print('Following' +preferred_browser+ 'browser is launched\n')

from behave import *


@Given('I login to update details')
def step_impl(context):
    print('I login to update details')


@when('I update following user details "{item_name}" and "{item_detail}"')
def step_impl(context, item_name, item_detail):
    print('Following user details are being updated')
    for row in context.table:
        context.temp_item_name = row['item_name']
        context.temp_item_details = row['item_detail']
        print('=====' + context.temp_item_name + '' + context.temp_item_details)


@then('User detail update should be successful')
def step_impl(context):
    print('User details are updated successfully')
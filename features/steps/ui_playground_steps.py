from behave import given, when, then
from playwright.sync_api import expect

@given('I navigate to the UI Playground home page')
def step_impl(context):
    context.ui_home.navigate_to_url()

@then('the page title should be "{title}"')
def step_impl(context, title):
    assert context.page.title() == title

@then('the h3 link texts should be')
def step_impl(context):
    actual_list = context.ui_home.all_h3_link_texts()
    expected_list = [row['link_text'] for row in context.table]
    assert actual_list == expected_list

@when('I click the "Dynamic ID" link')
def step_impl(context):
    expect(context.ui_home.link_dynamic_id()).to_be_visible()
    context.ui_home.link_dynamic_id().click()

@then('the button with dynamic ID should be visible and clickable')
def step_impl(context):
    expect(context.ui_home.btn_dynamic_id()).to_have_text("Button with Dynamic ID")
    expect(context.ui_home.btn_dynamic_id()).to_be_visible()
    context.ui_home.btn_dynamic_id().click()

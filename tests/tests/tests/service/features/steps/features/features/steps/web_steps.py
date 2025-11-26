# ====================================================================
# Task 7: features/steps/web_steps.py (Code Snippets for Web Steps)
# Note: Assume context.driver and helper functions are defined
# ====================================================================

# Task 7a: Step Definition for the Button Click
@when('I click the "{button_name}" button')
def step_impl(context, button_name):
    """Finds a button by its text (case-insensitive) and clicks it"""
    # This is a common pattern to find buttons:
    context.driver.find_element_by_xpath(
        f"//button[contains(text(), '{button_name}')]"
    ).click()

# Task 7b: Step Definition for verifying for a specific name or text to be present
@then('I should see "{text}"')
@then('I should see the name "{text}" in the "{element_name}" field')
def step_impl(context, text, element_name=None):
    """Verifies that the text is either present on the page or in a specific element"""
    if element_name:
        element = context.driver.find_element_by_id(element_name)
        assert text in element.get_attribute('value') or text in element.text
    else:
        # Search the whole page body for the text
        assert context.driver.find_element_by_tag_name('body').text.find(text) != -1

# Task 7c: Step Definition for verifying for a specific name or text NOT to be present
@then('I should not see "{text}"')
def step_impl(context, text):
    """Verifies that the text is NOT present on the page"""
    body = context.driver.find_element_by_tag_name('body').text
    assert body.find(text) == -1

# Task 7d: Step Definition for verifying a specific message is present
@then('I should see the message "{message}"')
def step_impl(context, message):
    """Verifies that a message is displayed on the page (e.g., in a flash area)"""
    # Assuming a flash message or notification area with a known ID or class
    flash_message = context.driver.find_element_by_id('flash_message') 
    assert message in flash_message.text

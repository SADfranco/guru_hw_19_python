import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@pytest.mark.parametrize("platform", ["ios"], indirect=True)
def test_input_text_ios():
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type('Hello, it is IOS automation test' + '\n')

    with step('Verify content found'):
        output_text = browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output"))
        output_text.should(have.text('Hello, it is IOS automation test'))

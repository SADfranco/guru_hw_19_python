import pytest
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@pytest.mark.parametrize("platform", ["android"], indirect=True)
def test_search_appium_android():
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Click on the first title'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@pytest.mark.parametrize("platform", ["android"], indirect=True)
def test_search_selene_android():
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Selene')

    with step('Click on the first title'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Selene'))
        results.first.click()


@pytest.mark.parametrize("platform", ["ios"], indirect=True)
def test_search_ios():
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).type('Hello, it is IOS automation test')

    with step('Verify content found'):
        output_text = browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output"))
        output_text.should(have.text('Hello, it is IOS automation test'))

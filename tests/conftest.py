import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
from selene import browser, support
import os

from utils import attach

from appium import webdriver


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', params=['android', 'ios'], autouse=True)
def platform(request):
    if request.param == 'android':
        platformName = 'android'
        replatformVersion = '13.0'
        deviceName = 'Google Pixel 7'
        UIoptions = UiAutomator2Options()
    else:
        platformName = 'ios'
        replatformVersion = '16'
        deviceName = 'iPhone 14 Pro Max'
        UIoptions = XCUITestOptions()

    options = UIoptions.load_capabilities({
        # Specify device and os_version for testing
        'platformName': platformName,
        'platformVersion': replatformVersion,
        'deviceName': deviceName,

        # Set URL of the application under test
        'app': 'bs://sample.app',

        # Set other BrowserStack capabilities
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            # Set your access credentials
            'userName': os.getenv("BROWSERSTACK_LOGIN"),
            'accessKey': os.getenv("BROWSERSTACK_PASS")
        }
    })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            os.getenv("BROWSERSTACK_URL"),
            options=options
        )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    attach.attach_screenshot_and_dump(browser)

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    attach.attach_bstack_video(session_id)

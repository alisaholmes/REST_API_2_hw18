import os

import allure
import pytest
from dotenv import load_dotenv
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(autouse=True)
def browser_management(request):
    with allure.step('Настройка браузера'):
        browser.config.base_url = os.getenv('URL')
        browser.config.timeout = 6.0
        browser.config.window_height = 1366
        browser.config.window_width = 1024

    yield

    with allure.step('Закрыть браузер'):
        browser.quit()

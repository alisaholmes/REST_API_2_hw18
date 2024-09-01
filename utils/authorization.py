import os

import allure
import pytest
import requests
from allure_commons.types import AttachmentType
from selene import browser, have


@pytest.fixture(scope='session', autouse=True)
def authorization_API():
    with allure.step('Авторизация'):
        login = os.getenv('LOGIN')
        password = os.getenv('PASSWORD')
        api_url = os.getenv('URL')
        result = requests.post(
            url=api_url + '/login',
            data={"Email": login, "Password": password, "RememberMe": False},
            allow_redirects=False)
        assert result
        allure.attach(body=result.text, name='Response', attachment_type=AttachmentType.TEXT, extension='txt')
        allure.attach(body=str(result.cookies), name='Cookies', attachment_type=AttachmentType.TEXT,
                      extension='txt')
    with allure.step('Получение cookie для API'):
        cookie = result.cookies.get('NOPCOMMERCE.AUTH')
    with allure.step('Передаем cookie для API'):
        browser.open(os.getenv('URL'))
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookie})
        browser.open(os.getenv('URL'))
        cookie = result.cookies.get('NOPCOMMERCE.AUTH')
    with allure.step('Проверка успешной авторизации'):
        browser.element('.account').should(have.text(login))

    return cookie

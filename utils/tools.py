import os
import logging
import allure
from allure_commons.types import AttachmentType
import requests
from selene import browser


def add_to_cart(add_to_cart, cookie, data=False):
    with allure.step('Добавление товара в корзину через API'):
        response = requests.post(
            url=os.getenv('URL') + add_to_cart,
            data=data,
            cookies={'NOPCOMMERCE.AUTH': cookie}
        )
        allure.attach(body=response.text, name='Response', attachment_type=AttachmentType.TEXT, extension='.txt')
        logging.info(response.status_code)
        logging.info(response.text)

        return response.status_code


def clear_cart():
    with allure.step('Очистить корзину'):
        browser.open(os.getenv('URL') + '/cart')
        browser.element('.qty-input').set_value('0').press_enter()

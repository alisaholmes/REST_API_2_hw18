import allure
from allure_commons.types import Severity
from selene import browser, have
from selene.support.conditions import have

from utils.authorization import authorization_API
from utils.tools import add_to_cart, clear_cart


@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'alisaholmes')
@allure.feature('Добавление товара в корзину')
@allure.story('Корзина')
@allure.link('https://demowebshop.tricentis.com', name='demowebshop')
def test_add_to_cart(authorization_API):
    with allure.step('Вход на сайт авторизованным пользователем'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': authorization_API})
        browser.open('/')
    with allure.step('Добавить товар в корзину через API'):
        add_to_cart(add_to_cart='/addproducttocart/catalog/36/1/1', cookie=authorization_API)
    with allure.step('Проверка корзины'):
        browser.element('.ico-cart .cart-label').click()
        browser.element('.product-name').should(have.text('Blue Jeans'))
    with allure.step('Очистить корзину'):
        clear_cart()



@allure.tag('Web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'alisaholmes')
@allure.feature('Отображение товара в корзине')
@allure.story('Корзина')
@allure.link('https://demowebshop.tricentis.com', name='demowebshop')
def test_add_sneaker_to_cart(authorization_API):
    with allure.step('Вход на сайт авторизованным пользователем'):
        browser.open('/')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': authorization_API})
        browser.open('/')

    with allure.step('Проверка статуса добавления товара в корзину'):
        response_code = add_to_cart(add_to_cart='/addproducttocart/details/28/1', cookie=authorization_API, data={
            'product_attribute_28_7_10': 25,
            'product_attribute_28_1_11': 29})
        assert response_code == 200

    with allure.step('Переход в корзину'):
        browser.element('.ico-cart .cart-label').click()

    with allure.step('Отображение товара в корзине'):
        browser.element('.product-name').should(have.text('Blue and green Sneaker'))

    clear_cart()
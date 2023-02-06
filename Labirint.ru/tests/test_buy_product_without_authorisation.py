import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.main_page import MainPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from base.base_class import Base


def test_buy_product():
    """Собираем тест"""

    s = Service('/home/nevi/Документы/resource/chromedriver')
    driver = webdriver.Chrome(service=s)

    mp = MainPage(driver)
    mp.go_to_site()

    pg = ProductsPage(driver)
    pg.select_products()

    cp = CartPage(driver)
    cp.buy_products()

    bc = Base(driver)
    bc.get_screenshot()

    time.sleep(5)

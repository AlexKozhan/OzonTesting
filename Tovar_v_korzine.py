"""Добавление товара в корзину и оформление заказа"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запускаем браузер
driver = webdriver.Chrome()

# Открываем страницу товара
driver.get("https://www.ozon.ru/product/apple-macbook-pro-13-2020-2021-silver-myd82ru-a-217010296/")

# Добавляем товар в корзину
add_to_cart_button = driver.find_element_by_css_selector("button.buy-button")
add_to_cart_button.click()

# Ждем, пока появится модальное окно с информацией о добавлении товара в корзину
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[data-widget='alert-popup']")))

# Переходим в корзину
cart_button = driver.find_element_by_css_selector("a[href='/cart']")
cart_button.click()

# Проверяем, что товар добавлен в корзину
assert "cart" in driver.current_url, "Не удалось добавить товар в корзину"

# Оформляем заказ (примерно)
checkout_button = driver.find_element_by_css_selector("button.bBtn")
checkout_button.click()

# Проверяем, что мы перешли на страницу оформления заказа
assert "checkout" in driver.current_url, "Не удалось перейти на страницу оформления заказа"

# Закрываем браузер
driver.quit()

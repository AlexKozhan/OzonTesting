"""Проверка фильтрации результатов поиска"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запускаем браузер
driver = webdriver.Chrome()

# Открываем страницу
driver.get("https://www.ozon.ru/?__rr=1&abt_att=1")

# Находим поле для ввода текста
search_box = driver.find_element_by_name("text")

# Вводим текст для поиска
search_box.send_keys("ноутбук")

# Находим и кликаем на кнопку поиска
search_button = driver.find_element_by_css_selector("button.search-button")
search_button.click()

# Ждем, пока появятся результаты поиска
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "search-results")))

# Находим фильтр по цене и устанавливаем диапазон цен
price_filter = driver.find_element_by_css_selector("input[data-test-id='range-filter-from']")
price_filter.clear()
price_filter.send_keys("50000")

# Применяем фильтр
apply_filter_button = driver.find_element_by_css_selector("button.apply-button")
apply_filter_button.click()

# Ждем, пока обновятся результаты поиска после применения фильтра
WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "spinner")))

# Проверяем, что отображаются только товары, цена которых больше 50000
products = driver.find_elements_by_css_selector(".search-results .product")
for product in products:
    price = product.find_element_by_css_selector(".price span").text
    assert float(price.replace(" ", "")) >= 50000, "Товар с ценой ниже 50000 отображается после применения фильтра"

# Закрываем браузер
driver.quit()

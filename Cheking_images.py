"""Проверка загрузки и отображения изображений товара:"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запускаем браузер
driver = webdriver.Chrome()

# Открываем страницу товара
driver.get("https://www.ozon.ru/product/apple-macbook-pro-13-2020-2021-silver-myd82ru-a-217010296/")

# Ждем, пока загрузится изображение товара
image = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img.image")))

# Проверяем, что изображение товара загружено и отображается
assert image.is_displayed(), "Изображение товара не загружено или не отображается"

# Проверяем наличие атрибута src у изображения
src = image.get_attribute("src")
assert src is not None, "У изображения товара отсутствует атрибут src"

# Закрываем браузер
driver.quit()

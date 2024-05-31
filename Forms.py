"""Заполнение формы и отправка данных"""

from selenium import webdriver

# Запускаем браузер
driver = webdriver.Chrome()

# Открываем страницу
driver.get("https://www.ozon.ru/?__rr=1&abt_att=1")

# Находим поле для ввода текста
search_box = driver.find_element_by_name("text")

# Вводим текст для поиска
search_box.send_keys("книги")

# Находим кнопку поиска и кликаем на нее
search_button = driver.find_element_by_css_selector("button.search-button")
search_button.click()

# Проверяем, что перешли на страницу с результатами поиска
assert "search-results" in driver.current_url, "Не удалось выполнить поиск"

# Закрываем браузер
driver.quit()

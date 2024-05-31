"""Авторизация пользователя"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запускаем браузер
driver = webdriver.Chrome()

# Открываем страницу авторизации
driver.get("https://www.ozon.ru/login")

# Заполняем форму авторизации
email_field = driver.find_element_by_name("email")
email_field.send_keys("testuser@example.com")

password_field = driver.find_element_by_name("password")
password_field.send_keys("password123")

# Отправляем форму
login_button = driver.find_element_by_css_selector("button.login-button")
login_button.click()

# Ждем, пока произойдет авторизация и появится профиль пользователя
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.user-profile")))

# Проверяем наличие профиля пользователя
user_profile = driver.find_element_by_css_selector("div.user-profile")
assert user_profile is not None, "Не удалось авторизоваться"

# Закрываем браузер
driver.quit()

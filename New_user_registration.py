"""Регистрация нового пользователя"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запускаем браузер
driver = webdriver.Chrome()

# Открываем страницу регистрации
driver.get("https://www.ozon.ru/register")

# Заполняем форму регистрации
username_field = driver.find_element_by_name("username")
username_field.send_keys("testuser")

email_field = driver.find_element_by_name("email")
email_field.send_keys("testuser@example.com")

password_field = driver.find_element_by_name("password")
password_field.send_keys("password123")

# Отправляем форму
register_button = driver.find_element_by_css_selector("button.register-button")
register_button.click()

# Ждем, пока появится сообщение об успешной регистрации
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.success-message")))

# Проверяем наличие сообщения об успешной регистрации
success_message = driver.find_element_by_css_selector("div.success-message")
assert "Успешная регистрация" in success_message.text, "Регистрация не удалась"

# Закрываем браузер
driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

driver = webdriver.Chrome()

driver.get("https://kinogo.biz/")

wait = WebDriverWait(driver, 10)
# Ждем пока прогрузится начальная страница сайта
search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[4]/div/div/div[2]/div[2]/form/input")))
# Вводим в поиске название фильма
search_input.click()
search_input.clear()
search_input.send_keys("кинг-конг")
# Выбираем первый в предложенных
first_recommended_film=wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[4]/div/div/div[2]/div[2]/form/div/div[1]/a[1]/div[2]")))
first_recommended_film.click()
# Вытягиваем ссылку на видео

player_window=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#dle-content > article > div.section > div.js-player-container.player-container > iframe")))
link = player_window.get_attribute("data-src")
link = "https:"+link
response = requests.get(link)

if response.status_code == 200:
    print("hihiihihih")  # Вывод содержимого ответа
else:
    print("Ошибка при выполнении запроса. Код состояния:", response.status_code)
driver.quit()
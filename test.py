from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

driver = webdriver.Chrome()

driver.get("https://kinogo.biz/")
driver.implicitly_wait(1)

# Ждем, пока элемент появится на странице
wait = WebDriverWait(driver, 10)
# Вводим в поиске название фильма
search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[4]/div/div/div[2]/div[2]/form/input")))
search_input.click()
search_input.clear()
search_input.send_keys("кинг-конг")
driver.implicitly_wait(2)

# Выбираем первый в предложенных

driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div/div[2]/div[2]/form/div/div[1]/a[1]/div[2]").click()

# Вытягиваем ссылку на видео

iframe = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/div[1]/div[1]/article/div[7]/div[3]/iframe")
link = iframe.get_property("src")

response = requests.get(link)

if response.status_code == 200:
    print(response.text)  # Вывод содержимого ответа
else:
    print("Ошибка при выполнении запроса. Код состояния:", response.status_code)
driver.quit()
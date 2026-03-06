from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Espera explícita hasta que carguen los productos
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item"))
)

# Parsear con BeautifulSoup
soup = BeautifulSoup(driver.page_source, "html.parser")
data = []

for p in soup.find_all("div", class_="inventory_item"):
    nombre = p.find("div", class_="inventory_item_name").text
    precio = p.find("div", class_="inventory_item_price").text
    data.append([nombre, precio])

df = pd.DataFrame(data, columns=["Producto", "Precio"])
print(df)

driver.quit()
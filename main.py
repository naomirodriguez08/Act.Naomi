#python -m venv venv
#Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
#.\venv\Scripts\Activate
#pip install selenium
#pip install webdriver-manager

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import pandas as pd
import time


USER = "standard_user"

PASSWORD = "secret_sauce"

def main():
   service = Service(ChromeDriverManager().install())
   option = webdriver.ChromeOptions()
   #option.add_argument("--headless")
   option.add_argument("--window-size=1920,1080")
   driver = Chrome(service=service, options=option)
   driver.get("https://www.saucedemo.com/")

   #LOGIN
   user_input = driver.find_element("id", "user-name").send_keys(USER)
   pass_input = driver.find_element("id", "password").send_keys(PASSWORD)
   driver.find_element("id", "login-button").click()
   time.sleep(2)

   #compra
   driver.find_element("id.name", "add-to-cart-sauce-labs-bolt-t-shirt").click()
   driver.find_element( "id", "add-to-cart-test.allhethings()-t-shirt-(red)").click()
   time.sleep(2)

   #carrito
   driver.find_element(
       "id.XPATH", "/html/body/div/div/div/div[1]/div[2]/div[2]/div[3]/a"
   ).click()
   time.sleep(2)

   driver.find_element("id", "checkout").click()

   #pago
   driver.find_element("id", "first-name").send_keys("TEST")
   driver.find_element("id", "last-name").send_keys("TEST")
   driver.find_element("id", "postal-code").send_keys("123467")
   time.sleep(2)

   driver.find_element("id", "continue").click()
   time.sleep(4)

   driver.find_element("id", "finish").click()

   time.sleep(10)
   driver.quit()


if __name__ == "__main__":
    main()
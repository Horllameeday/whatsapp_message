from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver_path = 'C:/Users/user/Documents/Applications/chromedriver_win32/chromedriver.exe'
chat = 'replace with the chat name'
message = 'Hello, this is an automated message'
url = 'https://web.whatsapp.com/'

driver = webdriver.Chrome(driver_path)
driver.get(url)

x_arg = f"//span[@title='{chat}']"
chat = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, x_arg))).click()

message_box = driver.find_element_by_class_name('_2A8P4')
message_box.send_keys(message + Keys.ENTER)
time.sleep(3)

print('Done')
driver.close()

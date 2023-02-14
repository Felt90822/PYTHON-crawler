from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

options=Options()
options.chrome_executable_path="C:\\Users\\USER\\OneDrive\\桌面\\Python專用\\crawler\\chromedriver.exe"
driver = webdriver.Chrome(options=options)

driver.get('https://zh.wikipedia.org/zh-tw/Wikipedia:%E9%A6%96%E9%A1%B5')

WebDriverWait(driver, 10).until(  #等待10秒 直到...載入
    EC.presence_of_element_located((By.NAME, "search"))
)

keys = "香蕉"
search = driver.find_element(By.NAME, "search")
search.send_keys(keys)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(  #等待10秒 直到...載入
    EC.presence_of_element_located((By.LINK_TEXT, keys))
)

enter = driver.find_element(By.LINK_TEXT, keys)
enter.click()

WebDriverWait(driver, 10).until(  #等待10秒 直到...載入
    EC.presence_of_element_located((By.CLASS_NAME, "image"))
)

IMG = driver.find_element(By.CLASS_NAME, "image")
IMG.click()

WebDriverWait(driver, 10).until(  #等待10秒 直到...載入
    EC.presence_of_element_located((By.CLASS_NAME, "jpg"))
)

pic = driver.find_element(By.CLASS_NAME, "jpg")
print(pic.get_attribute("src"))
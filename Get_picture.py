from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
import wget
import time

options=Options()
options.chrome_executable_path="C:\\Users\\USER\\OneDrive\\桌面\\Python專用\\crawler\\chromedriver.exe"

driver = webdriver.Chrome(options=options)

driver.get("https://twitter.com/i/flow/login")

name = WebDriverWait(driver, 10).until(  #等待10秒 直到...載入
    EC.presence_of_element_located((By.NAME, "text"))
)
name.send_keys("Felt90822")
name.send_keys(Keys.RETURN)

password = name = WebDriverWait(driver, 10).until(  #等待10秒 直到...載入
    EC.presence_of_element_located((By.NAME, "password"))
)
name.send_keys("Zero9487")
name.send_keys(Keys.RETURN)

check = WebDriverWait(driver, 10).until(  #等待10秒 直到...載入
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]'))
)
check.click()
time.sleep(1)

search = WebDriverWait(driver, 10).until(  #等待10秒 直到...載入
    EC.presence_of_element_located((By.CLASS_NAME, 'r-30o5oe'))
)
keyword = "#dog"
search.send_keys(keyword)
search.send_keys(Keys.RETURN)
time.sleep(1)

WebDriverWait(driver, 10).until(  #等待10秒 直到...載入
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[4]/a'))
)
pic_button = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[4]/a')
pic_button.click()
time.sleep(5)

imgs = driver.find_elements(By.CLASS_NAME, "css-9pa8cd")

path = os.path.join(keyword)
os.mkdir(path)
count = 0

for img in imgs:
    src = img.get_attribute("src")
    if src[-10:] == "name=small":
        save_as = os.path.join(path, keyword + str(count) + '.jpg')
        print(f"圖片位置:{src}")
        wget.download(img.get_attribute("src"), save_as)
        count += 1
    


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

driver.get('https://tw.search.yahoo.com/?fr=mcafee')

WebDriverWait(driver, 10).until(  #等待10秒 直到...載入
    EC.presence_of_element_located((By.NAME, "p"))
)

word = "貓"
search = driver.find_element(By.NAME, "p")
search.send_keys(word)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(  #等待10秒 直到...載入
    EC.presence_of_element_located((By.XPATH, '//*[@id="horizontal-bar"]/ol/li[1]/div/div[1]/ul/li[2]/a'))
)

BUTTON = driver.find_element(By.XPATH, '//*[@id="horizontal-bar"]/ol/li[1]/div/div[1]/ul/li[2]/a')
BUTTON.click()
time.sleep(5)

imgs = driver.find_elements(By.CLASS_NAME, "img")
for img in imgs:
    print(img.get_attribute("class src"))
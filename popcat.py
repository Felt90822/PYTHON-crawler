from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options=Options()
options.chrome_executable_path="C:\\Users\\USER\\OneDrive\\桌面\\Python專用\\crawler\\chromedriver.exe"
driver = webdriver.Chrome(options=options)

driver.get('https://popcat.click/')

cat = driver.find_element(By.ID, "app")

for i in range(1000):
    cat.click()

driver.close()

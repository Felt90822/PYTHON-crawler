from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options=Options()
options.chrome_executable_path="C:\\Users\\USER\\OneDrive\\桌面\\Python專用\\crawler\\chromedriver.exe"

driver = webdriver.Chrome(options=options)

driver.get("https://info.hwsh.ylc.edu.tw/online/")

userName = driver.find_element(By.NAME, "Loginid")
passWord = driver.find_element(By.NAME, "LoginPwd")

userName.send_keys("Your account")
passWord.send_keys("Your password")

signIn = driver.find_element(By.NAME, "Enter")

signIn.send_keys(Keys.RETURN)
time.sleep(5)

driver.close()

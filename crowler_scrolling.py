#運用 Selenium 捲動視窗
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.chrome_excutable_path="C:\\Users\\USER\\OneDrive\\桌面\\Python專用\\crawler\\chromedriver.exe"

driver = webdriver.Chrome(options=options)

driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")
#捲動視窗並等待瀏覽器載入更多內容
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

titleTags = driver.find_elements(By.CLASS_NAME, "base-search-card__title")
for titleTags in titleTags:
    print(titleTags.text)
driver.close()

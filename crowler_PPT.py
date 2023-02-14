from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''
options = Options()
options.chrome_excutable_path="C:\\Users\\USER\\OneDrive\\桌面\\Python專用\\crawler\\chromedriver.exe"

driver = webdriver.Chrome(options=options)
'''
PATH = "C:\\Users\\USER\\OneDrive\\桌面\\Python專用\\crawler\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.ptt.cc/bbs/Stock/index.html")
search = driver.find_element(By.NAME, "q")
search.clear() #清理搜尋欄位
search.send_keys("比特幣")    #輸入文字
search.send_keys(Keys.RETURN) #按下Enter鍵

element = WebDriverWait(driver, 10).until(  #等待10秒 直到...載入
        EC.presence_of_element_located((By.CLASS_NAME, "title"))
    )

'''
titles = driver.find_elements(By.CLASS_NAME, "title")
for title in titles:
    print(title.text)
'''
#尋找該文章的標題
link = driver.find_element(By.LINK_TEXT, "Re: [新聞] 特斯拉像比特幣 克魯曼：靠炒作和信仰")
#典籍該文章的標題
link.click()
'''
driver.back() #回到上一頁
driver.forward() #上一頁
'''
time.sleep(5)

driver.quit()
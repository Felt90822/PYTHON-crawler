#載入selenium相關物件
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#建立 Chrome Driver 的執行檔路徑
options=Options()
options.chrome_excutable_path="C:\\Users\\USER\\OneDrive\\桌面\\Python專用\\crawler\\chromedriver.exe"

#建立 Deiver 物件實體
driver=webdriver.Chrome(options=options)

'''
driver.maximize_window() #視窗最大化
driver.get("https://www.google.com.tw/")
#連線後做網頁截圖
driver.save_screenshot("screen_shot_max.png")
'''

driver.get("https://www.ptt.cc/bbs/Stock/index.html")
#print(driver.page_source) #取得網頁原始碼
'''
tags=driver.find_elements(By.CLASS_NAME, "title") #搜尋 class 屬性是 title 的所有訊息

for tag in tags:
    print(tag.text) #取得標籤裡的文字
'''
#取得上一頁文章標題
link = driver.find_element(By.LINK_TEXT, "‹ 上頁") #取得超連結的標籤
link.click() #模擬使用者點擊
tags=driver.find_elements(By.CLASS_NAME, "title")
for tag in tags:
    print(tag.text) #取得標籤裡的文字

driver.close()

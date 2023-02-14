#網路連線
import urllib.request as request
import json
'''
src = 'https://zh.wikipedia.org/'
with request.urlopen(src) as response:
    data= response.read().decode("utf-8")   #取得維基百科的原始碼 (HTML, CSS, JS),並用utf-8編碼
print(data)
'''
src1 = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire" #台大
with request.urlopen(src1) as response:
    data = json.load(response) #抓取 json 

# 將公司名稱印出
clist = data["result"]["results"]
for company in clist:
    print(company["公司名稱"]) #字典 
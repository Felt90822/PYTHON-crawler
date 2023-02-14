#抓取維基百科網頁原始碼(HTML)
import urllib.request as req
def getData(url):
    #建立一個 Request 物件, 附加Request Headers 的資訊
    request = req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    #解析原始碼, 取得每篇文章的標題
    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div",class_="title") #尋找 class = "nav-trigger hamburger"
    
    for title in titles: #印出所有
        if title.a != None: #如果 html 的 .a 存在 就印出來
            print(title.a.string) 
    
    #抓取上一頁的連結
    nextLink = root.find("a", string="下頁 ›")
    return nextLink["href"]
#主程序 : 抓取多個頁面的標籤
pageURL = "https://www.ptt.cc/bbs/Gossiping/index1.html"
count = 0
while count<3:
    pageURL = "https://www.ptt.cc" + getData(pageURL)
    count += 1

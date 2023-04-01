import urllib.request as req
import bs4

def bs():
    url = "https://www.bbc.com"
    # 幫request加上一個header
    newURL = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
    })

    with req.urlopen(newURL) as response:
        data = response.read().decode("utf-8")
    #print('所取得的資料型態：',type(data))
    #print('===得到的部份HTML內容===\n', data[2651:3500])

    root = bs4.BeautifulSoup(data,"html.parser")#解析器
    bbctitles = root.find_all("li", class_="title")#find title in div
    #print(titles[0].text)
    bbclink = root.find_all("li", class_="title")

    return bbctitles ,bbclink
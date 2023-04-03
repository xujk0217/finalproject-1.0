import urllib.request as req
import bs4

def bsbbc():
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
    promo = root.find("section", class_="module--promo")
    bbctitles = promo.find_all("a", class_="media__link")#find title in div
    #print(titles[0].text)
    bbcmain = promo.find_all("p", class_="media__summary")
    bbcdata = []
    for i in range(len(bbctitles)):
        itemcol = []
        title=bbctitles[i].text
        itemcol.append(title)
        url=bbctitles[i].get('href')
        itemcol.append(url)
        try:
            content=bbcmain[i].text
            itemcol.append(content)
        except IndexError:
            itemcol.append('no content')
        bbcdata.append(itemcol)

    #bbclinks = root.find_all("a[herf]", class_="media__link")
    #print('bbctitles[0]')
    #print(type(bbctitles))
    return bbcdata
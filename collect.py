import urllib.request as req
import bs4

def bsbbc():
    url = "https://www.bbc.com/news"
    # 幫request加上一個header
    newURL = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
    })

    with req.urlopen(newURL) as response:
        data = response.read().decode("utf-8")
    #print('所取得的資料型態：',type(data))
    #print('===得到的部份HTML內容===\n', data[2651:3500])

    root = bs4.BeautifulSoup(data,"html.parser")#解析器
    promo = root.find("div", id="news-top-stories-container")
    bbctitles = promo.find_all("h3", class_="gs-c-promo-heading__title")#find title in div
    #print(titles[0].text)
    bbcurls = promo.find_all("a", class_="gs-c-promo-heading")

    bbcmain = promo.find_all("p", class_="gs-c-promo-summary")
    bbcdata = []
    for i in range(1, len(bbctitles)):
        itemcol = []
        title=bbctitles[i].text
        itemcol.append(title)
        url=bbcurls[i].get('href')
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






def bsmappa():
    url = "https://www.mappa.co.jp/"
    # 幫request加上一個header
    newURL = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
    })

    with req.urlopen(newURL) as response:
        data = response.read().decode("utf-8")
    #print('所取得的資料型態：',type(data))
    #print('===得到的部份HTML內容===\n', data[2651:3500])

    root = bs4.BeautifulSoup(data,"html.parser")#解析器
    promo = root.find("section", id="news")
    mappatitles = promo.find_all("p", class_="newsLists__title")#find title in div
    #print(titles[0].text)
    mappaurls = promo.find_all("a", class_="newsLists__link")

    mappadate = promo.find_all("time")
    mappadata = []
    for i in range(len(mappatitles)):
        itemcol = []
        title=mappatitles[i].text
        itemcol.append(title)
        url=mappaurls[i].get('href')
        itemcol.append(url)
        try:
            time=mappadate[i].text
            itemcol.append(time)
        except IndexError:
            itemcol.append('no content')
        mappadata.append(itemcol)
    return mappadata





def bsyahoo():
    url = "https://movies.yahoo.com.tw/movie_intheaters.html"
    # 幫request加上一個header
    newURL = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
    })

    with req.urlopen(newURL) as response:
        data = response.read().decode("utf-8")
    #print('所取得的資料型態：',type(data))
    #print('===得到的部份HTML內容===\n', data[2651:3500])

    root = bs4.BeautifulSoup(data,"html.parser")#解析器
    promo = root.find("ul", class_="release_list")
    yahootitles = promo.find_all("a", class_="gabtn")#find title in div
    #print(titles[0].text)
    #yahoocontent = promo.find_all("span", class_="jq_text_overflow_180 jq_text_overflow_href_list")

    yahoodate = promo.find_all("div", class_="release_movie_time")
    yahoodata = []
    for i in range(1,60,6):
        itemcol = []
        title=yahootitles[i].text
        itemcol.append(title)
        url=yahootitles[i].get('href')
        itemcol.append(url)
        #content = yahoocontent[i].text
        #itemcol.append(content)
        oa = i//6
        try:
            time=yahoodate[oa].text
            itemcol.append(time)
        except IndexError:
            itemcol.append(yahoodate[1].text)
        yahoodata.append(itemcol)
    return yahoodata

def bsufo():
    url = "https://www.ufotable.com/"
    # 幫request加上一個header
    newURL = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
    })

    with req.urlopen(newURL) as response:
        data = response.read().decode("utf-8")
    #print('所取得的資料型態：',type(data))
    #print('===得到的部份HTML內容===\n', data[2651:3500])

    root = bs4.BeautifulSoup(data,"html.parser")#解析器
    promo = root.find("div", id="inforbox")
    ufotitles = promo.find_all("a")#find title in div
    #print(titles[0].text)
    #ufourls = promo.find_all("a", class_="newsLists__link")

    ufodate = promo.find_all('p', class_="news-date")
    ufodata = []
    for i in range(10):
        itemcol = []
        title=ufotitles[i].text
        itemcol.append(title)
        url=ufotitles[i].get('href')
        itemcol.append(url)
        try:
            time=ufodate[i].text
            itemcol.append(time)
        except IndexError:
            itemcol.append('no content')
        ufodata.append(itemcol)
    return ufodata


def bscw():
    url = "https://cloverworks.co.jp/news/"
    # 幫request加上一個header
    newURL = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
    })

    with req.urlopen(newURL) as response:
        data = response.read().decode("utf-8")
    #print('所取得的資料型態：',type(data))
    #print('===得到的部份HTML內容===\n', data[2651:3500])

    root = bs4.BeautifulSoup(data,"html.parser")#解析器
    promo = root.find("ul", class_="thumblist")
    cwtitles = promo.find_all("div", class_="item__title")#find title in div
    #print(titles[0].text)
    cwurls = promo.select("li.list__item>a")

    cwdate = promo.find_all('p', class_="item__date")
    cwdata = []
    for i in range(10):
        itemcol = []
        title=cwtitles[i].text
        itemcol.append(title)
        url=cwurls[i].get('href')
        itemcol.append(url)
        try:
            time=cwdate[i].text
            itemcol.append(time)
        except IndexError:
            itemcol.append('no content')
        cwdata.append(itemcol)
    return cwdata



def bswsj():
    url = "https://www.wsj.com/news/world?mod=nav_top_section"
    # 幫request加上一個header
    newURL = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
    })

    with req.urlopen(newURL) as response:
        data = response.read().decode("utf-8")
    #print('所取得的資料型態：',type(data))
    #print('===得到的部份HTML內容===\n', data[2651:3500])

    root = bs4.BeautifulSoup(data,"html.parser")#解析器
    promo = root.find("div", id="top-news")
    wsjtitles = promo.find_all("span", class_="WSJTheme--headlineText--He1ANr9C")#find title in div
    #print(titles[0].text)
    wsjurls = promo.select(".WSJTheme--headline--unZqjb45>a")

    wsjmain = promo.find_all("span", class_="WSJTheme--summaryText--2LRaCWgJ")
    wsjdata = []
    #print("title", wsjtitles, len(wsjtitles))
    #print("url", wsjurls, len(wsjurls))
    #print("main", wsjmain, len(wsjmain))
    for i in range(len(wsjtitles)):
        itemcol = []
        title=wsjtitles[i].text
        itemcol.append(title)
        url=wsjurls[i].get('href')
        itemcol.append(url)
        try:
            content=wsjmain[i].text
            itemcol.append(content)
        except IndexError:
            itemcol.append('no content')
        wsjdata.append(itemcol)

    #wsjlinks = root.find_all("a[herf]", class_="media__link")
    #print('wsjtitles[0]')
    #print(type(wsjtitles))
    return wsjdata


def bsuni():
    url = "https://www.u-movie.com.tw/cinema/page.php?page_type=coming"
    # 幫request加上一個header
    newURL = req.Request(url, headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
    })

    with req.urlopen(newURL) as response:
        data = response.read().decode("utf-8")
    #print('所取得的資料型態：',type(data))
    #print('===得到的部份HTML內容===\n', data[2651:3500])

    root = bs4.BeautifulSoup(data,"html.parser")#解析器
    promo = root.find("main", class_="col-12 col-lg-9 right-sidebar md-margin-60px-bottom sm-margin-40px-bottom md-padding-15px-lr")
    unititles = promo.find_all("h3", class_="text-large")#find title in div
    #print(titles[0].text)
    uniurl = promo.find_all("a")
    unicontent = promo.find_all("p", class_="m-0 width-95")
    unidata = []
    for i in range(9):
        itemcol = []
        title=unititles[i].text
        itemcol.append(title)
        url=uniurl[2*i].get('href')
        itemcol.append(url)
        #content = unicontent[i].text
        #itemcol.append(content)
        try:
            content=unicontent[i].text
            itemcol.append(content)
        except IndexError:
            itemcol.append('no content')
        unidata.append(itemcol)
    return unidata


# def bsimg():
#     url = "https://www.bbc.com/news"
#     newURL = req.Request(url, headers = {
#         "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
#     })
#     with req.urlopen(newURL) as response:
#         data = response.read().decode("utf-8")
#     root = bs4.BeautifulSoup(data,"html.parser")
#     imgbbc = root.find_all("img", class_="image-replace")

#     # url = "https://www.wsj.com/?gclid=Cj0KCQjw8qmhBhClARIsANAtbodKLgqnUcV6B-rMBgB6EMgp5-JEjGQV2tQ50yPLzzzzz8bqXOvPhKYaAhoFEALw_wcB&gclsrc=aw.ds&ef_id=ZCgUAAAAAGTO-QAm:20230403091551:s"
#     # newURL = req.Request(url, headers = {
#     #     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
#     # })
#     # with req.urlopen(newURL) as response:
#     #     data = response.read().decode("utf-8")
#     # roots = bs4.BeautifulSoup(data,"html.parser")
#     # imgwsj = roots.find_all("img", class_="WSJTheme--image--At42misj ")


#     imgdata = []
#     for i in range(1):
#         itemcol = []
#         bbcim=imgbbc[i].get('href')
#         itemcol.append(bbcim)
#         # swjim=imgwsj[i].get('src')
#         # itemcol.append(swjim)
#         imgdata.append(itemcol)
#     return imgdata
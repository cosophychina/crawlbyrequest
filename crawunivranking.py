#CrawUnivRankingB.py
from myrequests import MyRequest
from bs4 import BeautifulSoup
import bs4
 
def getHTMLText(url):
    return MyRequest().getUrlHtml(url, limitLen = False)
 
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    soup = soup.find('tbody')
    if soup is None:
        print("no tbody tag found!")
        return
    for tr in soup.children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
 
def printUnivList(ulist, num):
    if len(ulist) == 0:
        return
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
     
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20) # 20 univs

    
main()
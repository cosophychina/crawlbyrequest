#crawltaobaosales
# -*- coding: UTF-8 -*-

from myrequests import MyRequest
import re

def getHtmlText(url):
	return MyRequest().getUrlHtml(url, limitLen = False)

def parsePage(dlist, html):
	try:
		plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
		tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
		#llt = re.findall(r'\"item_loc\"\:\".*?\"', html)
		slt = re.findall(r'\"view_sales\"\:\".*?\"', html)
		for i in range(len(plt)):
			price = eval(plt[i].split(':')[1])
			title = eval(tlt[i].split(':')[1])
			#loc = eval(llt[i].split(':')[1])
			sales = eval(slt[i].split(':')[1])
			dlist.append([price, sales, title])

	except Exception as e:
		print(e)

def printGoodsList(dlist):
	tplt = "{0:4}\t{1:8}\t{2:10}\t{3:16}"
	print(tplt.format("序号", "价格", "销售量", "商品名称"))
	count = 0
	for g in dlist:
		count = count + 1
		print(tplt.format(count, g[0], g[1], g[2]))

def main():
	goods = "避孕套"
	pageDepth = 1
	start_url = 'https://s.taobao.com/search?q=' + goods + '&sort=sale-desc'
	goodsList = []
	for i in range(pageDepth):
		try:
			url = start_url + '&s=' +str(i * 44)
			html = getHtmlText(url)
			parsePage(goodsList, html)
		except:
			print("error occured.")
			continue;
	printGoodsList(goodsList)

main()

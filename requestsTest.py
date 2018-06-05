import myrequests
from myrequests import MyRequest




if __name__ == '__main__':
	url ='http://www.runoob.com/wp-content/uploads/2013/11/if-condition.jpg'
	req = MyRequest()
	# kv = {'wd': 'python'}
	# respText = req.getUrlHtml('http://www.baidu.com/s', params = kv)
	# if req.ifSuccess():
	# 	print(respText)
	# else:
	# 	print(req.getErrorInfo())
	req.downloadPicture(url)
	if req.ifSuccess():
		print("picture downloaded..")
	else:
		print(req.getErrorInfo())


def crawUnivRanking():
	
	pass

import requests
import os

class MyRequest(object):
	__maxlength = 5000 # maxLength to return from html response
	__timeout = 10
	__headers = {'User-Agent': 'Mazilla/5.0'}
	__success = True
	__errormessage = ""

	"""docstring for MyRequestst"""
	def __init__(self):
		super(MyRequest, self).__init__()

	def getUrlHtml(self, url, params = None, limitLen = True):
		r = self.__request('get', url, params = params)
		if self.__success:
			#print(len(r.text))
			if limitLen:
				return r.text[:self.__maxlength]
			else:
				return r.text

	def downloadPicture(self, url, path2save = None):
		r = self.__request('get', url)
		if self.__success:
			try:
				if path2save is None:
					path2save = os.getcwd()
				elif not os.path.exists(path2save):
					os.makedirs(path2save)
				if path2save[-1] != '/':
					path2save += '/'
				with open(path2save + url.split('/')[-1], 'wb') as f:
					f.write(r.content)
					f.close()
			except Exception as e:
				self.__success = False
				self.__errormessage = "Exception occured: {0}".format(type(e))
			else:
				pass

	def ifSuccess(self):
		return self.__success
	def getErrorInfo(self):
		return self.__errormessage

	def __request(self, method, url, **kwargs):
		self.__success = True
		self.__errormessage = ""
		try:
			r = requests.request(method, url, headers = self.__headers, timeout = self.__timeout, **kwargs)
			r.raise_for_status() #raise httpError if not 200
			r.encoding = r.apparent_encoding
			return r
		except requests.exceptions.HTTPError as e:
			self.__success = False
			self.__errormessage = "HttpError occured: status_code {0}".format(e.response.status_code)
		except Exception as e:
			self.__success = False
			self.__errormessage = "Exception occured: {0}".format(type(e))
		else:
			self.__success = False
'''
Created by auto_sdk on 2013-04-12 12:42:23
'''
from top.api.base import RestApi
class CaipiaoPresentItemsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.page_no = None
		self.page_size = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.caipiao.present.items.get'

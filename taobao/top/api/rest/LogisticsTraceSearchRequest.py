'''
Created by auto_sdk on 2013-04-12 12:42:23
'''
from top.api.base import RestApi
class LogisticsTraceSearchRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.seller_nick = None
		self.tid = None

	def getapiname(self):
		return 'taobao.logistics.trace.search'

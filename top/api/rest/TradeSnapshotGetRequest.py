'''
Created by auto_sdk on 2013-04-12 12:42:23
'''
from top.api.base import RestApi
class TradeSnapshotGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.tid = None

	def getapiname(self):
		return 'taobao.trade.snapshot.get'

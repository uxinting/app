'''
Created by auto_sdk on 2013-04-12 12:42:23
'''
from top.api.base import RestApi
class SimbaCreativesRecordGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.creative_ids = None
		self.nick = None

	def getapiname(self):
		return 'taobao.simba.creatives.record.get'
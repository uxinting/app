'''
Created by auto_sdk on 2013-04-12 12:42:23
'''
from top.api.base import RestApi
class LogisticsPartnersGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.goods_value = None
		self.is_need_carriage = None
		self.service_type = None
		self.source_id = None
		self.target_id = None

	def getapiname(self):
		return 'taobao.logistics.partners.get'

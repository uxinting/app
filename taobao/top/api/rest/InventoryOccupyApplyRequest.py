'''
Created by auto_sdk on 2013-04-12 12:42:23
'''
from top.api.base import RestApi
class InventoryOccupyApplyRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.biz_type = None
		self.biz_unique_code = None
		self.channel_flags = None
		self.items = None
		self.occupy_time = None
		self.occupy_type = None
		self.store_code = None

	def getapiname(self):
		return 'taobao.inventory.occupy.apply'

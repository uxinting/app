'''
Created by auto_sdk on 2013-04-12 12:42:23
'''
from top.api.base import RestApi
class FenxiaoOrderCloseRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.message = None
		self.purchase_order_id = None
		self.sub_order_ids = None

	def getapiname(self):
		return 'taobao.fenxiao.order.close'

'''
Created by auto_sdk on 2013-04-12 12:42:23
'''
from top.api.base import RestApi
class AlipayMicropayOrderUnfreezeRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.alipay_order_no = None
		self.auth_token = None
		self.memo = None

	def getapiname(self):
		return 'alipay.micropay.order.unfreeze'

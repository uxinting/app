'''
Created by auto_sdk on 2013-04-12 12:42:23
'''
from top.api.base import RestApi
class InventoryAuthorizeGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.authorize_code = None
		self.user_nick_list = None

	def getapiname(self):
		return 'taobao.inventory.authorize.get'

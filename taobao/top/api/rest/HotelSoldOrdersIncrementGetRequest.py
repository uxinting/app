'''
Created by auto_sdk on 2013-04-12 12:42:23
'''
from top.api.base import RestApi
class HotelSoldOrdersIncrementGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_modified = None
		self.need_guest = None
		self.need_message = None
		self.page_no = None
		self.page_size = None
		self.start_modified = None
		self.status = None
		self.use_has_next = None

	def getapiname(self):
		return 'taobao.hotel.sold.orders.increment.get'

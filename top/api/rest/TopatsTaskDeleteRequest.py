'''
Created by auto_sdk on 2013-04-12 12:42:23
'''
from top.api.base import RestApi
class TopatsTaskDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.task_id = None

	def getapiname(self):
		return 'taobao.topats.task.delete'

import tb
import pickle

key=pickle.load(open('key.data'))

t = tb.Trade()
res = t.getRes(appkey=key['appkey'],appSecret=key['appsecret'],sessionKey=key['sessionKey'],url=key['url'],options={'start_craeted': '2013-04-01 00:00:00'})

orders = res.get('trades').get('trade')[0].get('orders')
print orders

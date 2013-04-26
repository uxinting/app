import tb
import pickle

key=pickle.load(open('key.data'))

t = tb.Trade()
res = t.getRes(appkey=key['appkey'],appSecret=key['appsecret'],sessionKey=key['sessionKey'],url=key['url'],options={'start_craeted': '2013-04-21 00:00:00'})

trade = res.get('trades').get('trade')

orders = trade[0].get('orders').get('order')
print orders

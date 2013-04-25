import tb
import pickle

key=pickle.load(open('key.data'))

t = tb.Trade()
t.getTrades(appkey=key['appkey'],appSecret=key['appsecret'],sessionKey=key['sessionKey'],url=key['url'],options={'start_craeted': '2013-04-01 00:00:00'})

print t.getSell()

import tb
import pickle

key=pickle.load(open('key.data'))

t = tb.Trade()
t.getTrades(appkey=key['appkey'],appSecret=key['appsecret'],sessionKey=key['sessionKey'],url=key['url'])

print t.getTotalResults()
print t.getSell()

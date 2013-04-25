#-*- coding: utf-8 -*-
import top.api
import top

class Trade:
    '''used for download trades information identified by sessionKey'''
    def __init__(self):
        self.fields = 'orders, service_order'
        self.trades = None #the seller's trades set
        self.hasTrades = False #if this class has get the set
        self.sell = None #set's sell per day
        self.turnover = None #set's turnover per day
        self.cost = None #set's cost per day
        self.profit = None #set's profit per day

    def getTrades(self, appkey, appSecret, url, sessionKey, options={}):
        import time
        if options.get('start_created', None) is None:
            t = list(time.gmtime())
            t[1] = t[1] - 3
            options['start_created'] = time.strftime('%Y-%m-%d %H:%M:%S', tuple(t))

        if options.get('end_created', None) is None:
            options['end_created'] = time.strftime('%Y-%m-%d %H:%M:%S')

        try:
            req = top.api.TradesSoldGetRequest(url)
            req.set_app_info(top.appinfo(appkey, appSecret))

            req.fields = self.fields
            
            for k,v in options.items():
                if hasattr(req, k):
                    setattr(req, k, v)

            self.trades = req.getResponse(sessionKey).get('trades_sold_get_response')
            self.hasTrades = True
            return self.trades.get('trades').get('trade')
        except Exception, e:
            print e

    def getTotalResults(self):
        if self.trades is None:
            raise Exception("You havn't a trades set")
        else:
            return self.trades.get('total_results')

    def getSell(self, interval='day'):
        if self.sell is not None:
            return self.sell

        pace = 10
        if interval == 'month':
            pace = 7

        try:
            pass
        except:
            pass

    def showTrades(self):
        print self.trades

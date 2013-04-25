#-*- coding: utf-8 -*-
import top.api
import top

class Trade:
    '''used for download trades information identified by sessionKey'''
    def __init__(self):
        self.fields = 'seller_nick, buyer_nick, title, type, created, tid, seller_rate,seller_can_rate, buyer_rate,can_rate, status, payment, discount_fee, adjust_fee, post_fee, total_fee, pay_time, end_time, modified, consign_time, buyer_obtain_point_fee, point_fee, real_point_fee, received_payment, pic_path, num_iid, num, price, cod_fee, cod_status, shipping_type, receiver_name, receiver_state, receiver_city, receiver_district, receiver_address, receiver_zip, receiver_mobile, receiver_phone,seller_flag,alipay_id,alipay_no,is_lgtype,is_force_wlb,is_brand_sale,buyer_area,has_buyer_message, credit_card_fee, lg_aging_type, lg_aging, step_trade_status,step_paid_fee,mark_desc,has_yfx,yfx_fee,yfx_id,yfx_type,trade_source,send_time,orders'
        self.res = None #the seller's trades set
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

            self.res = req.getResponse(sessionKey).get('trades_sold_get_response')
            self.hasTrades = True
            return self.res.get('trades').get('trade')
        except Exception, e:
            print e

    def getTotalResults(self):
        if self.res is None:
            raise Exception("You havn't a trades set")
        else:
            return self.res.get('total_results')

    def getSell(self, interval='day'):
        if self.sell is not None:
            return self.sell

        pace = 10
        if interval == 'month':
            pace = 7

        try:
            sell = {}
            turnover = {}
            trade = self.res.get('trades').get('trade')
            for item in trade:
                if item.get('pay_time', None) is None:
                    continue
                key = item['pay_time'][:pace]
                
                try:
                    sell[key] = sell[key] + item.get('num', 1)
                    turnover[key] = turnover[key] + float(item.get('total_fee', 0))
                except:
                    sell[key] = item.get('num', 1)
                    turnover[key] = float(item.get('total_fee', 0))
            
            self.sell = sell
            self.turnover = turnover
            return self.sell
        except Exception, e:
            print e
            return None
        
    def getSellJson(self, interval='day'):
        if self.sell is None:
            self.getSell(interval)
        
        sellJson = []
        for k,v in self.sell.items():
            sellJson.append({'pay_time': k, 'sell': v})
        
        import json
        return json.dump(sellJson)
    
    def getTurnover(self, interval='day'):
        if self.turnover is not None:
            return self.turnover

        pace = 10
        if interval == 'month':
            pace = 7

        try:
            sell = {}
            turnover = {}
            trade = self.res.get('trades').get('trade')
            for item in trade:
                print item
                if item.get('pay_time', None) is None:
                    continue
                key = item['pay_time'][:pace]
                
                try:
                    sell[key] = sell[key] + item.get('num', 1)
                    turnover[key] = turnover[key] + float(item.get('total_fee', 0))
                except:
                    sell[key] = item.get('num', 1)
                    turnover[key] = float(item.get('total_fee', 0))
            
            self.sell = sell
            self.turnover = turnover
            return self.turnover
        except Exception, e:
            print e
            return None
    
    def getTurnoverJson(self, interval='day'):
        if self.turnover is None:
            self.getTurnover(interval)
        
        turnoverJson = []
        for k,v in self.turnover.items():
            turnoverJson.append({'pay_time': k, 'turnover': v})
        
        import json
        return json.dump(turnoverJson)

    def showTrades(self):
        print self.res

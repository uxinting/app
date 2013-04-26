#-*- coding: utf-8 -*-
import top.api
import top

class Trades:
    '''used for store the trade set into session'''
    
    def __init__(self, session, options):
        ''' If session is None,options must has keys include "appkey, appsecret, url, sessionKey"'''
        if session.get('trade', None) is not None:
            return
        
        try:
            appkey = options['appkey']
            appsecret = options['appsecret']
            url = options['url']
            sessionKey = options['sessionKey']
            
            #the range trades occur
            import time
            if options.get('start_created', None) is None:
                t = list(time.gmtime())
                t[1] = t[1] - 3
                options['start_created'] = time.strftime('%Y-%m-%d %H:%M:%S', tuple(t))
    
            if options.get('end_created', None) is None:
                options['end_created'] = time.strftime('%Y-%m-%d %H:%M:%S')
                
            if options.get('fields', None) is None:
                options['fields'] = 'seller_nick, buyer_nick, title, type, created, tid, seller_rate,seller_can_rate, buyer_rate,can_rate, status, payment, discount_fee, adjust_fee, post_fee, total_fee, pay_time, end_time, modified, consign_time, buyer_obtain_point_fee, point_fee, real_point_fee, received_payment, pic_path, num_iid, num, price, cod_fee, cod_status, shipping_type, receiver_name, receiver_state, receiver_city, receiver_district, receiver_address, receiver_zip, receiver_mobile, receiver_phone,seller_flag,alipay_id,alipay_no,is_lgtype,is_force_wlb,is_brand_sale,buyer_area,has_buyer_message, credit_card_fee, lg_aging_type, lg_aging, step_trade_status,step_paid_fee,mark_desc,has_yfx,yfx_fee,yfx_id,yfx_type,trade_source,send_time,orders'
                
            req = top.api.TradesSoldGetRequest(url)
            req.set_app_info(top.appinfo(appkey, appsecret))
            
            for k, v in options.items():
                if hasattr(req, k):
                    setattr(req, k, v)
            
            res = req.getResponse(sessionKey)
            session['trade'] = res.get('trades').get('trade')
            session['total_results'] = res.get('total_results')
        except:
            raise Exception("Invalid options!")
        
    def getTotalResults(self, session):
        return session.get('total_results', 0)
    
    def __getSell(self, session, interval='day'):
        pace = 10
        if interval == 'month':
            pace = 7
        
        trade = session.get('trade', None)
        if trade is None:
            return None
        
        try:
            sell = {}
            for item in trade:
                if item.get('pay_time', None) is None:
                    continue
                key = item['pay_time'][:pace]
                
                try:
                    sell[key] = sell[key] + item.get('num', 1)
                except:
                    sell[key] = item.get('num', 1)

            return sell
        except Exception, e:
            return None
        
    def getSellJson(self, session, interval='day'):
        '''interval could be "day" or "month"'''
        sell = self.__getSell(session, interval)
        
        sellJson = []
        for k,v in sell.items():
            sellJson.append({'pay_time': k, 'sell': v})
        
        import json
        return json.dumps(sellJson)
    
    def __getTurnover(self, session, interval='day'):
        pace = 10
        if interval == 'month':
            pace = 7
        
        trade = session.get('trade', None)
        if trade is None:
            return None
        
        try:
            turnover = {}
            for item in trade:
                if item.get('pay_time', None) is None:
                    continue
                key = item['pay_time'][:pace]
                
                try:
                    turnover[key] = turnover[key] + float(item.get('total_fee', 0))
                except:
                    turnover[key] = float(item.get('total_fee', 0))

            return turnover
        except Exception, e:
            return None
        
    def getTurnoverJson(self, session, interval='day'):
        '''interval could be "day" or "month"'''
        turnover = self.__getTurnover(session, interval)
        turnoverJson = []
        for k,v in turnover.items():
            turnoverJson.append({'pay_time': k, 'turnover': v})
        
        import json
        return json.dumps(turnoverJson)

class Trade:
    '''used for download trades information identified by sessionKey'''
    def __init__(self, res=None):
        self.fields = 'seller_nick, buyer_nick, title, type, created, tid, seller_rate,seller_can_rate, buyer_rate,can_rate, status, payment, discount_fee, adjust_fee, post_fee, total_fee, pay_time, end_time, modified, consign_time, buyer_obtain_point_fee, point_fee, real_point_fee, received_payment, pic_path, num_iid, num, price, cod_fee, cod_status, shipping_type, receiver_name, receiver_state, receiver_city, receiver_district, receiver_address, receiver_zip, receiver_mobile, receiver_phone,seller_flag,alipay_id,alipay_no,is_lgtype,is_force_wlb,is_brand_sale,buyer_area,has_buyer_message, credit_card_fee, lg_aging_type, lg_aging, step_trade_status,step_paid_fee,mark_desc,has_yfx,yfx_fee,yfx_id,yfx_type,trade_source,send_time,orders'
        self.res = res #the seller's trades set
        self.hasRes = False #if this class has get the set
        self.sell = None #set's sell per day
        self.turnover = None #set's turnover per day
        self.cost = None #set's cost per day
        self.profit = None #set's profit per day

    def getRes(self, appkey, appSecret, url, sessionKey, options={}):
        if self.res is not None:
            return self.res

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
            self.hasRes = True
            return self.res
        except Exception, e:
            print e

    def getTotalResults(self):
        if self.res is None:
            raise Exception("You havn't a res set")
        else:
            return self.res.get('total_results')

    def getTrade(self):
        if self.res is None:
            raise Exception("You havn't a res set")
        else:
            return self.res.get('trades').get('trade')
        
    def getOrder(self):
        if self.res is None:
            raise Exception("You havn't a res set")
        else:
            return self.res.get('trades').get('trade')[0].get('orders').get('order')

    def getSell(self, interval='day', trade=None):
        if self.sell is not None:
            return self.sell
        
        if self.res is not None:
            trade = self.res.get('trades').get('trade')
            
        if self.res is None and trade is None:
            raise Exception("You havn't a res or trade set, run getRes")

        pace = 10
        if interval == 'month':
            pace = 7

        try:
            sell = {}
            turnover = {}
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
            return None
        
    def getSellJson(self, interval='day', trade=None):
        if self.sell is None:
            self.getSell(interval, trade)
        
        sellJson = []
        for k,v in self.sell.items():
            sellJson.append({'pay_time': k, 'sell': v})
        
        import json
        return json.dumps(sellJson)
    
    def getTurnover(self, interval='day', trade=None):
        if self.turnover is not None:
            return self.turnover

        if self.res is not None:
            trade = self.get('trades').get('trade')

        if self.res is None and trade is None:
            raise Exception("You havn't a res or trade set, run getRes()")
        
        pace = 10
        if interval == 'month':
            pace = 7

        try:
            sell = {}
            turnover = {}
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
    
    def getTurnoverJson(self, interval='day', trade=None):
        if self.turnover is None:
            self.getTurnover(interval, trade)
        
        turnoverJson = []
        for k,v in self.turnover.items():
            turnoverJson.append({'pay_time': k, 'turnover': v})
        
        import json
        return json.dumps(turnoverJson)

class Buyer:
    '''buyer of seller'''
    def __init__(self, session=None):
        self.session = session
        self.trade = None
        self.buyers = None
        
    def getBuyers(self, appkey, appSecret, url, sessionKey, options={}):
        if self.session is not None:
            return self.getBuyersFromSession(self.session)
        
        res = Trade().getRes(appkey, appSecret, url, sessionKey, options)
        trade = res.get('trades').get('trade')
        
        self.trade = trade
        
        self.session = {}
        self.session['trade'] = trade
        return self.getBuyersFromSession(self.session)
    
    def getTrade(self):
        return self.trade
    
    def getBuyersFromSession(self, session=None):
        if self.session is None:
            if self.session is None:
                self.session = session
            else:
                raise Exception("You havn't a session or trades set")
        
        trade = session.get('trade', None)
        if trade is None:
            try:
                trade = session.get('res').get('trades').get('trade')
            except:
                raise Exception("session has no set avilable")
        
        buyer = {}
        for item in trade:
            key = item.get('buyer_nick', None)
            if key is None:
                continue

            info = { 'sell': 0, 'total_fee': 0, 'pay_time': ''}
            try:
                info['sell'] = info['sell'] + item.get('num', 0)
                info['total_fee'] = info['total_fee'] + float(item.get('total_fee'), 0.0)
                info['pay_time'] = item.get('pay_time', 'Wait buyer to pay')
                buyer[key] = info
            except:
                return None
        
        self.buyers = buyer
        return buyer
    
    def getBuyersJson(self, session=None):
        if session is None:
            pass
        buyers = []
        for k,v in self.buyers.items():
            info = { 'buyer_nick': k}
            for vk,vv in v.items():
                info[vk] = vv
            buyers.append(info)
        
        import json
        return json.dumps(buyers)
            
        
#-*- coding: utf-8 -*-
import top.api
import top

class Trades:
    '''used for store the trade set into session'''
    
    def __init__(self, session, options):
        ''' If session is None,options must has keys include "appkey, appsecret, url, sessionKey"'''
        if session.get('trade', None) is None:
            try:
                appkey = options['appkey']
                appsecret = options['appsecret']
                url = options['url']
                sessionKey = options['sessionKey']
                
                #the range trades occur
                import time
                if options.get('start_created', None) is None:
                    t = list(time.gmtime())
                    t[1] = t[1] - 1
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

                res = req.getResponse(sessionKey).get('trades_sold_get_response')
                session['trade'] = res.get('trades').get('trade')
                session['total_results'] = res.get('total_results')
                session['hasData'] = True
            except Exception, e:
                raise Exception(repr(e))
        self.session = session
        
    def getTotalResults(self): 
        return self.session.get('total_results', 0)
    
    def __getSell(self, interval='day'):
        pace = 10
        if interval == 'month':
            pace = 7
        
        trade = self.session.get('trade', None)
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
        except:
            return None
        
    def getSellJson(self, interval='day'):
        '''interval could be "day" or "month"'''
        sell = self.__getSell(interval)
        
        sellJson = []
        for k,v in sell.items():
            sellJson.append({'pay_time': k, 'sell': v})
        
        import json
        return json.dumps(sellJson)
    
    def __getTurnover(self, interval='day'):
        pace = 10
        if interval == 'month':
            pace = 7
        
        trade = self.session.get('trade', None)
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
        except:
            return None
        
    def getTurnoverJson(self, interval='day'):
        '''interval could be "day" or "month"'''
        turnover = self.__getTurnover(interval)
        turnoverJson = []
        for k,v in turnover.items():
            turnoverJson.append({'pay_time': k, 'turnover': v})
        
        import json
        return json.dumps(turnoverJson)

class Buyers:
    '''seller 's buyers'''
    def __init__(self, session, options):
        ''' If session is None,options must has keys include "appkey, appsecret, url, sessionKey"'''
        if session.get('trade', None) is None:
            Trades(session=session, options=options)
            
        self.session = session
    
    def __getBuyer(self):
        trade = self.session.get('trade', None)
        
        buyer = {}
        for item in trade:
            key = item.get('buyer_nick', None)
            if key is None:
                continue

            if buyer.get(key, None) is None:
                buyer[key] = { 'sell': 0, 'total_fee': 0}
                
            info = buyer[key]
            try:
                info['sell'] = info['sell'] + item.get('num', 0)
                info['total_fee'] = info['total_fee'] + float(item.get('total_fee', 0.0))
            except:
                return None
        return buyer
    
    def getBuyerJson(self):
        buyer = self.__getBuyer()
        
        buyers = []
        for k,v in buyer.items():
            info = { 'buyer_nick': k}
            for vk,vv in v.items():
                info[vk] = vv
            buyers.append(info)

        import json
        return json.dumps(buyers)
            
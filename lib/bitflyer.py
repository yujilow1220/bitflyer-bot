import pybitflyer
import os

def buy(currency='BTC', price=0):
    api = pybitflyer.API(api_key=os.env['BITFLYER_API_KEY'], api_secret=os.env['BITFLYER_API_SECRET'])
    api.sendchildorder(product_code="%s_JPY" % currency,
                   child_order_type="MARKET",
                   side="BUY",
                   size=jpy_to_size(currency, price),
                   minute_to_expire=10000,
                   time_in_force="GTC"
                   )

    return

def jpy_to_size(currency, price):
    api = pybitflyer.API()
    ticker =  api.ticker(product_code="%s_JPY" % currency)
    return price / ticker['best_bid']


jpy_to_size("BTC", 1000)
    

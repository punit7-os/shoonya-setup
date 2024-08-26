from NorenRestApiPy.NorenApi import  NorenApi
import pandas as pd
import logging 
import pyotp
import json

#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

class ShoonyaApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='https://api.shoonya.com/NorenWClientTP/', websocket='wss://api.shoonya.com/NorenWSTP/')        
        global api
        api = self
api = ShoonyaApiPy()
token = 'XXXXXXXXXXX'
otp = pyotp.TOTP(token).now()     
user    = 'XXXXXXXX'
pwd     = 'XXXXXX'
factor2 = otp
vc      = 'XXXXXXX'
app_key = 'XXXXXXXXXXXXX'
imei    = 'XXXXXXXXX'   

#make the api call
ret = api.login(userid=user, password=pwd, twoFA=otp, vendor_code=vc, api_secret=app_key, imei=imei)
a = api.get_limits()


# print('''Cash is:''',a["cash"],"Rupees")
import time
from datetime import datetime

buy_time = '10:00:00'  # Market open time (Eastern Time)
sell_time = '15:00:00'  # Close a few minutes before market close (Eastern Time)
current_time = datetime.now().strftime('%H:%M:%S')
print(current_time)


while True:
    current_time = datetime.now().strftime('%H:%M:%S')
    
    if current_time == buy_time:
        ret = api.place_order(buy_or_sell='B', product_type='I',
                        exchange='NSE', tradingsymbol='IDFC-EQ', 
                        quantity=15, discloseqty=0,price_type='MKT', price=0, trigger_price=None,
                        retention='DAY', remarks='my_order_001')
        ret
        print("Buy order is placed" + current_time)
        
    if current_time == sell_time:
        ret = api.place_order(buy_or_sell='B', product_type='I',
                        exchange='NSE', tradingsymbol='IDFC-EQ', 
                        quantity=15, discloseqty=0,price_type='MKT', price=0, trigger_price=None,
                        retention='DAY', remarks='my_order_001')
        ret
       
        print("Sell Order is also placed" + current_time)
        break
    
    time.sleep(1) 
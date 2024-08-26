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
token = '42N7D5SX4M7TDL2ODQ5B5TU7XN65PJ77'
otp = pyotp.TOTP(token).now()     
user    = 'FA155856'
pwd     = 'Fin@01Fin'
factor2 = otp
vc      = 'FA155856_U'
app_key = '172af09764b8507292751366d3edc828'
imei    = 'abc1234'   

#make the api call
ret = api.login(userid=user, password=pwd, twoFA=otp, vendor_code=vc, api_secret=app_key, imei=imei)
a = api.get_limits()


# print('''Cash is:''',a["cash"],"Rupees")
import time
from datetime import datetime
import pytz

# Define IST timezone
ist = pytz.timezone('Asia/Kolkata')
_current_time = datetime.now(ist).strftime('%H:%M:%S')

print(_current_time)

# Market times in IST
buy_time = '09:16:00'  # Buy time in IST
sell_time = '12:00:00'  # Sell time in IST

while True:
    # Get the current time in IST and format it as HH:MM:SS
    current_time = datetime.now(ist).strftime('%H:%M:%S')

    if current_time == buy_time:
        ret = api.place_order(buy_or_sell='B', product_type='I',
                              exchange='NSE', tradingsymbol='IDFC-EQ',
                              quantity=15, discloseqty=0, price_type='MKT', price=0, trigger_price=None,
                              retention='DAY', remarks='my_order_001')
        ret
        print("Buy order is placed at " + current_time)

    if current_time == sell_time:
        ret = api.place_order(buy_or_sell='S', product_type='I',
                              exchange='NSE', tradingsymbol='IDFC-EQ',
                              quantity=15, discloseqty=0, price_type='MKT', price=0, trigger_price=None,
                              retention='DAY', remarks='my_order_001')
        ret
        print("Sell order is also placed at " + current_time)
        break

    time.sleep(1)


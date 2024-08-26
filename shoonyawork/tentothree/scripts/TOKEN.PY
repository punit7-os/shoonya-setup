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

SWT = api.searchscrip(exchange='NSE', searchtext='IDBI')
print(SWT)

# ket = api.get_time_price_series(exchange='NSE', token='1476', starttime=starttime, interval=5)
import datetime
lastBusDay = datetime.datetime.today()
lastBusDay = lastBusDay.replace(hour=0, minute=0, second=0, microsecond=0)
ket = api.get_time_price_series(exchange='NSE', token='1476', starttime=lastBusDay.timestamp(), interval=5)
print(ket)
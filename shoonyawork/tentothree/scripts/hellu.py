
# # def main():
# #     print("We did it!")
# #     print(1+3)

# # if __name__ == "__main__":
# #     main()

# from datetime import datetime
# current_time = datetime.now().strftime('%H:%M:%S')
# print(current_time)

# import time
# from datetime import datetime
# buy_time = '00:05:30'  # Market open time (Eastern Time)
# sell_time = '00:05:35'  # Close a few minutes before market close (Eastern Time)



# while True:
#     current_time = datetime.now().strftime('%H:%M:%S')
    
#     if current_time == buy_time:
#         print("Yeah I'm Working Yoo" + current_time)
        
#     if current_time == sell_time:
       
#         print("Yeah I'm Working" + current_time)
#         break
    
#     time.sleep(1) 

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
pwd     = 'Sho07Fin@01'
factor2 = otp
vc      = 'FA155856_U'
app_key = '172af09764b8507292751366d3edc828'
imei    = 'abc1234'   

#make the api call
ret = api.login(userid=user, password=pwd, twoFA=otp, vendor_code=vc, api_secret=app_key, imei=imei)
a = api.get_limits()

print(a)
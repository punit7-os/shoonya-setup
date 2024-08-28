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

# SWT = api.searchscrip(exchange='NSE', searchtext='IDBI-EQ')
# print(SWT)

# ket = api.get_time_price_series(exchange='NSE', token='1476', starttime=starttime, interval=5)
# import datetime
# lastBusDay = datetime.datetime.today()
# lastBusDay = lastBusDay.replace(hour=0, minute=0, second=0, microsecond=0)
# ket = api.get_time_price_series(exchange='NSE', token='1476', starttime=lastBusDay.timestamp(), interval=5)
# print(ket)
import time
import datetime
from datetime import datetime as dt
import pytz

# Define IST timezone
ist = pytz.timezone('Asia/Kolkata')

# Market times in IST
buy_time = '13:30:55'  # Buy time in IST
sell_time = '13:32:00'  # Sell time in IST

# Initialize variables to store order numbers
buy_order_number = None
stop_loss_order_number = None
sell_order_number = None

while True:
    # Get the current time in IST and format it as HH:MM:SS
    current_time = dt.now(ist).strftime('%H:%M:%S')
    print(f"Current time: {current_time}")

    if current_time == buy_time:
        # Set the start time as the beginning of the day
        last_bus_day = dt.today().replace(hour=0, minute=0, second=0, microsecond=0)
        starttime = last_bus_day.timestamp()
        
        # Retrieve the latest price series data using token 1476
        try:
            ret = api.get_time_price_series(exchange='NSE', token='1476', starttime=starttime, interval=1)
            print(f"Full API Response: {ret}")  # Print the full response for debugging
            
            if ret and isinstance(ret, list) and len(ret) > 0 and 'into' in ret[-1]:
                # Get the current market price from the latest data point
                current_market_price = float(ret[-1]['into'])
                
                # Calculate trigger price as 1% below current market price
                trigger_price = round(0.99 * current_market_price, 2)
                
                # Calculate stop-loss price as 1.1% below current market price
                stop_loss_price = round(0.989 * current_market_price, 2)

                # Place the buy order with quantity set to 5
                ret_buy = api.place_order(buy_or_sell='B', product_type='I',
                                          exchange='NSE', tradingsymbol='IDBI-EQ',
                                          quantity=5, discloseqty=0, price_type='MKT', price=0, trigger_price=None,
                                          retention='DAY', remarks='my_order_001')
                
                if ret_buy['stat'] == 'Ok':  # Check if the buy order was successfully placed
                    buy_order_number = ret_buy['norenordno']
                    print(f"Buy order is placed at {current_time} with market price {current_market_price}")

                    # Place the stop-loss order with quantity set to 5
                    ret_sl = api.place_order(buy_or_sell='S', product_type='I',
                                             exchange='NSE', tradingsymbol='IDBI-EQ',
                                             quantity=5, discloseqty=0, price_type='SL-LMT', price=stop_loss_price, 
                                             trigger_price=trigger_price,
                                             retention='DAY', remarks='my_stoploss_order_001')
                    if ret_sl['stat'] == 'Ok':
                        stop_loss_order_number = ret_sl['norenordno']
                        print(f"Stop-loss order placed with stop-loss price {stop_loss_price} and trigger price {trigger_price}")
                    else:
                        print(f"Stop-loss order failed: {ret_sl.get('emsg', 'Unknown error')}.")
                else:
                    print(f"Buy order failed: {ret_buy.get('emsg', 'Unknown error')}. Stop-loss order not placed.")
            else:
                print("No valid price data found or 'price' key is missing.")
        
        except Exception as e:
            print(f"An error occurred while retrieving price data: {e}")

    if current_time == sell_time:
        # Place the sell order with quantity set to 5
        ret_sell = api.place_order(buy_or_sell='S', product_type='I',
                                   exchange='NSE', tradingsymbol='IDBI-EQ',
                                   quantity=5, discloseqty=0, price_type='MKT', price=0, trigger_price=None,
                                   retention='DAY', remarks='my_order_001')
        if ret_sell['stat'] == 'Ok':
            sell_order_number = ret_sell['norenordno']
            print(f"Sell order is placed at {current_time}")

            # Cancel the stop-loss order if it exists
            if stop_loss_order_number:
                ret_cancel_sl = api.cancel_order(orderno=stop_loss_order_number)
                if ret_cancel_sl['stat'] == 'Ok':
                    print(f"Stop-loss order with number {stop_loss_order_number} is canceled.")
                else:
                    print(f"Failed to cancel stop-loss order: {ret_cancel_sl.get('emsg', 'Unknown error')}.")
        else:
            print(f"Sell order failed: {ret_sell.get('emsg', 'Unknown error')}.")

        break

    # Check if the stop-loss order has executed
    if stop_loss_order_number:
        # (Placeholder) Implement logic to check if stop-loss order has executed
        # For demonstration, you would normally check the status of the stop-loss order here
        stop_loss_executed = True  # Replace with actual check

        if stop_loss_executed:
            # Cancel the sell order if it exists
            if sell_order_number:
                ret_cancel_sell = api.cancel_order(orderno=sell_order_number)
                if ret_cancel_sell['stat'] == 'Ok':
                    print(f"Sell order with number {sell_order_number} is canceled.")
                else:
                    print(f"Failed to cancel sell order: {ret_cancel_sell.get('emsg', 'Unknown error')}.")
            break

    time.sleep(1)


# def main():
#     print("We did it!")
#     print(1+3)

# if __name__ == "__main__":
#     main()

from datetime import datetime
current_time = datetime.now().strftime('%H:%M:%S')
print(current_time)

import time
from datetime import datetime
buy_time = '00:05:30'  # Market open time (Eastern Time)
sell_time = '00:05:35'  # Close a few minutes before market close (Eastern Time)



while True:
    current_time = datetime.now().strftime('%H:%M:%S')
    
    if current_time == buy_time:
        print("Yeah I'm Working Yoo" + current_time)
        
    if current_time == sell_time:
       
        print("Yeah I'm Working" + current_time)
        break
    
    time.sleep(1) 
import time
from datetime import date

today = date.today()
print("Today's date:", str(today).replace('-',''))
time1=time.time()
#time.sleep(2)
time2=time.time()
time_dff=time2-time1
print (print('%.2f' % (time2-time1) ))




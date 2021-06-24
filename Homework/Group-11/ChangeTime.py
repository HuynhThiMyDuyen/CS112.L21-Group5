from datetime import datetime

time = input()
try:
    time_24 = datetime.strptime(time, '%I:%M:%S%p')
    print(time_24.time())
except:
    print("Error")
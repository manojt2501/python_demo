import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print('hello Manoj! wow great it works')
print(current_time)
time.sleep(10)
print(current_time)
print('after 10 seconds')

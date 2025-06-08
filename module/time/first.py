import time
# print(4)
# time.sleep(5)
# print("This is printed after 5 second")

print(time.ctime(0))
start=time.perf_counter()
r=time.localtime()
formated_time=time.strftime("%Y-%m-%d %H:%M:%S",r)
print(formated_time)
end=time.perf_counter()
print(f"time taken:{end-start} second")
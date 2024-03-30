import time 

# print(time.ctime()) # convert a time expressed in seconds since spach to readable string
# #                      epach = when your computer thinks time began( reference point)

# print(time.time()) # return current second since epach

# print(time.ctime(time.time()))

# time_object = time.localtime()
# print(time_object)
# local_time = time.strftime("%B %d %Y %H:%S",time_object)
# print(local_time)


# (year , month ,day , hours ,minutes , secs , # day of the week ,# day of the year, dst)
time_tuple = (2020 , 3, 30 , 22, 34, 43, 0, 0 , 0)
time_string = time.asctime(time_tuple)
print(time_string)
#********************************************** 
# Python Multiprocessing
#**********************************************
# multiprocessing = running task in parallel on different cpu corces , typesses  GIL used for thread
#                   multiprocessing = better for cpu bound task (heavy cpu usage )     
#                   multithreading = better for to bound tasks ( waiting around)
from multiprocessing import Process , cpu_count
import time 
# 
#
def counter(num):
    count = 0 
    while count < num:
        count += 1




def main():
    a = property(target=counter,args = (1000000000,))
    b = property(target=counter,args = (1000000000,))
    b.start()
    b.start()
    
    a.join()
    b.join()
    print("finished in ",time.perf_counter(),"seconds")




if __name__ == '__main__':
    main()
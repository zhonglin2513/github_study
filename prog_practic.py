# with open('d:/Python/Git_repo_Python/Python_Practic/output.txt','w') as f:
#     for i in range(10):
#         f.write(f'Hello, Python!{i}\n')
   
# with open('d:/Python/Git_repo_Python/Python_Practic/output.txt','r') as f:
#     print(f.read())

# import ctypes
# import mmap 
# import os
# import numpy as np 
# import struct

# x=ctypes.c_uint(123)
# addr=ctypes.addressof(x)
# print(f'address of x:{hex(addr)}')

# ptr=ctypes.cast(addr, ctypes.POINTER(ctypes.c_int))
# print(f'the original value of x:{ptr.contents.value}')
# ptr.contents.value=456
# print(f'the new value of x:{ptr.contents.value}')
# # The address of x:0x7ffdfb8c4a10
# # The original value of x:123
# # The new value of x:456

# filePath=os.path.join(os.path.abspath('.'),'test.bin')
# with open(filePath,'wb') as f: 
#     f.write(b'\x00' *1024)  # Create a file with 1KB of zero bytes

# with open(filePath,'r+b') as f:
#     mm=mmap.mmap(f.fileno(), 0)  # Memory-map the file, size 0 means whole file
#     mm[0:4]=b'\x01\x02\x03\x04'  # Write some bytes to the memory-mapped file
#     mm.flush()  # Ensure changes are written to disk
#     mm.close()  # Close the memory-mapped file

# # with open(filePath,'rb') as f:
# #     print(f.read())

# buf=np.zeros(10,dtype=np.uint8)
# buf[0]=255
# print(buf.tobytes())


# data=struct.pack('<I', 12345678)
# print(data)  # b'4\x16\x00\x00'
# value=struct.unpack('<I',data)[0]
# print(value)  # 12345678

# import json
# class Student(object):
#     def __init__(self, name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score 

# s=Student('Bob', 20, 88)
# print(json.dumps(s))

from multiprocessing import Process
import os 

# print ('process(%s) started....' % os.getpid())
# pid = os.fork()
# if pid==0:
#     print('I am child process (%s) and my parent is (%s).' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# os._exit(0)

# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')
# from multiprocessing import Process, Lock
# import math, time

# def dummy():
#     pass 

# def calc():
#     for _ in range(10**4):
#         with open('d:/Python/Git_repo_Python/Python_Practic/calc.txt', 'a') as f:
#             f.write(str(math.sqrt(12345)))

# def calc1(n,lock):
#     for _ in range(n):
#         with lock:
#             with open('d:/Python/Git_repo_Python/Python_Practic/calc1.txt', 'a') as f:
#                 f.write(str(math.sqrt(12345)))
    
# if __name__ =='__main__':
#     print('start signal process calc...')
#     start = time.time()
#     calc()
#     end = time.time()
#     print('elapsed time: %f' % (end - start))

#     start = time.time()
#     total = 10**4
#     n_proc = 4
#     per_proc = total // n_proc
#     lock = Lock()
#     ps = [Process(target=calc1, args=(per_proc,lock)) for _ in range(n_proc)]
#     start = time.time()
#     for p in ps: p.start()
#     for p in ps: p.join()
#     print("Done in", time.time() - start)




# if __name__ =='__main__':
#     print('start signal process calc...')
#     start = time.time()
#     calc()

#     # p = Process(target=dummy) #calc start/end process time 
#     # p.start()
#     # p.join()

#     end = time.time()
#     print('elapsed time: %f' % (end - start))

#     print('start multiprocessing calc...')
#     p1 = Process(target=calc)
#     p2 = Process(target=calc)
#     p3 = Process(target=calc)
#     p4 = Process(target=calc)
#     start = time.time()
#     p1.start(); p2.start(); p3.start(); p4.start()
#     p1.join(); p2.join(); p3.join(); p4.join()
#     print("Done in", time.time() - start)

# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

# import time, threading 
# balance =0 
# def loop():
#     print('Thread %s is running...' % threading.current_thread().name)
#     n=0
#     while n< 5:
#         n=n+1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('Thread %s ended.' % threading.current_thread().name)

# print('Thread %s is running...' % threading.current_thread().name)
# t=threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('Thread %s ended.' % threading.current_thread().name)

# import  threading 
# balance =0 
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for _ in range(10000000):
#         change_it(n)

# t1=threading.Thread(target=run_thread,args=(3,))
# t2=threading.Thread(target=run_thread,args=(5,))
# t3=threading.Thread(target=run_thread,args=(8,))
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# print(balance)  # Expected output: 0, but may vary due to threading

# multithread
import time, threading

# 假定这是你的银行存款:
balance = 0

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(3,))
t2 = threading.Thread(target=run_thread, args=(5,))
t3 = threading.Thread(target=run_thread, args=(7,))
t4 = threading.Thread(target=run_thread, args=(11,))
t5 = threading.Thread(target=run_thread, args=(13,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
print(balance)























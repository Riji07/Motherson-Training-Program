# from multiprocessing import Process
# my_numbers = [3, 4, 5, 6, 7, 8]
# def cube(x):
#    for x in my_numbers:
#         print('%s cube is %s' % (x, x**3))
# def evenno(x):
#    for x in my_numbers:
#     if x % 2 == 0:
#         print('%s is an even number ' % (x))


# if __name__ == '__main__':
#     my_numbers = [3, 4, 5, 6, 7, 8]
#     my_process1 = Process(target=cube, args=('x',))
#     my_process2 = Process(target=evenno, args=('x',))
#     my_process1.start()
#     my_process2.start()
#     my_process1.join()
#     my_process2.join() 
#     print ("Done")  


# from multiprocessing import Process
# def display():
#     print ('Hi !! I am Python')
# if __name__ == '__main__':
#     p = Process(target=display)
#     p.start()
#     p.join()
#     print("Done")


# from multiprocessing import Process
# def display(my_name):
#     print ('Hi !!!' + " " + my_name)
# if __name__ == '__main__':
#     p = Process(target=display, args=('Python',))
#     p.start()
#     p.join()
#     print("Done")


# from multiprocessing import Process
# my_numbers = [3, 4, 5, 6, 7, 8]
# def cube(x):
#     for x in my_numbers:
#         print('%s cube is %s' % (x, x**3))
# if __name__ == '__main__':
#         my_numbers = [3, 4, 5, 6, 7, 8]
#         p = Process(target=cube, args=('x',))
#         p.start()
#         p.join
#         print ("Done")


# from multiprocessing import Process, Pipe
# def myfunction(conn):
#     conn.send(['hi!! I am Python'])
#     conn.close()
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=myfunction, args=(child_conn,))
#     p.start()
#     print (parent_conn.recv() )
#     p.join() #pipe


#Queues
# import multiprocessing
# def evenno(numbers, q):
#     for n in numbers:
#         if n % 2 == 0:
#             q.put(n)
# if __name__ == "__main__":
#             q = multiprocessing.Queue()
#             p = multiprocessing.Process(target=evenno, args=(range(10), q))
#             p.start()
#             p.join()
# while q:
#             print(q.get())


# from multiprocessing import Process, Lock
# def dispmay_name(l, i):
#     l.acquire()
#     print ('Hi', i)
#     l.release()
# if __name__ == '__main__':
#     my_lock = Lock()
#     my_name = ['Aadrika', 'Adwaita', 'Sakya', 'Sanj']
# for name in my_name:
#     Process(target=dispmay_name, args=(my_lock,name)).start()


# import multiprocessing, logging
# logger = multiprocessing.log_to_stderr()
# logger.setLevel(logging.INFO)
# logger.warning('Error has occurred')


# import time
# from multiprocessing import Process
# def cube(x):
#     print(f"start process {x}")
#     print(x * x * x)
#     time.sleep(1)
#     print(f"end process {x}")
# if __name__ == "__main__":
#     processes = []
#     for i in range(10):
#         p = Process(target=cube, args=(i,))
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()


# from multiprocessing import Process, Pipe
# def cube_sender(x, x_conn):
#     x_conn.send(x * x * x)
# def cube_receiver(y_conn):
#     print(y_conn.recv())
# if __name__ == "__main__":
#     x_conn, y_conn = Pipe()
#     processes = []

#     p1 = Process(
#         target=cube_sender,
#         args=(
#             19,
#             x_conn,
#         ),
#     )

#     p2 = Process(target=cube_receiver,args=(y_conn,),)

#     processes.extend([p1, p2])

#     for p in processes:
#         p.start()

#     for p in processes:
#         p.join()


# from multiprocessing import Process, Queue
 
 
# def cube(x, q):
#     q.put(x * x * x)
 
 
# def add(x, q):
#     q.put(x + 1)
# if __name__ == "__main__":
#     q = Queue()
#     processes = []
#     for i in range(10):
#         p = Process(target=cube, args=(i, q,))
#         processes.append(p)
#         p.start()
 
#     for p in processes:
#         p.join()
 
#     processes = []
#     print("INITIAL VALUES: ")
#     while not q.empty():
#         val = q.get()
#         print(val)
#         p = Process(target=add, args=(val, q,))
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()
 
#     print("FINAL VALUES: ")
#     while not q.empty():
#         print(q.get())  


# from multiprocessing import Process, Value
# def cube(x):
#     x.value = x.value * x.value * x.value
# if __name__ == "__main__":
#     num = Value("i", 10)
#     p = Process(target=cube, args=(num,))
#     p.start()
#     p.join()
#     p = Process(target=cube, args=(num,))
#     p.start()
#     p.join()

#     print(num.value)



# from multiprocessing import Process, Array
# def cube(x):
#     for i in range(len(x)):
#         x[i] = x[i] + 1
# if __name__ == "__main__":
#     arr = Array("i", 3)
#     p = Process(target=cube, args=(arr,))
#     p.start()
#     p.join()

#     print(arr[:])


# from multiprocessing import Process, Manager
# def cube(d, l):
#     d["car"] = "ford"
#     l.sort()
# if __name__ == "__main__":
#     manager = Manager()

#     d = manager.dict()
#     l = manager.list([9, 3])

#     p = Process(
#         target=cube,
#         args=(
#             d,
#             l,
#         ),
#     )
#     p.start()
#     p.join()

#     print(d)
#     print(l)


# import time
# from multiprocessing import Pool
# def cube(x):
#     print(f"start process {x}")
#     result = x * x * x
#     time.sleep(1)
#     print(f"end process {x}")
#     return result
# if __name__ == "__main__":
#     ts = time.time()
#     pool = Pool(processes=4)
#     print([pool.apply(cube, args=(x,)) for x in range(10)])
#     pool.close()
#     pool.join()
#     print("Time in parallel:", time.time() - ts)





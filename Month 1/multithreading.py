# import threading
# def print_cube(num):
#     print("Cube:{}".format(num*num*num))
# def print_square(num):
#     print("Square:{}".format(num*num))
# if __name__ == "__main__":
#     t1=threading.Thread(target=print_square,args=(10,))
#     t2=threading.Thread(target=print_cube,args=(10,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
#     print("Done!")


# import threading
# import os
# def task1():
#     print("Task 1 assigned to thread:{}".format(threading.current_thread().name))
#     print("ID of process running task 1:{}".format(os.getpid()))
# def task2():
#     print("Task 2 is assigned to thread:{}".format(threading.current_thread().name))
#     print("ID of process running task 2:{}".format(os.getpid()))
# if __name__=="__main__":
#     print("ID of process running main program:{}".format(os.getpid()))
#     print("Main thread name:{}".format(threading.current_thread().name))
#     t1=threading.Thread(target=task1,name="t1")
#     t2=threading.Thread(target=task2,name="t2")
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()


# import threading
# x=0
# def increment():
#     global X
#     x+=1
# def thread_task():
#     for _ in range(100000):
#         increment()
# def main_task():
#     global X
#     x=0
#     t1=threading.Thread(target=thread_task)
#     t2=threading.Thread(target=thread_task)
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()
# if __name__=="__main__":
#     for i in range(10):
#         main_task()
#         print("Iteration{0}:x={1}".format(i,x))


# import threading
# x = 0
# def increment():
#  	global x
#  	x += 1
# def thread_task():
#  	for _ in range(100000):
#  		increment()
# def main_task():
#  	global x
#  	x = 0
#  	t1 = threading.Thread(target=thread_task)
#  	t2 = threading.Thread(target=thread_task)
#  	t1.start()
#  	t2.start()
#  	t1.join()
# 	t2.join()
#  if __name__ == "__main__":
#  	for i in range(10):
#  		main_task()
#  		print("Iteration {0}: x = {1}".format(i,x))




import threading
x=0
def increment():
	global x
	x += 1
def thread_task(lock):
	for _ in range(100000):
		lock.acquire()
		increment()
		lock.release()
def main_task():
	global x
	x=0
	lock=threading.Lock()
	t1=threading.Thread(target=thread_task,args=(lock,))
	t2=threading.Thread(target=thread_task,args=(lock,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
if __name__=="__main__":
	for i in range(10):
		main_task()
		print("Iteration {0}:x={1}".format(i,x))
		



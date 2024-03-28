import threading

def function1():
    for i in range(10):
        print("ONE ")

def function2():
    for i in range(10):
        print("TWO ")

def function3():
    for i in range(10):
        print("THREE ")

t1 = threading.Thread(target = function1)
t2 = threading.Thread(target = function2)
t3 = threading.Thread(target = function3)

t1.start()
t2.start()
t3.start()
from threading import Thread
from time import sleep

def work(number, name):
    print("i am {} \n and sleeping for {} seconds".format(name, number))
    sleep(float(number))

t = Thread(target = work, name='Thread1', args=('1', 'FirsT'))
t.start()
t.join()
#!/usr/bin/env python3

from threading import Thread
import time

haha = time.time()

def sleeper(number, name):
    print("I am {} \n and I am sleeping for {} seconds".format(name, number))
    time.sleep(5)
    print("{} waked up!".format(name))

thread_list = []
stream = 5
for i in range(stream): 
    t = Thread(target = sleeper, name='Thread{}'.format(str(i)), args=(5, 'Thread{}'.format(str(i))))

    thread_list.append(t)
    t.start()
    print("Module {} started.".format(t.name)) # NOTE: interesting


# INFO: без данного куска выполнения, программа продолжит свое проживание на 25 строке и закончит комплирование
# NOTE: следует написать t.join() для ожидания окончания работы всех ядер
for k in thread_list:
    t.join()

print("Time taken {} ".format(time.time() - haha))

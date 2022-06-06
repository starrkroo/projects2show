#!/usr/bin/env python3

import threading
import time

def sleeper(n, name):
  print("Привет, я {}. Собираюсь поспать.".format(name))
  time.sleep(n)
  print("{} проснулся.".format(name))

t = threading.Thread(target=sleeper, name='Thread1', args=(5, 'Thread1'))

thread_list = []

start = time.time()

stream = 5
for i in range(stream):
  t = threading.Thread(
      target=sleeper,
      name  ='Thread{}'.format(str(i)),
      args  = (5, "Thread{}".format(str(i))
    ))

	# добавление потока в массив
  thread_list.append(t)
  print(thread_list)
# запуск текущего (итого) потока
  t.start()
  print("{} has started".format(t.name))

# подключение к работе функции по ее завершение
# ---> функция завершила работу - напечатал текст
for t in thread_list:
  # итерация по массиву для выполнение дочерниго выполнения алгоритма
  t.join() # ждем завершения всех потоков

print("Time taken: {}".format(time.time() - start))

print("All threads done.")

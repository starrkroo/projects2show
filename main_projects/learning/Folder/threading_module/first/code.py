import threading
import time

def sleeper(n, name):
	print("Привет, я {}. Собираюсь поспать.".format(name))
	time.sleep(n)
	print("{} проснулся.".format(name))

# threading.Thread(function_for_threaging, name_of_process, args_of_current_function)
t = threading.Thread(target=sleeper, name='Thread1', args=(5, 'Thread1'))

# starts
t.start()

# ждать исполнение всех дочерних потоков (по возврастанию(вниз))
# u can try to remove this line, than line: 21 will work in time with compiling this code :D
t.join()

# запускается новый поток, сперва считывается весь код

print('Hello!')

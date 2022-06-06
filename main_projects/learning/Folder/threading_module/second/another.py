import threading
import time

def sleeper(n, name):
	print("Привет, я {}. Собираюсь поспать.".format(name))
	time.sleep(n)
	print("{} проснулся.".format(name))

start = time.time()
for i in range(5):
	sleeper(5, i)
print("Time taken {}".format(time.time() - start))
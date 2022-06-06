import time
timestr = time.strftime("%d%m%Y%I%M%S")

with open(str(timestr+".txt"), 'w') as f:
	f.write("file with current time")
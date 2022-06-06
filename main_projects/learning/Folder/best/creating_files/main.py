from os import mkdir, listdir, chdir

data = 'data'

try:
    mkdir(data)
    chdir(data)
except:
    chdir(data)

x = listdir()
try:
    x = max(x)
    print(x)
except:
    pass

for k in range(1,10):

    if str(k) in x:
        with open('hello_' + str(int(k+1)) + '.txt', 'w') as f:
            f.write('hello world')

    else:
        with open('hello_1.txt', 'w') as f:
            f.write('hello another world')






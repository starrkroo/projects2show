import json

items = {
	'Linux': "Is operation system",
	'OSs'  : ['Ubuntu', "Kali", 'Mint'],
	'Name' : 'idk',
	"Number": 1990
}

some = json.dumps(items)
print(some)

with open('file.txt', 'w') as f:
	f.write(json.dumps(some))





##############################################################
with open('file.txt') as f:
	some = f.read()
print(json.loads(some))
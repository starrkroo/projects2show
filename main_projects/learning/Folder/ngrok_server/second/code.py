#!/usr/bin/env python3

from os import system
from time import sleep
import re
from subprocess import check_output

RED, WHITE, CYAN, GREEN, DEFAULT = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m'

def runNgrok():
  system('./Server/ngrok http 1111 > /dev/null &')
  while True:
    sleep(2)
    system('curl -s -N http://127.0.0.1:4040/status | grep "https://[0-9a-z]*\.ngrok.io" -oh > ngrok.url')
    urlFile = open('ngrok.url', 'r')
    url = urlFile.read()
    urlFile.close()
    if re.match("https://[0-9a-z]*\.ngrok.io", url) != None:
      print("\n {0}[{1}*{0}]{1} Ngrok URL: {2}".format(CYAN, DEFAULT, GREEN) + url + "{1}".format(CYAN, DEFAULT, GREEN))
      link = check_output("curl -s 'http://tinyurl.com/api-create.php?url='"+url, shell=True).decode().replace('http', 'https')
      print("\n {0}[{1}*{0}]{1} TINYURL: {2}".format(CYAN, DEFAULT, GREEN) + link + "{1}".format(CYAN, DEFAULT, GREEN))
      print("\n")
      break

if __name__ == '__main__':
    runNgrok()

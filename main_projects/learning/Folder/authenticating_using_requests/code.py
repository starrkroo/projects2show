#!/usr/bin/env python3

import requests
import lxml.html

"""
SOURCE: 
	https://ru.stackoverflow.com/questions/468378/Авторизация-в-vk-с-помощью-requests
	https://stackoverflow.com/questions/9548729/how-to-authenticate-a-site-with-python-using-urllib2
"""

login = '89894715441'
password = 'starrk0909100'
url = 'https://vk.com/'

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}

session = requests.session()
data = session.get(url, headers = headers)
page = lxml.html.fromstring(data.content)

form = page.forms[0]
form.fields['email'] = login
form.fields['pass'] = password

response = session.post(form.action, data=form.form_values())

print('onLoginDone' in response.text)

r2 = session.get('https://vk.com/im')

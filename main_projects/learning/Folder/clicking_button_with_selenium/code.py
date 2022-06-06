#!/usr/bin/env python3

from selenium import webdriver

# NOTE: source to install phantomJS: https://www.programsbuzz.com/post/how-install-phantomjs-ubuntu-1804-lts

driver = webdriver.PhantomJS()#('/usr/lib/chromium-browser/chromedriver')

driver.get('https://google.com')
button = driver.find_element_by_css_selector("input.gNO89b")
query = driver.find_element_by_css_selector('input.gLFyf')
query.send_keys('who you are?')
button.click()
driver.save_screen('screen.png')
# username.send_keys('#Login')
# password = driver.find_element_by_css_selector("input#password")
# password.click()
# password.send_keys('11111')
# submit = driver.find_element_by_css_selector("input#kc-login")
# submit.click()
# time.sleep(3)
# activate_btn = driver.find_element_by_xpath(activate_xpath)

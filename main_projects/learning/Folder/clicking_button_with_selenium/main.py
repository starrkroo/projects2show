
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


# prepare the option for the chrome driver
# start chrome browser
driver = webdriver.Chrome("C:\\webdrivers\\chromedriver.exe")
driver.get('https://google.com')
driver.implicitly_wait(5)

query = driver.find_element_by_class_name('gLFyf')
query.send_keys('shit what is going on?')

driver.find_element_by_css_selector('.gNO89b').click()
print(driver.current_url)
driver.quit()

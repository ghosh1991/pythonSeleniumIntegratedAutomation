import time

from selenium import webdriver

"""  specified Chrome driver path in Local environment  """
driver = webdriver.Chrome("C:\\Users\\ratul\\Downloads\\chromedriver_win32\\chromedriver.exe")

driver.get('http://www.google.de/')

"""  Screen will be displayed for 5 sec  """
time.sleep(5)

search_box = driver.find_element_by_name('q')
search_box.send_keys('relayr')
search_box.submit()

time.sleep(5)
driver.quit()

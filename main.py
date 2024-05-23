from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--remote-debugging-port=9222')

driver = webdriver.Chrome(options=options)
driver.get('http://www.google.com')
print(driver.title)
driver.quit()

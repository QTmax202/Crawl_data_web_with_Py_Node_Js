from selenium import webdriver

# driver = webdriver.Chrome(executable_path='/path/to/chromedriver')
driver = webdriver.Chrome()
# driver.get(f'https://ebank.mbbank.com.vn/cp/pl/login?returnUrl=%2F')
driver.get(f'https://ebank.mbbank.com.vn/cp/pl/login')
title = driver.title
print(title)
element = driver.get_screenshot_as_base64
print(element)
# data = element.text
# print(data)
# driver.close()

# Extract data from the webpage using Selenium

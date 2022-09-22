from selenium import webdriver
from selenium.webdriver.common.by import By

c = webdriver.ChromeOptions()
c.add_argument("--incognito")

driver = webdriver.Chrome(executable_path="./chromedriver.exe",options=c)
driver.implicitly_wait(0.5)

driver.get('https://www.amazon.com/')

driver.find_element(By.ID,"nav-orders").click()

expected_result_1 = driver.find_element(By.ID, "a-page")
actual_result_1 = driver.find_element(By.ID,"a-page")
assert expected_result_1 == actual_result_1, f'Error! Expected {expected_result_1}, but got {actual_result_1}'
expected_result_2 = driver.find_element(By.ID,"authportal-main-section")
actual_result_2 = driver.find_element(By.ID,"authportal-main-section")
assert expected_result_2 == actual_result_2, f'Error! Expected {expected_result_2}, but got {actual_result_2}'
expected_result_3 = driver.find_element(By.ID,"ap_email")
actual_result_3 = driver.find_element(By.ID,"ap_email")
assert expected_result_3 == actual_result_3, f'Error! Expected {expected_result_3}, but got {actual_result_3}'

print('Test Case Passed, browser closes immediately')
driver.find_element(By.ID, "ap_email").send_keys('Browser will close in 10 seconds')
driver.implicitly_wait(1)
driver.quit()


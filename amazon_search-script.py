from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

c = webdriver.ChromeOptions()
c.add_argument("--incognito")

driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=c)
driver.implicitly_wait(0.5)
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, "nav-orders").click()

sleep(2)

driver.find_element(By.ID, "a-page")

expected_result_2 = 'Sign in'
actual_result_2 = driver.find_element(By.XPATH, ".//h1").text
assert expected_result_2 == actual_result_2, f'Error! Expected {expected_result_2}, but got {actual_result_2}'


driver.find_element(By.ID, "ap_email")

print('Test Case Passed, browser closes immediately')
driver.find_element(By.ID, "ap_email").send_keys('Browser will close in 10 seconds')
driver.implicitly_wait(1)
driver.quit()

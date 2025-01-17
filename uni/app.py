from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

import csv
from openpyxl import load_workbook

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
# options.add_argument("--headless")
service = Service(executable_path="C:\drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# FEDERAL
driver.get("https://www.nuc.edu.ng/nigerian-univerisities/federal-univeristies/")
dropdown = driver.find_element(By.XPATH, '//*[@id="tablepress-2_length"]/label/select').click()
wait = WebDriverWait(driver, 2)
queries = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tablepress-2_length"]/label/select/option[5]')))
display_all = driver.find_element(By.XPATH, '//*[@id="tablepress-2_length"]/label/select/option[5]').click()

for x in range(1, 52):
    no = driver.find_element(By.XPATH, '//*[@id="tablepress-2"]/tbody/tr[' +str(x)+ ']/td[1]').text
    uni_name = driver.find_element(By.XPATH, '//*[@id="tablepress-2"]/tbody/tr[' +str(x)+ ']/td[2]').text
    
    detail_tup = (no, uni_name)
    print(detail_tup)
    
    f = open('universities/federal.csv', 'a', newline='')
    writer = csv.writer(f)
    writer.writerow(detail_tup)
    f.close()

driver.quit()

# STATE
# driver.get("https://www.nuc.edu.ng/nigerian-univerisities/state-univerisity/")
# dropdown = driver.find_element(By.XPATH, '//*[@id="tablepress-4_length"]/label/select').click()
# wait = WebDriverWait(driver, 2)
# queries = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tablepress-4_length"]/label/select/option[4]')))
# display_all = driver.find_element(By.XPATH, '//*[@id="tablepress-4_length"]/label/select/option[4]').click()

# for x in range(1, 60):
#     no = driver.find_element(By.XPATH, '//*[@id="tablepress-4"]/tbody/tr[' +str(x)+ ']/td[1]').text
#     uni_name = driver.find_element(By.XPATH, '//*[@id="tablepress-4"]/tbody/tr[' +str(x)+ ']/td[2]').text
    
#     detail_tup = (no, uni_name)
#     print(detail_tup)
    
#     f = open('universities/state.csv', 'a', newline='')
#     writer = csv.writer(f)
#     writer.writerow(detail_tup)
#     f.close()

# driver.quit()

# PRIVATE
# driver.get("https://www.nuc.edu.ng/nigerian-univerisities/private-univeristies/")
# dropdown = driver.find_element(By.XPATH, '//*[@id="tablepress-3_length"]/label/select').click()
# wait = WebDriverWait(driver, 2)
# queries = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="tablepress-3_length"]/label/select/option[5]')))
# display_all = driver.find_element(By.XPATH, '//*[@id="tablepress-3_length"]/label/select/option[5]').click()

# for x in range(1, 101):
#     no = driver.find_element(By.XPATH, '//*[@id="tablepress-3"]/tbody/tr[' +str(x)+ ']/td[1]').text
#     uni_name = driver.find_element(By.XPATH, '//*[@id="tablepress-3"]/tbody/tr[' +str(x)+ ']/td[2]').text
    
#     detail_tup = (no, uni_name)
#     print(detail_tup)
    
#     f = open('universities/private.csv', 'a', newline='')
#     writer = csv.writer(f)
#     writer.writerow(detail_tup)
#     f.close()
    
# next = driver.find_element(By.XPATH, '//*[@id="tablepress-3_next"]').click()
# for x in range(1, 12):
#     no = driver.find_element(By.XPATH, '//*[@id="tablepress-3"]/tbody/tr[' +str(x)+ ']/td[1]').text
#     uni_name = driver.find_element(By.XPATH, '//*[@id="tablepress-3"]/tbody/tr[' +str(x)+ ']/td[2]').text
    
#     detail_tup = (no, uni_name)
#     print(detail_tup)
    
#     f = open('universities/private.csv', 'a', newline='')
#     writer = csv.writer(f)
#     writer.writerow(detail_tup)
#     f.close()
    

driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv

options = webdriver.ChromeOptions()
options.add_argument("--incognito")
# options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path="C:\drivers\chromedriver_win32\chromedriver.exe", options=options
)

# FEDERAL
# driver.get('https://net.nbte.gov.ng/Federal%20Polytechnics')
# for x in range(2, 42):
#   no = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[1]').text
#   poly_name = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[2]').text
#   # web_addr = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[4]').text
#   # year_est = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[3]').text
#   # detail_tup = (no, poly_name, '', web_addr, year_est)
#   detail_tup = (no, poly_name)
#   print(detail_tup)
  
#   f = open('technical/federal.csv', 'a', newline='')
#   writer = csv.writer(f)
#   writer.writerow(detail_tup)
#   f.close()
  
# STATE
# driver.get('https://net.nbte.gov.ng/state%20polytechnics')
# for x in range(2, 51):
#   no = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[1]').text
#   poly_name = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[2]').text
    
#   detail_tup = (no, poly_name)
#   print(detail_tup)
  
#   f = open('technical/state.csv', 'a', newline='')
#   writer = csv.writer(f)
#   writer.writerow(detail_tup)
#   f.close()
  
# PRIVATE
# driver.get('https://net.nbte.gov.ng/private%20polytechnics')
# for x in range(2, 86):
#   no = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[1]').text
#   poly_name = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[2]').text
    
#   detail_tup = (no, poly_name)
#   print(detail_tup)
  
#   f = open('technical/private.csv', 'a', newline='', encoding="utf-8")
#   writer = csv.writer(f)
#   writer.writerow(detail_tup)
#   f.close()

# SPECIALIZED INSTITUTIONS
# driver.get('https://net.nbte.gov.ng/specialised%20institutions')
# for x in range(2, 57):
#   no = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[1]').text
#   poly_name = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[2]').text
    
#   detail_tup = (no, poly_name)
#   print(detail_tup)
  
#   f = open('technical/specialized.csv', 'a', newline='', encoding="utf-8")
#   writer = csv.writer(f)
#   writer.writerow(detail_tup)
#   f.close()
  
# AGRICULTURE
# driver.get('https://net.nbte.gov.ng/colleges%20of%20agric')
# for x in range(2, 37):
#   no = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[1]').text
#   poly_name = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[2]').text
    
#   detail_tup = (no, poly_name)
#   print(detail_tup)
  
#   f = open('technical/agric.csv', 'a', newline='', encoding="utf-8")
#   writer = csv.writer(f)
#   writer.writerow(detail_tup)
#   f.close()

# PUBLIC COLLEGE OF HEALTH
# driver.get('https://net.nbte.gov.ng/public%20colleges%20of%20health')
# for x in range(2, 70):
#   no = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[1]').text
#   poly_name = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[2]').text
    
#   detail_tup = (no, poly_name)
#   print(detail_tup)
  
#   f = open('technical/public_coll_health.csv', 'a', newline='', encoding="utf-8")
#   writer = csv.writer(f)
#   writer.writerow(detail_tup)
#   f.close()

# PRIVATE COLLEGE OF HEALTH
# driver.get('https://net.nbte.gov.ng/private%20colleges%20of%20health')
# for x in range(2, 23):
#   no = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[1]').text
#   poly_name = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[2]').text
    
#   detail_tup = (no, poly_name)
#   print(detail_tup)
  
#   f = open('technical/private_coll_health.csv', 'a', newline='', encoding="utf-8")
#   writer = csv.writer(f)
#   writer.writerow(detail_tup)
#   f.close()

# # TECHNICAL COLLEGE
# driver.get('https://net.nbte.gov.ng/technical%20colleges')
# for x in range(2, 129):
#   no = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[1]').text
#   poly_name = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[2]').text
    
#   detail_tup = (no, poly_name)
#   print(detail_tup)
  
#   f = open('technical/technical_colleges.csv', 'a', newline='', encoding="utf-8")
#   writer = csv.writer(f)
#   writer.writerow(detail_tup)
# f.close()
  
# INNOVATION ENTERPRISE INSTITUTIONS
# driver.get('https://net.nbte.gov.ng/IEIs')
# for x in range(2, 183):
#   no = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[1]').text
#   poly_name = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[2]').text
    
#   detail_tup = (no, poly_name)
#   print(detail_tup)
  
#   f = open('technical/IEIs.csv', 'a', newline='', encoding="utf-8")
#   writer = csv.writer(f)
#   writer.writerow(detail_tup)
#   f.close()

# VOCATIONAL ENTERPRISE INSTITUTIONS
# driver.get('https://net.nbte.gov.ng/VEI')
# for x in range(2, 82):
#   no = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[1]').text
#   poly_name = driver.find_element(By.XPATH, '//*[@id="block-zircon-content"]/article/div/div/table/tbody/tr[' +str(x)+ ']/td[2]').text
    
#   detail_tup = (no, poly_name)
#   print(detail_tup)
  
#   f = open('technical/VEIs.csv', 'a', newline='', encoding="utf-8")
#   writer = csv.writer(f)
#   writer.writerow(detail_tup)
#   f.close()
  
driver.quit()

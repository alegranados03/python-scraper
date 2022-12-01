from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://wac.bell.ca:8000/wac-ia/bell_login.jsp")
userID = driver.find_element(By.XPATH, "//input[@id='strUsrAlias']")
userID.send_keys("LB110")
Dealer_code = driver.find_element(By.XPATH, "//input[@id='strDealerID']")
Dealer_code.send_keys("35582")
Password = driver.find_element(By.XPATH, "//tbody/tr[3]/td[3]/input[2]")
Password.send_keys("Expert3l")
SubmitBtn = driver.find_element(By.XPATH, "//input[@id='loginId']")
SubmitBtn.click()
PortIn_dates_changes = driver.find_element(
    By.XPATH, "//span[contains(text(),'Port-In Date Changes')]")
PortIn_dates_changes.click()
Manual_entry = driver.find_element(
    By.XPATH, "//a[contains(text(),'Manual Entry')]")
Manual_entry.click()
PortIn_Number = driver.find_element(
    By.XPATH, "//a[contains(text(),'Manual Entry')]")
PortIn_Number.send_keys("")
Requested_date = driver.find_element(
    By.XPATH, "//input[@id='dp1669855704625']")
ASAP_checkbox = driver.find_element(
    By.XPATH, "//tbody/tr[@id='rowId_0']/td[6]/input[1]")
ASAP_checkbox.click()
Validate_btn = driver.find_element(
    By.XPATH, "//body[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/div[2]/span[1]/a[1]/span[1]")
Validate_btn.click()

driver.implicitly_wait(10)
driver.close()

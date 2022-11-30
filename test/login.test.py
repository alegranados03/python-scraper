from ast import Bytes
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import login

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://wac.bell.ca:8000/wac-ia/bell_login.jsp")
userID = driver.find_element("//input[@id='strUsrAlias']")
userID.send_keys("LB110")
Dealer_code = driver.find_element("//input[@id='strDealerID']")
Dealer_code.send_keys("35582")
Password = driver.find_element("//tbody/tr[3]/td[3]/input[2]")
Password.send_keys("Expert3l")
SubmitBtn = driver.find_element("//input[@id='loginId']")
SubmitBtn.click()
driver.close()

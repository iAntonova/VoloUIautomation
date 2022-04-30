from lib2to3.pgen2 import driver
from jmespath import search
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from jmespath import search
driver = webdriver.Chrome()

driver.get('http://automationpractice.com/index.php')
searchbox = driver.find_element_by_xpath('//*[@id="search_query_top"]')
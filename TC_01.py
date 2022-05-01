from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import NoSuchElementException
import time
import logging

if __name__ == '__main__':

    has_logging = False

    logging.basicConfig(filename = 'tc_01_logs.log',
                            format = '%(asctime)s - %(filename)s ' '%(levelname)s: %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S', level='INFO')

    has_logging = True
        
    try:
        logging.info("Loading Chrome")
        driver_c = webdriver.Chrome()
        logging.info("Loading Firefox")
        driver_f = webdriver.Firefox()
        logging.info("Loading Edge")
        driver_e = webdriver.Edge()
        drivers = [driver_c, driver_f, driver_e]

    except Exception as x:
        logging.error(x)
    else:
        logging.info("Loading successful")

    for driver in drivers:
        try:
            driver.maximize_window()
            driver.get('http://automationpractice.com/index.php')
                
            search_box = driver.find_element_by_id('search_query_top')
            search_button = driver.find_element_by_name('submit_search')

            search_box.send_keys('product')
            logging.info("Searching for 'product'")
            search_button.click()
            time.sleep(5)

            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//*[@id='center_column']/p"))
            )
                
            get_source = driver.page_source
            search_text = "No results were found for your search"

            if search_text in get_source:
                print(True)
                logging.info("Text is displayed on the page: True")
            else:
                print(False)
                logging.info("Text is displayed on the page: False")

        except:
            driver.quit()

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import logging
import time

# Logging config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s- %(levelname)s-%(message)s",
    filename='log_file.log',
    filemode='w+')

# Data and locators used in test
driver_types = ['chrome', 'firefox', 'edge']
url = 'http://automationpractice.com/'
field_search_id = 'search_query_top'
button_search_name = 'submit_search'
message_warning_class = 'alert-warning'
searched_word = 'product'


# Return driver by type
def get_driver(driver_type):
    try:
        if driver_type == 'chrome':
            return webdriver.Chrome(ChromeDriverManager().install())
        elif driver_type == 'firefox':
            return webdriver.Firefox(
                executable_path=GeckoDriverManager().install())
        elif driver_type == 'edge':
            return webdriver.Edge(EdgeChromiumDriverManager().install())
        logging.info(f'{driver_type} driver successfully initialized')
    except:
        logging.error(f'{driver_type} driver not initialized')


def test(driver):
    driver.maximize_window()
    driver.get(url)
    search_field = driver.find_element_by_id(field_search_id)
    search_button = driver.find_element_by_name(button_search_name)
    search_field.send_keys(searched_word)
    search_button.click()
    time.sleep(3)
    try:
        driver.find_element_by_class_name(message_warning_class)
        logging.info('No result is found')
    except:
        logging.error("Not Found warning message")


for driver_type in driver_types:
    logging.info(f'Start test for {driver_type}')
    driver = get_driver(driver_type)
    if driver:
        test(driver)
        driver.quit()

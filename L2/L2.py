import time
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager



# Logging config
logging.basicConfig(filename = 'L2/tc_02_logs.log', level=logging.INFO,
                    format = '%(asctime)s - %(filename)s ' '%(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', filemode='w+')

# Data and locators used in test
driver_types = ['chrome', 'firefox', 'edge']
URL = 'https://courses.letskodeit.com/practice'
RADIO_BTN = 'div#radio-btn-example > fieldset > label'
SELECT_CLASS = 'div#select-class-example > fieldset > select > option'
MUTLIPLE_SELECT = 'div#multi-select-example-div > fieldset > select > option'
CHECKBOX = 'div#checkbox-example-div > fieldset > label'
SWITCH_WINDOW = 'div#open-window-example-div > fieldset > button'
SWITCH_TAB = 'div#open-tab-example-div > fieldset > a'
SWITCH_TO_ALERT = 'div#alert-example-div > fieldset > input'
WEB_TABLE = 'div#table-example-div > div.left-align > fieldset > table > tbody > tr > td'
ENABLED_DISABLED = 'div#enabled-example-div > fieldset > input'
ELEMENT_DISPLAYED = 'div#hide-show-example-div > fieldset > input'
MOUSE_HOVER = 'div#mouse-hover-example-div > div > fieldset > div > button'

# Return driver
def get_driver(driver_type):
    try:
        if driver_type == 'chrome':
            return webdriver.Chrome(ChromeDriverManager().install())
        elif driver_type == 'firefox':
            return webdriver.Firefox(
                executable_path=GeckoDriverManager().install())
        elif driver_type == 'edge':
            return webdriver.Edge(EdgeChromiumDriverManager().install())
        logging.info(f'{driver_type} driver initialized successfully')
    except:
        logging.error(f'{driver_type} driver not initialized')

def test(driver):
    driver.maximize_window()
    driver.get(URL)
    time.sleep(3)
    try:
        result_radio_btn = driver.find_elements_by_css_selector(RADIO_BTN)
        logging.info('"Radio Buttons Example" block found!')
        try:
            count_radio_btn = len(result_radio_btn)
            logging.info(f'Radio Buttons amount: {count_radio_btn}')
        except:
            logging.error("Warning message: Unable to count 'Radio Buttons Example'")
    except:
        logging.error("Warning message: 'Radio Buttons Example' Not Found")


    try:
        result_select_class = driver.find_elements_by_css_selector(SELECT_CLASS)
        logging.info('"Select Class Example" block found!')
        try:
            count_select_class = len(result_select_class)
            logging.info(f'Select Class amount: {count_select_class}')
        except:
            logging.error("Warning message: Unable to count 'Select Class Example'")
    except:
        logging.error("Warning message: 'Select Class Example' Not Found")


    try:
        result_multiple_select = driver.find_elements_by_css_selector(MUTLIPLE_SELECT)
        logging.info('"Multiple Select Example" block found!')
        try:
            count_multiple_select = len(result_multiple_select)
            logging.info(f'Multiple Select amount: {count_multiple_select}')
        except:
            logging.error("Warning message: Unable to count 'Multiple Select Example'")
    except:
        logging.error("Warning message: 'Multiple Select Example' Not Found")


    try:
        result_checkbox = driver.find_elements_by_css_selector(CHECKBOX)
        logging.info('"Checkbox Example" block found!')
        try:
            count_checkbox = len(result_checkbox)
            logging.info(f'Checkbox amount: {count_checkbox}')
        except:
            logging.error("Warning message: Unable to count 'Checkbox Example'")
    except:
        logging.error("Warning message: 'Checkbox Example' Not Found")


    try:
        result_switch_window = driver.find_elements_by_css_selector(SWITCH_WINDOW)
        logging.info('"Switch Window Example" block found!')
        try:
            count_switch_window = len(result_switch_window)
            logging.info(f'Switch Window amount: {count_switch_window}')
        except:
            logging.error("Warning message: Unable to count 'Switch Window Example'")
    except:
        logging.error("Warning message: 'Switch Window Example' Not Found")


    try:
        result_switch_tab = driver.find_elements_by_css_selector(SWITCH_TAB)
        logging.info('"Switch Tab Example" block found!')
        try:
            count_switch_tab = len(result_switch_tab)
            logging.info(f'Switch Tab amount: {count_switch_tab}')
        except:
            logging.error("Warning message: Unable to count 'Switch Tab Example'")
    except:
        logging.error("Warning message: 'Switch Tab Example' Not Found")


    try:
        result_switch_to_alert = driver.find_elements_by_css_selector(SWITCH_TO_ALERT)
        logging.info('"Switch To Alert Example" block found!')
        try:
            count_switch_to_alert = len(result_switch_to_alert)
            logging.info(f'Switch To Alert amount: {count_switch_to_alert}')
        except:
            logging.error("Warning message: Unable to count 'Switch To Alert Example'")
    except:
        logging.error("Warning message: 'Switch To Alert Example' Not Found")


    try:
        result_web_table = driver.find_elements_by_css_selector(WEB_TABLE)
        logging.info('"Web Table Example" block found!')
        try:
            count_web_table = len(result_web_table)
            logging.info(f'Web Table amount: {count_web_table}')
        except:
            logging.error("Warning message: Unable to count 'Web Table Example'")
    except:
        logging.error("Warning message: 'Web Table Example' Not Found")


    try:
        result_enabled_disabled = driver.find_elements_by_css_selector(ENABLED_DISABLED)
        logging.info('"Enabled/Disabled Example" block found!')
        try:
            count_enabled_disabled = len(result_enabled_disabled)
            logging.info(f'Enabled/Disabled amount: {count_enabled_disabled}')
        except:
            logging.error("Warning message: Unable to count 'Enabled/Disabled Example'")
    except:
        logging.error("Warning message: 'Enabled/Disabled Example' Not Found")



    try:
        result_element_displayed = driver.find_elements_by_css_selector(ELEMENT_DISPLAYED)
        logging.info('"Element Displayed Example" block found!')
        try:
            count_element_displayed = len(result_element_displayed)
            logging.info(f'Element Displayed amount: {count_element_displayed}')
        except:
            logging.error("Warning message: Unable to count 'Element Displayed Example'")
    except:
        logging.error("Warning message: 'Element Displayed Example' Not Found")


    try:
        result_mouse_hover = driver.find_elements_by_css_selector(MOUSE_HOVER)
        logging.info('"Mouse Hover Example" block found!')
        try:
            count_mouse_hover = len(result_mouse_hover)
            logging.info(f'Mouse Hover amount: {count_mouse_hover}')
        except:
            logging.error("Warning message: Unable to count 'Mouse Hover Example'")
    except:
        logging.error("Warning message: 'Mouse Hover Example' Not Found")



for driver_type in driver_types:
    logging.info(f'Start test for {driver_type}')
    driver = get_driver(driver_type)
    if driver:
        test(driver)
        driver.quit()

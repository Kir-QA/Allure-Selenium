### fixture imports ###
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
### fixture config ###
@pytest.fixture(scope='session')
### main function ###
def browser():
    # Name of test case:
    ### start configuration of chrome ###
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-infobars") # disablings infobars
    chrome_options.add_argument("--disable-extensions") # disablings extentions
    chrome_options.add_argument("--disable-gpu") # applicaple to windows os only
    chrome_options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
    '''
    Disactivated params for chrome:
    '''
    chrome_options.add_argument("start-maximized") # open Browser in maximized mode
    #chrome_options.add_argument("--headless") # Start Chrome in headless mode
    ### end configuration of chrome ###
    
    ### Variable's for web driver selenium ###
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    ### Closing function web driver ###
    yield driver
    driver.quit()
### END of fixture
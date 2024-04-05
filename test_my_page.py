### Import's of Library & Files ###
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
### Global variable & Constant's ###
URL = 'https://kir-qa.github.io/'
### main code ###
def test_my_page(browser):
    # START function #
    """
    Test case Eva-01: Open URL https://kir-qa.github.io/
    """
    # Open site in browser #
    browser.get(url= URL)
    # Find blocks whith info
    blocks = browser.find_elements(by=By.CSS_SELECTOR, value="[class='link']")
    # Starting cycle in one string
    links = [block.text for block in blocks]
    # Checking assertition. When having this fields whith right text, assertition is thruth. #
    assert links == ['TELEGRAM', 'TWITTER', 'EMAIL', 'GIT'], 'Unexpected links'
    # END of function #
#@pytest.mark.xfail(reason="Wait for resolve BUG #Sv87879Eva-01") #TEMPORARY skip function
def test_mario_jump(browser):
    # START function #
    """
    Test case Eva-02: Check mario jump & make sceen shot in folder screen & make allure screenshot
    """
    # Open site in browser #
    browser.get(url= URL)
    # Find mario
    element = browser.find_element(by=By.CSS_SELECTOR, value="[alt=Марио]")
    element.click()
    # Make screenshot in screen folder
    browser.save_screenshot('/Users/sveet/Pojects/Python/Python_allure_selenium_home/screen/my_page.png')
    #Just for fun
    element = browser.find_element(by=By.CSS_SELECTOR, value="[class='mario-img']")
    # make screenshot for allure report
    assert element.is_displayed
    allure.attach(
              browser.get_screenshot_as_png(),
              name='screenshot',
              attachment_type=allure.attachment_type.PNG
        )
    # END function #
### THE END ###
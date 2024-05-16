import pytest
 
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
 
GOOGLE_HOME = 'https://google.com/'
LINK_CLASS = 'LC20lb'
 
scenarios('google_scenario.feature')
 
 
@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()
 
 
@given('the Google home page is displayed')
def google_home(browser):
    browser.get(GOOGLE_HOME)
 
 
@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    search_input = browser.find_element(By.ID, 'APjFqb')
    search_input.send_keys(phrase + Keys.RETURN)
 
 
@then(parsers.parse('results are shown for "{phrase1}" or "{phrase2}"'))
def search_results(browser, phrase1, phrase2):
    links = browser.find_elements(By.CSS_SELECTOR, 'a > .LC20lb')
    
    count = 0
    for l in links:
        if phrase1 in l.text.lower() or phrase2 in l.text.lower():
            count += 1
    
    assert count / len(links) > 0.8, "Count found links less than 80%"
    # assert len(h2s) > 0
    
    search_input = browser.find_element(By.ID, 'APjFqb')
    assert search_input.text == phrase1

    

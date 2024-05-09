import pytest
 
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
 
 
GOOGLE_HOME = 'https://google.com/'
 
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
 
 
@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    assert len(browser.find_elements(By.XPATH, '//h2')) > 0
    
    search_input = browser.find_element(By.ID, 'APjFqb')
    assert search_input.text == phrase


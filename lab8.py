from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, 'username')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login')

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

class AnalysisOpening:
    def __init__(self, driver):
        self.driver = driver
        self.opening_name = (By.CLASS_NAME, "eco-opening-name")
        self.pgn_input = (By.CLASS_NAME, "load-from-pgn-textarea")
        self.pgn_input_button = (By.CLASS_NAME, "cc-button-primary")
        
    def enter_opening(self, pgn):
        self.driver.find_element(*self.pgn_input).send_keys(pgn)

    def click_input_btn(self):
        self.driver.find_element(*self.pgn_input_button).click()

    def get_opening_name(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.opening_name))
        opening_element = self.driver.find_element(*self.opening_name)
        opening_name = opening_element.text
        return opening_name
    
    def check_opening(self, pgn, opening_name):
        self.enter_opening(pgn)
        self.click_input_btn()
        assert(self.get_opening_name() == opening_name)


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("https://www.chess.com/login")
    
    login_page = LoginPage(driver)
    login_page.login("trade57", "0979035573")
    
    driver.get("https://www.chess.com/analysis")
    analysis = AnalysisOpening(driver)
    analysis.check_opening("rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPPKPPP/RNBQ1BNR b kq - 1 2", "King's Pawn Opening: The Bongcloud")

    driver.quit()



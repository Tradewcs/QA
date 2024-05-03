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

class OpeningPage:
    def __init__(self, driver):
        self.driver = driver
        self.opening_name = (By.CLASS_NAME, "eco-opening-name")
        self.pgn_input = (By.CLASS_NAME, "load-from-pgn-textarea")
        self.pgn_input_button = (By.XPATH, "/html/body/div[3]/div/div/div[1]/div/div[2]/div[7]/button")
        
    def enter_pgn(self, pgn):
        self.driver.find_element(*self.pgn_input).send_keys(pgn)

    def click_input_btn(self):
        self.driver.find_element(*self.pgn_input_button).click()

    def is_opening_present(self, postion):
        try:
            WebDriverWait(self.driver, 15).until(EC.text_to_be_present_in_element(self.opening_name, postion))
            return True
        except:
            return False
      
from selenium import webdriver
from Pages import *    
import pytest
    

@pytest.mark.parametrize("pgn, result", [("rnbqkbnr/pppp1ppp/8/4p3/4P3/8/PPPPKPPP/RNBQ1BNR b kq - 1 2", "King's Pawn Opening: The Bongcloud"), ("rnbqkbnr/pppp1ppp/8/4p3/3P4/8/PPP1PPPP/RNBQKBNR w KQkq e6 0 2", "Englund Gambit")])
def test_check_opening(pgn, result):
    driver = webdriver.Firefox()
    driver.get("https://www.chess.com/analysis")
    openingPage = OpeningPage(driver) 

    openingPage.enter_pgn(pgn)
    openingPage.click_input_btn()
    assert openingPage.is_opening_present(result), f"The text {result} must be present"


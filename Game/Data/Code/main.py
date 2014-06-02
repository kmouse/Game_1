from Data.Code.main_menu import run_menu
from Data.Code.game import control_game
import logging

# Log debug and higher calls to this file
logging.basicConfig(filename='game.log', level=logging.DEBUG)


def run():
    logging.info("Running")
    while True:
        run_menu()
        control_game()
        
if __name__ == "__main__":
    run()
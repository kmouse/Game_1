from main_menu import run_menu
from game import control_game


def run():
    while True:
        run_menu()
        control_game()
        
if __name__ == "__main__":
    run()
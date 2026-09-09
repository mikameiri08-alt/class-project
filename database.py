import pandas as pd
import screen
import game_field
import main

#dictionary to hold the save files
play_saves = {}

def get_current_data():
    """get the current data"""
    return {
        "grass_positions": [screen.grass_positions],
        "mine_positions": [game_field.mine_positions],
        "player_x": [main.player_x],
        "player_y": [main.player_y]
    }

def short_press_num(num):
    """Saves the current game state to the dictionary."""
    df = pd.DataFrame(get_current_data())
    play_saves[num] = df

def long_num_press(num):
    """Loads and prints the saved game state."""
    if num not in play_saves:
        print("Didn't save anything under this number.")
    else:
        df = play_saves[num]
        print(df)

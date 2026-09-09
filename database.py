import os
import pandas as pd
import screen
import game_field
import main


def get_current_data():
    """get the current data from the game"""
    return {
        "grass_positions": [str(screen.grass_positions)],
        # Converted to string to preserve lists/tuples in CSV
        "mine_positions": [str(game_field.mine_positions)],
        "player_x": [main.player_x],
        "player_y": [main.player_y]
    }


def short_press_num(digit):
    """Saves the current game state directly to a CSV file."""
    df = pd.DataFrame(get_current_data())
    filename = f"save_slot_{digit}.csv"
    df.to_csv(filename, index=False)
    print(f"Game successfully exported and saved to {filename}")


def long_num_press(digit):
    """Loads and reads the game state back from the CSV file."""
    filename = f"save_slot_{digit}.csv"

    # Check if the file exists on the disk
    if not os.path.exists(filename):
        print(f"No save file found named '{filename}'")
    else:
        # Read the data back into Python
        df = pd.read_csv(filename)
        print(df)


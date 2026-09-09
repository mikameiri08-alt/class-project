import os
import ast
import pandas as pd
import screen
import game_field



def get_current_data(player_x, player_y):
    """get the current data from the game"""
    return {
        "grass_positions": [str(screen.grass_positions)],
        # save the current mines
        "mine_positions": [str(screen.level_mines)],
        "trap position": [str(screen.level_traps)],
        "player_x": [player_x],
        "player_y": [player_y]
    }


def short_press_num(digit, player_x, player_y):
    """save the data from the game"""
    df = pd.DataFrame(get_current_data(player_x, player_y))
    filename = f"save_slot_{digit}.csv"
    df.to_csv(filename, index=False)
    print(f"Game successfully saved to {filename}")


def long_num_press(digit):
    """load the data from the game (specific num press)"""
    filename = f"save_slot_{digit}.csv"

    if not os.path.exists(filename):
        print(f"No save file found named '{filename}'")
        return None

    df = pd.read_csv(filename)

    # get the data from the CVS
    loaded_grass = ast.literal_eval(df["grass_positions"].iloc[0])
    loaded_mines = ast.literal_eval(df["mine_positions"].iloc[0])
    loaded_x = int(df["player_x"].iloc[0])
    loaded_y = int(df["player_y"].iloc[0])

    # update the mines and grass location
    screen.grass_positions = loaded_grass
    screen.level_mines = loaded_mines
    game_field.mine_positions = loaded_mines

    print(f"Game slot {digit} successfully loaded!")
    return loaded_x, loaded_y

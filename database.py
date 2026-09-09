import os
import ast
import pandas as pd
import screen
import game_field

def get_current_data(player_x, player_y, guard_row, guard_x):
    """Gathers all persistent map layouts and structural positions into a unified dictionary structure"""
    return {
        "grass_positions": [str(screen.grass_positions)],
        "mine_positions": [str(screen.level_mines)],
        "trap_positions": [str(screen.level_traps)],
        "player_x": [player_x],
        "player_y": [player_y],
        "guard_row": [guard_row],
        "guard_x": [guard_x]
    }

def short_press_num(digit, player_x, player_y, guard_row, guard_x):
    """Saves the active game matrices and entity variables to a designated target file slot"""
    df = pd.DataFrame(get_current_data(player_x, player_y, guard_row, guard_x))
    filename = f"save_slot_{digit}.csv"
    df.to_csv(filename, index=False)
    print(f"Game successfully saved to {filename}")

def long_num_press(digit):
    """Loads previous game matrices and entity variables from a slot, reconstruction lists using AST parser"""
    filename = f"save_slot_{digit}.csv"

    if not os.path.exists(filename):
        print(f"No save file found named '{filename}'")
        return None

    df = pd.read_csv(filename)

    # Safely reconstruct array data blocks from stored string maps using literal evaluation
    loaded_grass = ast.literal_eval(df["grass_positions"].iloc[0])
    loaded_mines = ast.literal_eval(df["mine_positions"].iloc[0])
    loaded_traps = ast.literal_eval(df["trap_positions"].iloc[0])
    loaded_x = int(df["player_x"].iloc[0])
    loaded_y = int(df["player_y"].iloc[0])
    loaded_guard_row = int(df["guard_row"].iloc[0])
    loaded_guard_x = int(df["guard_x"].iloc[0])

    screen.grass_positions = loaded_grass
    screen.level_mines = loaded_mines
    game_field.mine_positions = loaded_mines
    screen.level_traps = loaded_traps

    print(f"Game slot {digit} successfully loaded!")
    return loaded_x, loaded_y, loaded_guard_row, loaded_guard_x

import json
import pickle
from ..main import active_entities, global_vars
from ..utils import *


def move_left():
    print('moved left\n')


def move_right():
    print('moved right\n')


def move_up():
    print('moved up\n')


def move_down():
    print('moved down\n')


def quit_game():
    save_player()
    quit_choice = input('\nAre you sure you want to quit? (y/N): ')

    if quit_choice.lower() == 'y':
        quit()
    else:
        return


def stats():
    for stat, value in active_entities['player'].get_stats().items():
        print(stat.capitalize() + ': ' + str(value))
    print()


def save_player():
    player = active_entities['player']
    with open(global_vars.get('player_savefile_path', ''), 'w+') as player_savefile:
        if player_savefile:
            player_attributes = vars(player)
            del player_attributes['inventory']
            # Write to save file
            player_savefile.write(json.dumps(player_attributes))


def get_default_action_methods():
    return {
        'move_left': move_left,
        'move_right': move_right,
        'move_up': move_up,
        'move_down': move_down,
        'quit': quit_game,
        'stats': stats,
        'clear_screen': clear_screen,
        'save_player': save_player
    }

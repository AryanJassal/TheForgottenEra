import os

from ..main import active_entities

def move_left():
    print('moved left')

def move_right():
    print('moved right')

def move_up():
    print('moved up')

def move_down():
    print('moved down')

def quit_game():
    quit_choice = input('\nAre you sure you want to quit? (y/N): ')

    if quit_choice.lower() == 'y':
        quit()
    else:
        return

def stats():
    active_entities['player'].get_stats()

def clear_screen():
    os.system('cls clear')

def get_default_action_methods():
    return {
        'move_left': move_left, 
        'move_right': move_right, 
        'move_up': move_up,
        'move_down': move_down,
        'quit': quit_game,
        'stats': stats,
        'clear_screen': clear_screen
    }

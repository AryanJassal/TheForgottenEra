import json, os, sys
import zyga

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_PATH)

with open('playerconfig.json', 'r') as file:
    playerdata = json.load(file)

with open('items.json', 'r') as file:
    itemdata = json.load(file)

player = zyga.entity_classes.Player(zyga.game_objects.create_attribute_list(playerdata))
squirrel = zyga.entities.hideous_squirrel

def move_down():
    print('moved down')

def stats():
    player.get_stats()

def quit_game():
    quit_choice = input('\nAre you sure you want to quit? (y/N): ')

    if quit_choice.lower() == 'y':
        quit()
    else:
        return

methods = {
    'move_down': move_down,
    'stats': stats,
    'quit': quit_game
}
methods.update(zyga.world.get_default_action_methods())

poison = zyga.items.Poison(itemdata.get('poison'))
player.acquire_item(poison)

os.system('cls clear')

# Main game loop
while True:
    command = input('|command-prompt> ')
    result = zyga.world.parse_actions(command, methods)

    if result:
        result()
        print()

    # input()
    # os.system('cls clear')

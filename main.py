import json
import os
import sys
import zyga
from actions import return_actions

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
PLAYER_SAVEFILE_DIR = os.path.dirname(os.path.abspath('playerconfig.json'))
PLAYER_SAVEFILE = os.path.abspath('playerconfig.json')

sys.path.append(SCRIPT_PATH)
zyga.global_vars['player_savefile'] = PLAYER_SAVEFILE

try:
    with open(PLAYER_SAVEFILE, 'r') as file:
        playerdata = {}
        try:
            playerdata = json.load(file)
        except json.JSONDecodeError:
            # The file's empty
            zyga.clear_screen()
            print('The player configuration file is empty. Loading base values for all player stats.')
            zyga.pause_screen('Press any key to continue.')
except FileNotFoundError:
    zyga.clear_screen()
    print('The player configuration file does not exist. Loading base values for all player stats.')
    zyga.pause_screen('Press any key to continue.')

# try:
#     playerdata = pickle.load(open(PLAYER_SAVEFILE, 'rb'))
# except FileNotFoundError:
#     playerdata = {}
#     zyga.clear_screen()
#     print('The player configuration file does not exist. Loading base values for all player stats.')
#     zyga.pause_screen('Press any key to continue.')

# print(playerdata)
# zyga.pause_screen()


with open('items.json', 'r') as file:
    itemdata = json.load(file)

# for items in playerdata.get['inventory']:
#     inventory_items = ()

player = zyga.entity_classes.Player(zyga.game_objects.create_attribute_list(playerdata))

methods = return_actions()
methods.update(zyga.cli.get_default_action_methods())

poison = zyga.items.Item(itemdata.get('poison'))
baditem = zyga.items.Item(itemdata.get('baditem'))
player.acquire_item(poison)
player.acquire_item(poison)
player.acquire_item(poison)
player.acquire_item(baditem)

os.system('cls clear')
# print(PLAYER_SAVEFILE_PATH)

# Main game loop
while True:
    command = input('|command-prompt> ')
    result = zyga.cli.parse_actions(command, methods)

    if result:
        result()
        # print()

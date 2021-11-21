import json
import os
import sys
import zyga

from actions import return_actions

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
PLAYER_SAVEFILE_DIR = os.path.dirname(os.path.abspath('playerconfig.json'))
PLAYER_SAVEFILE_PATH = os.path.abspath('playerconfig.json')

sys.path.append(SCRIPT_PATH)
zyga.global_vars['player_savefile_path'] = PLAYER_SAVEFILE_PATH

with open(PLAYER_SAVEFILE_PATH, 'r') as file:
    playerdata = {}
    try:
        playerdata = json.load(file)
    except json.JSONDecodeError:
        # The file's empty
        zyga.clear_screen()
        print('The player configuration file is empty. Loading minimum values for all player stats.')
        zyga.pause_screen('Press any key to continue.')


with open('items.json', 'r') as file:
    itemdata = json.load(file)

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

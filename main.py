import json, os, sys
import zyga

from actions import return_actions

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_PATH)

with open('playerconfig.json', 'r') as file:
    playerdata = json.load(file)

with open('items.json', 'r') as file:
    itemdata = json.load(file)

player = zyga.entity_classes.Player(zyga.game_objects.create_attribute_list(playerdata))
# squirrel = zyga.entities.hideous_squirrel

methods = return_actions()
methods.update(zyga.world.get_default_action_methods())

# poison = zyga.items.Poison(itemdata.get('poison'))
poison = zyga.items.Item(itemdata.get('poison'))
baditem = zyga.items.Item(itemdata.get('baditem'))
player.acquire_item(poison)
player.acquire_item(poison)
player.acquire_item(poison)
player.acquire_item(baditem)

os.system('cls clear')

# Main game loop
while True:
    command = input('|command-prompt> ')
    result = zyga.world.parse_actions(command, methods)

    if result:
        result()
        print()

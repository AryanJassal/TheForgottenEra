from zyga import *
from actions import return_actions

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
PLAYER_SAVEFILE = os.path.abspath('playerconfig.json')
PLAYER_INVENTORY_SAVEFILE = os.path.abspath('playerinventory.json')

sys.path.append(SCRIPT_PATH)
global_vars['player_savefile'] = PLAYER_SAVEFILE
global_vars['player_inventory_savefile'] = PLAYER_INVENTORY_SAVEFILE


playerdata = load_file(PLAYER_SAVEFILE)
playerinventory = load_file(PLAYER_INVENTORY_SAVEFILE)
itemdata = load_file('items.json')

player = load_player(playerdata, playerinventory)

methods = return_actions()
methods.update(cli.get_default_action_methods())

# poison = items.Item(itemdata.get('poison'))
# baditem = items.Item(itemdata.get('baditem'))
# player.acquire_item(poison)
# player.acquire_item(poison)
# player.acquire_item(poison)
# player.acquire_item(baditem)

os.system('cls clear')

# Main game loop
while True:
    command = input('|> ')
    result = cli.parse_actions(command, methods)

    if result:
        result()

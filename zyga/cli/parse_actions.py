# import os
from .default_actions import *
from ..main import *
# from ..game_objects import *

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))


def get_default_actions():
    with open(os.path.join(SCRIPT_PATH, 'default_actions.json'), 'r') as def_actions:
        if def_actions:
            return json.load(def_actions)
        print('The file default_actions.json could not be loaded.')
        return


def parse_actions(_prompt, methods=get_default_action_methods(), action_list=get_default_actions()):
    if not _prompt:
        # print('Please enter a command.')
        return

    command = _prompt.split()
    player = active_entities['player']

    for v in action_list.values():
        for key, value in v.items():
            if command[0] in key.split('|'):
                if type(value) is str:
                    # for single-word method calling commands
                    if command[0] in key:
                        value = value.replace('$', '')

                        if methods.get(value):
                            try:
                                return methods.get(value)
                            except:
                                print(f'Method {value} not found.')
                                return
                        else:
                            print(f'Command method {value} not found in methods. Please add it in the dictionary and try again.\n')
                            return
                else:
                    for prompts, action in value.items():
                        for prompt in prompts.split('|'):
                            # For prompts which involve item tags
                            if '%' in prompt:
                                valid_items = {}
                                prompt = prompt.replace('%', '')

                                for item_id, data in player.get_inventory().items():
                                    for tag in data['item'].get_tags():
                                        if tag == prompt:
                                            valid_items[item_id] = data['item']

                                for _item_id, _item in valid_items.items():
                                    if command[1] == _item_id:
                                        _item.consume()
                                        return
                                print('The player does not have this item. You can check your inventory with the command \'inv\'.\n')
                                return

                            # For method calling commands
                            if command[1] == prompt:
                                action = action.replace('$', '')

                                if methods.get(action):
                                    try:
                                        return methods.get(action)
                                    except AttributeError:
                                        print(f'Method {action} not found.\n')
                                        return
                                else:
                                    print(f'Command method {action} not found in methods. Please add it in the dictionary and try again.\n')
                                    return

                            # Command not found in command dictionary
                            else:
                                print('Incorrect argument provided. Please double-check it and try again.\n')
                                return
        print('Command not found. Please check your spelling and try again.\n')
        return

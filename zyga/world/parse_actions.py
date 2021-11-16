import os, json
from .default_actions import *
from ..main import *
from ..game_objects import *

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

def get_default_actions():
    with open(os.path.join(SCRIPT_PATH, 'default_actions.json'), 'r') as def_actions:
        return json.load(def_actions)

def parse_actions(prompt, methods=get_default_action_methods(), action_list=get_default_actions()):
    if not prompt:
        # print('Please enter a command.')
        return

    command = prompt.split()
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
                            print(f'Command method {value} not found in methods. Please add it in the dictionary and try again.')
                else:
                    for prompts, action in value.items():
                        for prompt in prompts.split('|'):
                            # For prompts which involve item tags
                            if '%' in prompt:
                                valid_items = {}
                                prompt = prompt.replace('%', '')

                                for item in player.get_inventory():
                                    for tag in item.get_tags():
                                        if tag == prompt:
                                            valid_items[item.name] = item                     

                                for items in valid_items.values():
                                    if command[1] == items.id:
                                        items.consume()
                                        return
                                print('Invalid argument provided. Please double-check it and try again.')
                                return

                            # For method calling commands
                            elif command[1] == prompt:
                                action = action.replace('$', '')

                                if methods.get(action):
                                    try:
                                        return methods.get(action)
                                    except:
                                        print(f'Method {action} not found.')
                                        return
                                else:
                                    print(f'Command method {action} not found in methods. Please add it in the dictionary and try again.')
                                    return

                            # Command not found in command dictionary
                            else:
                                print('Incorrect argument provided. Please double-check it and try again.')
                                return
        print('Command not found. Please check your spelling and try again.')
        return
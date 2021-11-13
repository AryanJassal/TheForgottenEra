import os, json
from .default_actions import *
from ..main import *

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

def get_default_actions():
    with open(os.path.join(SCRIPT_PATH, 'default_actions.json'), 'r') as def_actions:
        return json.load(def_actions)

def parse_actions(prompt, methods=get_default_action_methods(), action_list=get_default_actions()):
    command = prompt.split()

    for k, v in action_list.items():
        for key, value in v.items():
            if command[0] in key.split('|'):
                for prompt, action in value.items():

                    # for consumables
                    if '%' in prompt:
                        valid_items = [item for item in temp_playerinv.items() if prompt.replace('%', '') in item.get('tags')]

                        if command[1] in valid_items:
                            temp_playerinv[command[1]].consume()
                        pass                        

                    # for method calling commands
                    if command[1] == prompt:
                        action = action.replace('$', '')

                        if methods.get(action):
                            try:
                                return methods.get(action)
                            except:
                                print(f'Method {action} not found.')
                                return
                        else:
                            print(f'Command method {action} not found in methods. Please add it in the dictionary and try again.')
                print('Incorrect argument provided. Please double-check it and try again.')
                return
        print('Command not found. Please check your spelling and try again, or type \'help\' (not yet functional but bear with it)')
        return
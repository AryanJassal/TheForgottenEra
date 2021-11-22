import random
import json
from .entity_classes import Player
from .item_classes import Item
from ..utils import *


def create_attribute_list(attributes):
    attribute_list = {}

    for k, v in attributes.items():
        for key, value in v.items():
            if type(value) is dict:
                attribute_list[key] = random.randint(value['min'], value['max'])
            else:
                attribute_list[key] = value

    return attribute_list


def load_file(filepath):
    data = {}
    try:
        with open(filepath, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                # The file's empty
                clear_screen()
                print(f'The file at {filepath} is empty or invalid. Loading base values for all player stats.')
                pause_screen('Press any key to continue.')
    except FileNotFoundError:
        clear_screen()
        print(f'The file at {filepath} does not exist. Loading base values for all player stats.')
        pause_screen('Press any key to continue.')

    return data


def load_player(playerconfig, itemdata):
    attribute_list = {}
    for key, value in playerconfig.items():
        attribute_list[key] = value

    player = Player(attribute_list)

    for item in itemdata:
        player.acquire_item(Item(item))

    return player

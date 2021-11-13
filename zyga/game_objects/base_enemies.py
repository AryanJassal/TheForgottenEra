import json
import os
from .entity_classes import *
from .utils import create_attribute_list

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(SCRIPT_PATH, 'default_enemy_config.json'), 'r') as config:
    enemyconfig = json.load(config)

ec = enemyconfig

# print(create_attribute_list(enemyconfig))
hideous_squirrel = Enemy(create_attribute_list(enemyconfig))

## Add support for weighted bias in loading config file

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

# print(player.get_name(), 'enters the arena with', player.get_health(), 'health!')
# print('Oh? What is this? A', squirrel.get_name(), 'walks in with', squirrel.get_health(), 'health!')
# print('The player did not like how', squirrel.get_name(), 'looked! They attacked them, dealing', player.calculate_damage(squirrel), 'damage!')
# player.attack_entity(squirrel)
# print(squirrel.get_name(), 'is only left with', squirrel.get_health(), 'health!')
# print('The', squirrel.get_name(), 'is annoyed! It attacks the', player.get_name(), 'back, dealing', squirrel.calculate_damage(player), 'damage! It\'s nothing for the ' + player.get_name() + '!')
# squirrel.attack_entity(player)
# print('The player attacks its enemy agian, dealing', player.calculate_damage(squirrel), 'damage!')
# player.attack_entity(squirrel)

# while squirrel.has_health():
#     print('The squirrel still has', squirrel.get_health(), 'health left. The player attacks it again, dealing', player.calculate_damage(squirrel), 'damage!')
#     player.attack_entity(squirrel)

# else:
#     print('The squirrel couldn\'t handle the ' + player.get_name() + '\'s power and has died! It dropped', squirrel.death_exp, 'experience points. The player has', player.get_exp(), 'experience points in total!')

def move_down():
    print('moved down')

methods = {
    'move_down': move_down
}
methods.update(zyga.world.get_default_action_methods())

poison = zyga.items.Poison(itemdata.get('poison'))

command = input('|command-prompt> ')
result = zyga.world.parse_actions(command, methods)

if result:
    result()

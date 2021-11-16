from ..main import active_entities

class Item:
    def __init__(self, attributes):
        self.name = attributes.get('name', '')
        self.id = attributes['id']
        self.tags = [tag for tag in attributes['tags']]
        self.consume_action = attributes['on_consume']

    def get_tags(self):
        return self.tags

    def consume(self):
        player = active_entities['player']

        for action, strength in self.consume_action.items():
            if action == 'lose_health':
                player.modify_health(strength, '-')
            elif action == 'modify_health':
                player.modify_health(strength)
            elif action == 'gain_health':
                player.modify_health(strength, '+')
            elif action == 'lose_hunger':
                player.modify_hunger(strength, '-')
            elif action == 'modify_hunger':
                player.modify_hunger(strength)
            elif action == 'gain_hunger':
                player.modify_hunger(strength, '+')
            elif action == 'lose_thirst':
                player.modify_thirst(strength, '-')
            elif action == 'modify_thirst':
                player.modify_thirst(strength)
            elif action == 'gain_thirst':
                player.modify_thirst(strength, '+')
            elif action == 'lose_stamina':
                player.modify_stamina(strength, '-')
            elif action == 'modify_stamina':
                player.modify_stamina(strength)
            elif action == 'gain_stamina':
                player.modify_stamina(strength, '+')

        if action == 'feedback':
            print(strength)
        player.remove_item(self)

# class Poison(Item):
#     def consume(self, consumed_by=''):
#         if not self.consume_action.get('target', '') or self.consume_action.get('target') == 'self':
#             if consumed_by:
#                 consumed_by.modify_health(self.consume_action.get('strength', 0), '-')
#             else:
#                 active_entities['player'].modify_health(self.consume_action.get('strength', 0), '-')
#         else:
#             active_entities.get(self.consume_action.get('target')).modify_health(self.consume_action.get('strength', 0), '-')

#         print('Ouch! What was that?! Poison?!?!\n')

# class BadItem(Item):
#     def consume(self):
#         player = active_entities['player']

#         player.modify_health(50, '-')
#         player.modify_thirst(50, '-')
#         player.modify_hunger(50, '-')

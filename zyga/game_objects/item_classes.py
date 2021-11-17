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

        for action, params in self.consume_action.items():
            if action == 'modify_health':
                player.modify_health(**params)
            elif action == 'modify_hunger':
                player.modify_hunger(**params)
            elif action == 'modify_thirst':
                player.modify_thirst(**params)
            elif action == 'modify_stamina':
                player.modify_hunger(**params)

        if action == 'feedback':
            print(params)
        player.remove_item(self)

from ..main import active_entities

class Item:
    def __init__(self, attributes):
        self.name = attributes.get('name', '')
        self.id = attributes['id']
        self.tags = [tag for tag in attributes['tags']]
        self.consume_action = attributes['on_consume']

        # def consume(self, consumed_by):
        #     if not self.consume_action.get('target', '') or self.consume_action.get('target') == 'self':
        #         consumed_by.remove_health(self.consume_action.get('strength', 0))
        #     else:
        #         active_entities.get(self.consume_action.get('target')).remove_health(self.consume_action.get('strength', 0))

class Poison(Item):
    def consume(self, consumed_by):
        if not self.consume_action.get('target', '') or self.consume_action.get('target') == 'self':
            consumed_by.remove_health(self.consume_action.get('strength', 0))
        else:
            active_entities.get(self.consume_action.get('target')).remove_health(self.consume_action.get('strength', 0))

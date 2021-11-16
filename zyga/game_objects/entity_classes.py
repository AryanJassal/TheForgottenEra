from ..main import active_entities
import os

class Entity:
    def __init__(self, attributes):
        self.name = attributes.get('name', '')
        self.max_health = attributes.get('max_health', 1)
        self.health = self.max_health
        self.attack = attributes.get('attack', 0)
        self.defense = attributes.get('defense', 0)
        # self.level = attributes.get('level', 0)

    def get_name(self):
        return self.name

    def modify_health(self, health, operation='m'):
        if operation == 'm' or operation == '=':
            self.health = health
        elif operation == 'g' or operation == '+':
            self.health = min(self.health, self.health + health)
        elif operation == 'l' or operation == '-':
            self.health = max(0, self.health - health)
        else:
            raise ValueError(f'Operation {operation} is invalid. Options are: m: modify, g: gain, l: lose.')

    def modify_max_health(self, health, operation='m'):
        if operation == 'm' or operation == '=':
            self.max_health = health
        elif operation == 'g' or operation == '+':
            self.max_health = min(self.max_health, self.max_health + health)
        elif operation == 'l' or operation == '-':
            self.max_health = max(0, self.max_health - health)
        else:
            raise ValueError(f'Operation {operation} is invalid. Options are: m: modify, g: gain, l: lose.')

    def get_defense(self):
        return self.defense

    def has_health(self):
        return self.health > 0

    def calculate_damage(self, opponent):
        return max(0, self.attack - opponent.get_defense())
        # Do some wizardly math to account for def and other possible attributes

    def attack_entity(self, opponent):
        damage_given = self.calculate_damage(opponent)

        opponent.remove_health(damage_given)

        return damage_given


class Player(Entity):
    def __init__(self, attributes):
        super().__init__(attributes)

        self.inventory = attributes.get('inventory', [])
        self.money = attributes.get('money', 0)
        self.max_hunger = attributes.get('max_hunger', 100)
        self.hunger = attributes.get('hunger') if attributes.get('hunger', '') else self.max_hunger
        self.max_thirst = attributes.get('max_thirst', 100)
        self.thirst = attributes.get('thirst') if attributes.get('thirst', '') else self.max_thirst
        self.max_stamina = attributes.get('max_stamina', 1)
        self.stamina = attributes.get('stamina') if attributes.get('stamina', '') else self.max_stamina
        self.exp = attributes.get('exp', 0)

        active_entities['player'] = self

    def gain_exp(self, experience):
        self.exp += experience

    def get_exp(self):
        return self.exp

    def attack_entity(self, opponent):
        damage = self.calculate_damage(opponent)
        opponent.remove_health(damage)

        if not opponent.has_health():
            self.gain_exp(opponent.death_exp)

    def get_inventory(self):
        return self.inventory

    def get_item_from_inventory(self, item_id):
        try:
            return self.inventory[item_id]
        except:
            return None

    def acquire_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)
    
    def get_stats(self):
        print('Health:', str(self.health) + '/' + str(self.max_health))
        print('Hunger:', str(self.hunger) + '/' + str(self.max_hunger))
        print('Thirst:', str(self.thirst) + '/' + str(self.max_thirst))
        print('Stamina:', str(self.stamina) + '/' + str(self.max_stamina))
        print('Experience Points:', self.exp)
        print('Money:', self.money)

    def get_amount_of_item(self, item):
        instances = 0
        for instance in self.get_inventory():
            if instance.id == item.id:
                instances += 1
        return instances

    # def modify_attributes(self, attributes):
    #     self.max_hunger = attributes.get('max_hunger') if attributes.get('max_hunger', '') else self.max_hunger
    #     self.hunger = attributes.get('hunger') if attributes.get('hunger', '') else self.hunger
    #     self.max_thirst = attributes.get('max_thirst') if attributes.get('max_thirst', '') else self.max_thirst
    #     self.thirst = attributes.get('thirst') if attributes.get('thirst', '') else self.thirst
    #     self.max_stamina = attributes.get('max_stamina') if attributes.get('max_stamina', '') else self.max_stamina
    #     self.stamina = attributes.get('stamina') if attributes.get('stamina', '') else self.stamina

    # def gain_hunger(self, hunger):
    #     self.hunger = min(self.max_hunger, self.hunger + hunger)

    def modify_hunger(self, hunger, operation='m'):
        if operation == 'm' or operation == '=':
            self.hunger = hunger
        elif operation == 'g' or operation == '+':
            self.hunger = min(self.hunger, self.hunger + hunger)
        elif operation == 'l' or operation == '-':
            self.hunger = max(0, self.hunger - hunger)
        else:
            raise ValueError(f'Operation {operation} is invalid. Options are: m: modify, g: gain, l: lose.')

    def modify_max_hunger(self, hunger, operation='m'):
        if operation == 'm' or operation == '=':
            self.max_hunger = hunger
        elif operation == 'g' or operation == '+':
            self.max_hunger = min(self.max_hunger, self.max_hunger + hunger)
        elif operation == 'l' or operation == '-':
            self.max_hunger = max(0, self.max_hunger - hunger)
        else:
            raise ValueError(f'Operation {operation} is invalid. Options are: m: modify, g: gain, l: lose.')
    
    # def lose_hunger(self, hunger):
    #     self.hunger = max(0, self.hunger - hunger)

    # def gain_thirst(self, thirst):
    #     self.thirst = min(self.max_hunger, self.thirst + thirst)
    
    def modify_thirst(self, thirst, operation='m'):
        if operation == 'm' or operation == '=':
            self.thirst = thirst
        elif operation == 'g' or operation == '+':
            self.thirst = min(self.thirst, self.thirst + thirst)
        elif operation == 'l' or operation == '-':
            self.thirst = max(0, self.thirst - thirst)
        else:
            raise ValueError(f'Operation {operation} is invalid. Options are: m: modify, g: gain, l: lose.')

    def modify_max_thirst(self, thirst, operation='m'):
        if operation == 'm' or operation == '=':
            self.max_thirst = thirst
        elif operation == 'g' or operation == '+':
            self.max_thirst = min(self.max_thirst, self.max_thirst + thirst)
        elif operation == 'l' or operation == '-':
            self.max_thirst = max(0, self.max_thirst - thirst)
        else:
            raise ValueError(f'Operation {operation} is invalid. Options are: m: modify, g: gain, l: lose.')

    # def lose_thirst(self, thirst):
    #     self.hunger = max(0, self.thirst + thirst)

    # def gain_stamina(self, stamina):
        # self.hunger = min(self.max_stamina, self.stamina + stamina)

    def modify_stamina(self, stamina, operation='m'):
        if operation == 'm' or operation == '=':
            self.stamina = stamina
        elif operation == 'g' or operation == '+':
            self.stamina = min(self.stamina, self.stamina + stamina)
        elif operation == 'l' or operation == '-':
            self.stamina = max(0, self.stamina - stamina)
        else:
            raise ValueError(f'Operation {operation} is invalid. Options are: m: modify, g: gain, l: lose.')

    def modify_max_stamina(self, stamina, operation='m'):
        if operation == 'm' or operation == '=':
            self.max_stamina = stamina
        elif operation == 'g' or operation == '+':
            self.max_stamina = min(self.max_stamina, self.max_stamina + stamina)
        elif operation == 'l' or operation == '-':
            self.max_stamina = max(0, self.max_stamina - stamina)
        else:
            raise ValueError(f'Operation {operation} is invalid. Options are: m: modify, g: gain, l: lose.')

    # def lose_stamina(self, stamina):
        # self.stamina = max(0, self.stamina + stamina)

class Enemy(Entity):
    def __init__(self, attributes):
        super().__init__(attributes)

        self.death_exp = attributes.get('death_exp', 0)

        # active_entities[self.name] = 
        # Need to add multiple enemies to active entities with id

    def destroy_object(self):
        del self

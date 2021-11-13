from ..main import active_entities

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

    def get_health(self):
        return self.health

    def remove_health(self, damage_taken):
        self.health -= damage_taken

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

        self.inventory = attributes.get('inventory', {})
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


class Enemy(Entity):
    def __init__(self, attributes):
        super().__init__(attributes)

        self.death_exp = attributes.get('death_exp', 0)

        # active_entities[self.name] = 
        # Need to add multiple enemies to active entities with id

    def destroy_object(self):
        del self


class Player:
    def __init__(self, name):
        # TODO: create some sort of stats and assign them on creation.
        # Stats should be able to change as the character develops
        # self.stats = []
        self.attackPower = 10
        self.hp = 50
        self.defense = 3
        # TODO: during character creation, allow the player to enter the name.
        self.name = name
        # character starts at level one.
        # TODO: figure out the correlation between stats and levels. What exactly does the level mean for the character?
        # Does the level influence the stats of the player? Does it mean that they can use better gear? Both?
        self.level = 1
        # TODO: figure out some more attributes to add to the player. Equipment? Inventory?

    def attack(self, target):
        target.roll_defense(self.attackPower)

    def roll_defense(self, incoming_attack):
        # defensive formula will need extended tweaking to get right. Probably needs to scale down with higher numbers.
        # at the moment all it does is reduce damage linearly, which does not make for good scaling later on in the game
        self.hp = (self.hp - (incoming_attack - self.defense))

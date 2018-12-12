
# at the moment this class only describes the one enemy for testing purposes. Later I intend to expand this by making
# it a parent class and instantiating the specific creatures in a way that they can inherit this main class.


class Enemy:
    def __init__(self):
        self.hp = 50
        # need to figure out how to make these stats relevant. Attack is self-explanatory, but defense needs some
        # sort of formula to work.
        self.attackPower = 7
        self.defense = 3

        self.name = "Grunt"

    def attack(self, target):
        target.roll_defense(self.attackPower)

    def roll_defense(self, incoming_attack):
        # defensive formula will need extended tweaking to get right. Probably needs to scale down with higher numbers.
        # at the moment all it does is reduce damage linearly, which does not make for good scaling later on in the game
        self.hp = (self.hp - (incoming_attack - self.defense))

    def take_turn(self, target):
        # This behavior is a complete placeholder. I need to give the AI more options before I can have it choose.
        self.attack(target)


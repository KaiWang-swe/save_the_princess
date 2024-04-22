class Character:
    def __init__(self, strength=5):
        self.strength = strength

    def update_strength(self, delta):
        if self.strength+delta>=1:
            self.strength += delta 
        else:
            self.strength = 1
    
class Hero(Character):
    def __init__(self, strength=5, equip_sword=False):
        super().__init__(strength)
        self.equip_sword = equip_sword

class Yeti(Character):
    def __init__(self,strength=3):
        super().__init__(strength)

class Dragon(Character):
    def __init__(self, strength=8):
        super().__init__(strength)
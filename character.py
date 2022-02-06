class Character():
    def __init__(self, name: str, attack: int, health: int, speed: int, playable: bool):
        self.name = name
        self.attack = attack
        self.health = health
        self.speed = speed
        self.playable = playable
        self.alive = True

    def kill(self):
        self.alive = False

    def take_damage(self, damage: int) -> bool:
        self.health -= damage
        if self.health <= 0:
            self.alive = False
            return True
        else:
            return False
    #If self.alive False, then should also be removed from squad
    
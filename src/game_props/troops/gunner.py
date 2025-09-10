
class gunner:
    def __init__(self, health, damage, defence, mov_points, debug=None):
        self.health = health
        self.mov_points = mov_points
        self.defence = defence
        self.damage = damage

    def attack(self, enemy):
        damage = self.damage
        defe = enemy.defence

        while damage >= 0:
            if enemy.defence != 0:
                enemy.defence -= damage
                damage -= defe
                if self.debug != None:
                    print(f"{enemy.defence}\n{damage}\n{defe}")

            else:
                enemy.health -= damage
                if self.debug != None:
                    print(enemy.health)

    def move(self, current_hex, ):
         pass
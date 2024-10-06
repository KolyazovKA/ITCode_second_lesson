from random import randint

class Person():
    def __init__(self, health: int, damage: int, armor: int):
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self) -> int:
        return self.damage

    def _get_damage(self, damage:int) -> None:
        if damage < self.armor:
            self.armor -= damage
        else:
            self.armor = 0
            if self.health < self.damage - self.armor:
                self.health = 0
                return
            self.health -= self.damage - self.armor

    def _is_death(self) -> bool:
        if self.health == 0:
            return True
        else:
            return False


class Player(Person):
    def __init__(self, health: int, damage: int, armor: int):
        super().__init__(health, damage, armor)

    def alive(self) -> bool:
        if self._is_death():
            print("Игрок погиб")
            return False
        else:
            return True

    def get_damage(self, damage: int):
        super()._get_damage(damage)
        print(f'''Игрок атакован.\n
                Здоровье: {self.health}\n
                Броня: {self.armor}''')


class Enemy(Person):
    def __init__(self, health: int, damage: int, armor: int):
        super().__init__(health, damage, armor)

    def alive(self):
        if self._is_death():
            print("Враг погиб")
            return False
        else:
            return True
    
    def get_damage(self, damage: int):
        self._get_damage(damage)
        print(f'''Враг атакован.\n
                Здоровье: {self.health}\n
                Броня: {self.armor}''')


class Game():
    def __init__(self, player: Player, enemy: Enemy):
        self.player = player
        self.enemy = enemy

        print(f'''\t\tИгрок\t\tВраг\n
                Здоровье: {self.player.health}\tЗдоровье: {self.enemy.health}\n
                Броня: {self.player.armor}\tБроня: {self.enemy.armor}\n
                Урон: {self.player.damage}\tУрон: {self.enemy.damage}''')

    def fight(self):
        while True:
            player_attack = self.player.attack()
            self.enemy.get_damage(player_attack)

            if not self.enemy.alive():
                print('Победил игрок')
                break
            
            enemy_attack = self.enemy.attack()
            self.player.get_damage(enemy_attack)

            if not self.player.alive():
                print('Победил враг')
                break


if __name__ == '__main__':
    
    player = Player(randint(50, 100), randint(5, 20), randint(10, 30))
    enemy = Enemy(health=randint(50, 100), damage=randint(5, 20), armor=randint(10, 30))

    game = Game(player, enemy)
    game.fight()
    

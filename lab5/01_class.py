class Dragon:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def talk(self):
        print(self.name, 'health', self.health, '. Hit me!')


def main():
    dragon_list = [Dragon('Smog'), Dragon('Hidra')]
    finish = False
    while not finish:
        dragon = dragon_list[0]
        dragon.talk()
        damage = int(input())
        dragon.get_damage(damage)
        if not dragon.is_alive():
            dragon_list.pop(0)
        if not dragon_list:
            finish = True
    print('YOU ARE WIN!')


main()

import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """Атакует другого героя."""
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")

    def is_alive(self):
        """Проверяет, жив ли герой."""
        return self.health > 0


class Game:
    def __init__(self):
        self.player = Hero("Игрок")
        self.computer = Hero("Компьютер")

    def start(self):
        """Запускает игру."""
        print("Начинается битва!")
        while self.player.is_alive() and self.computer.is_alive():
            # Ход игрока
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден! {self.player.name} выиграл!")
                break

            # Ход компьютера
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} побежден! {self.computer.name} выиграл!")
                break

            # Вывод текущего состояния
            print(f"Здоровье {self.player.name}: {self.player.health}")
            print(f"Здоровье {self.computer.name}: {self.computer.health}")
            print("-" * 30)


# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.start()
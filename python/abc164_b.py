from dataclasses import dataclass


@dataclass
class Monster:
    health: int
    strength: int

    def attack(self, other: "Monster"):
        other.health -= self.strength

    def is_dead(self) -> bool:
        return self.health <= 0


def battle(first: Monster, second: Monster) -> bool:
    while True:
        first.attack(second)
        if second.is_dead():
            return True

        second.attack(first)
        if first.is_dead():
            return False


def main():
    a, b, c, d = map(int, input().split())

    t_monster = Monster(health=a, strength=b)
    a_monster = Monster(health=c, strength=d)

    if battle(t_monster, a_monster):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()

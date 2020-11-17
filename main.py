class Animal:
    def __init__(animal, name, gender, weight=0, sound='classic'):
        animal.name = name
        animal.gender = gender
        animal.weight = weight
        animal.sound = sound

    def eat(animal, food):
        animal.weight += food
        print(f"{animal.name} ate 1 piece of food, it's weight now is {animal.weight}")

    def say(animal, repeats=1):
        print(animal.sound * repeats)


class Milkable(Animal):
    def __init__(animal, name, gender, weight):
        super().__init__(name, gender, weight)

    def milk(animal):
        print(f'{animal.name} has been milked')


class Cutable(Animal):
    def __init__(animal, name, gender, weight):
        super().__init__(name, gender, weight)

    def cut(animal):
        print(f"{animal.name} has been cut")


class EggCollectable(Animal):
    def __init__(animal, name, gender, weight):
        super().__init__(name, gender, weight)

    def collect_eggs(animal):
        print(f"{animal.name}'s eggs have been collected ")


class Cow(Milkable):
    def __init__(animal, name, gender, weight=0):
        super().__init__(name, gender, weight)
        animal.sound = 'MOO'


class Goat(Milkable):
    def __init__(animal, name, gender, weight=0):
        super().__init__(name, gender, weight)
        animal.sound = 'Maa'


class Hen(EggCollectable):
    def __init__(animal, name, gender, weight=0):
        super().__init__(name, gender, weight)
        animal.sound = 'Cluck'


class Goose(EggCollectable):
    def __init__(animal, name, gender, weight=0):
        super().__init__(name, gender, weight)
        animal.sound = 'Honk'


class Duck(EggCollectable):
    def __init__(animal, name, gender, weight=0):
        super().__init__(name, gender, weight)
        animal.sound = 'Quack'


class Sheep(Cutable):
    def __init__(animal, name, gender, weight=0):
        super().__init__(name, gender, weight)
        animal.sound = 'Baa'


sery = Goose('Серый', 'male', 15)
bely = Goose('Белый', 'male', 17)
manka = Cow('Манька', 'female', 100)
barash = Sheep('Барашек', 'male', 70)
kudrya = Sheep('Кудрявый', 'male', 73)
koko = Hen('Ко-ко', 'female', 3)
kuka = Hen('Кукареку', 'female', 2)
roga = Goat('Рога', 'female', 60)
kopita = Goat('Копыта', 'female', 62)
kryakwa = Duck('Кряква', 'female', 7)
max_weight = 0
animal_list = [sery, bely, manka, barash, kudrya, koko, kuka, roga, kopita, kryakwa]

for animal in animal_list:
    animal.eat(1)
    if isinstance(animal, Milkable):
        animal.milk()
    elif isinstance(animal, EggCollectable):
        animal.collect_eggs()
    else:
        animal.cut()
    animal.say(1)

    if animal.weight >= max_weight:
        max_weight_name = animal.name
        max_weight = animal.weight
print(f"The heaviest animal is {max_weight_name}. It's weight is {max_weight}.")

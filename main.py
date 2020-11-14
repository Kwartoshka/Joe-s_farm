# class Cow:
#     def __init__(animal, name,  gender, weight, ):
#         animal.name = name
#         animal.gender = gender
#         animal.weight = weight
#         animal.sound = 'MOO'
#
#     def eat(animal, food):
#         animal.weight += food
#
#     def milk(animal):
#         print(f'{animal.name} has been milked')
#
#     def say(animal, repeats = 1):
#         print(animal.name * repeats)
#
#
# class Goat:
#     def __init__(animal, name,  gender, weight, ):
#         animal.name = name
#         animal.gender = gender
#         animal.weight = weight
#         animal.sound = 'Maa'
#
#     def eat(animal, food):
#         animal.weight += food
#
#     def milk(animal):
#         print(f'{animal.name} has been milked')
#
#     def say(animal, repeats = 1):
#         print(animal.sound * repeats)
#
#
# class Hen:
#     def __init__(animal, name,  gender, weight, ):
#         animal.name = name
#         animal.gender = gender
#         animal.weight = weight
#         animal.sound = 'Cluck'
#
#     def eat(animal, food):
#         animal.weight += food
#
#     def collect_eggs(animal):
#         print(f"{animal.name}'s eggs have been collected ")
#
#     def say(animal, repeats = 1):
#         print(animal.sound * repeats)
#
#
# class Goose:
#     def __init__(animal, name,  gender, weight, ):
#         animal.name = name
#         animal.gender = gender
#         animal.weight = weight
#         animal.sound = 'Honk'
#
#     def eat(animal, food):
#         animal.weight += food
#
#     def collect_eggs(animal):
#         print(f"{animal.name}'s eggs have been collected ")
#
#     def say(animal, repeats = 1):
#         print(animal.sound * repeats)
#
#
# class Duck:
#     def __init__(animal, name,  gender, weight, ):
#         animal.name = name
#         animal.gender = gender
#         animal.weight = weight
#         animal.sound = 'Quack'
#
#     def eat(animal, food):
#         animal.weight += food
#
#     def collect_eggs(animal):
#         print(f"{animal.name}'s eggs have been collected")
#
#     def say(animal, repeats = 1):
#         print(animal.sound * repeats)
#
# class Sheep:
#     def __init__(animal, name, gender, weight, ):
#         animal.name = name
#         animal.gender = gender
#         animal.weight = weight
#         animal.sound = 'Cluck'
#
#     def eat(animal, food):
#         animal.weight += food
#
#     def cut(animal):
#         print(f"{animal.name} has been cut")
#
#     def say(animal, repeats = 1):
#         print(animal.sound * repeats)
#
#
# sery = Goose('Серый', 'male', 15)
# bely = Goose('Белый', 'male', 17)
# manka = Cow('Манька', 'female', 100)
# barash = Sheep('Барашек', 'male', 70)
# kudrya = Sheep('Кудрявый', 'male', 73)
# koko = Hen('Ко-ко', 'female', 3)
# kuka = Hen('Кукареку', 'female', 2)
# roga = Goat('Рога', 'female', 60)
# kopita = Goat('Копыта', 'female', 62)
# kryakwa = Duck('Кряква', 'female', 7)
#
# animal_list = [sery, bely, manka, barash, kudrya, koko, kuka, roga, kopita, kryakwa]
#
# for animal in animal_list:
#     animal.eat(1)
#     print(f"{animal.name}'s weight is now animal.weight"
#     if isinstance(animal, Cow) or isinstance(animal, Goat):
#         animal.milk
#     elif isinstance(animal, Hen) or isinstance(animal, Goose) or isinstance(animal, Duck):
#         animal.collect_eggs()
#     else:
#         animal.cut()
#     animal.say()

a = 1
if a == 1
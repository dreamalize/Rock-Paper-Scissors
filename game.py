import random
random.seed()


def get_rating(name):
    file = open('rating.txt', 'r', encoding='utf-8')
    gamers = {}
    for line in file:
        gamer = line.split()
        gamers[gamer[0]] = int(gamer[1])
    file.close()
    if name in gamers:
        return name, gamers[name]
    else:
        return name, 0


def win_options():
    user_input = input()
    if user_input == "":
        user_input = "rock,paper,scissors"
    list = user_input.split(",")
    temp_list = list[:]
    for i in range(len(list)):
        element = temp_list.pop(0)

        WIN_OPTIONS[element] = []
        start = int(len(temp_list) / 2)
        loosers = temp_list[start:]
        for i in loosers:
            WIN_OPTIONS[element].append(i)
        temp_list.append(element)
    return list



class Player:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        print("Hello, {}".format(self.name))

    def game(self):
        list_options = win_options()
        print("Okay, let's start")
        while True:

            comp_choice = random.choice(list_options)
            user_input = input()
            if user_input == "!exit":
                print("Buy!")
                break
            elif user_input == "!rating":
                print(f"Your rating: {self.rating}")
            elif user_input not in WIN_OPTIONS:
                print("Invalid input")
            else:
                if user_input == comp_choice:
                    self.rating += 50
                    print("There is a draw ({})".format(comp_choice))
                elif user_input in WIN_OPTIONS[comp_choice]:
                    print("Sorry, but the computer chose {}".format(comp_choice))
                else:
                    self.rating += 100
                    print("Well done. The computer chose {} and failed".format(comp_choice))


WIN_OPTIONS = {}


name_input = input("Enter your name: ")
player_name, rating = get_rating(name_input)
person = Player(player_name, rating)
Player.game(person)

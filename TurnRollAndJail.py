import random
player = 0
turn = 0
game = 0
double = 0

def dice():
    global dice_roll
    global dice_roll_2

    dice_roll = random.randint(1,6)
    dice_roll_2 = random.randint(1, 6)
    roll_result = dice_roll + dice_roll_2
    print("Dice 1 is: " + str(dice_roll))
    print("Dice 2 is: " + str(dice_roll_2))
    print("Roll is: " + str(roll_result))

    return dice_roll
    return dice_roll_2
    return roll_result

while game == 0:
    while player == 0:
        print("Player 1")
        print(double)
        dice()  # Picks two numbers
        if dice_roll == dice_roll_2:  # Checks if numbers are equal
            print("Double")
            double += 1  # if numbers are equal, increase double number by 1
            print(double)
            dice()
            if dice_roll == dice_roll_2:
                print("Double")
                double += 1
                print(double)
                dice()
                if double == 2 and dice_roll == dice_roll_2:
                    double += 1
                    print("Double")
                    print(double)
                    print("Go to jail!")
                    double = 0
                    print("Double reset")
                else:
                    double == 0
                    print("Double reset")
            else:
                double == 0
                print("Double reset")
        else:
            double == 0
            print("Double reset")
        turn = int(input("End of your turn? Press 1: "))
        if turn == 1:
            break

    while player == 0:
        print("Player 1")
        print(double)
        dice()  # Picks two numbers
        if dice_roll == dice_roll_2:  # Checks if numbers are equal
            print("Double")
            double += 1  # if numbers are equal, increase double number by 1
            print(double)
            dice()
            if dice_roll == dice_roll_2:
                print("Double")
                double += 1
                print(double)
                dice()
                if double == 2 and dice_roll == dice_roll_2:
                    double += 1
                    print("Double")
                    print(double)
                    print("Go to jail!")
                    double = 0
                    print("Double reset")
                else:
                    double == 0
                    print("Double reset")
            else:
                double == 0
                print("Double reset")
        else:
            double == 0
            print("Double reset")
        turn = int(input("End of your turn? Press 1: "))
        if turn == 1:
            break















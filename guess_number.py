import random

counter = 1
computer_number = random.randint(10, 40)
while True:
    user_number = int(input("Enter your number :"))
    if computer_number == user_number:
        print("you win !")
        print("❤️❤️❤️❤️❤️")
        break
    elif computer_number > user_number:
        print("go up")
        counter +=1
    elif computer_number < user_number:
        print("go down")
        counter +=1

print("tedad hades : ",counter)
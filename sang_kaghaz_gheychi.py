import random

count = int(input("Enter your Number of games : "))
computer_number = 0
user_number = 0
mosavi = 0

for i in range(count):
    user_choice = input("Enter your choice :")
    numbers = random.randint(1, 3)
    computer_choice = ""
    if numbers == 1:
        computer_choice = "sang"
    elif numbers == 2:
        computer_choice = "kaghaz"
    elif numbers == 3:
        computer_choice = "gheychi"

    if computer_choice == "sang" and user_choice == "sang":
        print("computer :", computer_choice, "user : ", user_choice)
        print("mosavi")
        mosavi +=1
    elif computer_choice == "sang" and user_choice == "kaghaz":
        print("computer :", computer_choice, "user : ", user_choice)
        print("user win")
        user_number += 1
    elif computer_choice == "sang" and user_choice == "gheychi":
        print("computer :", computer_choice, "user : ", user_choice)
        print("computer win")
        computer_number += 1
    elif computer_choice == "kaghaz" and user_choice == "sang":
        print("computer :", computer_choice, "user : ", user_choice)
        print("computer win")
        computer_number +=1
    elif computer_choice == "kaghaz" and user_choice == "kaghaz":
        print("computer :", computer_choice, "user : ", user_choice)
        print("mosavi")
        mosavi += 1
    elif computer_choice == "kaghaz" and user_choice == "gheychi":
        print("computer :", computer_choice, "user : ", user_choice)
        print("user win")
        user_number += 1
    elif computer_choice == "gheychi" and user_choice == "sang":
        print("computer :", computer_choice, "user : ", user_choice)
        print("user win")
        user_number +=1
    elif computer_choice == "gheychi" and user_choice == "gheychi":
        print("computer :", computer_choice, "user : ", user_choice)
        print("mosavi")
        mosavi += 1
    elif computer_choice == "gheychi" and user_choice == "kaghaz":
        print("computer :", computer_choice, "user : ", user_choice)
        print("computer win")
        computer_number += 1


print(f"Result : computer = {computer_number} user = {user_number} equal = {mosavi}")
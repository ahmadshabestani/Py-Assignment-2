time = int(input("Enter seconds: "))
hour = time / 3600
minutes = (time / 60) % 60
seconds = time % 60

print(f"{int(hour)}:{int(minutes)}:{seconds}")


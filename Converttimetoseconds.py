hour = int(input("Enter hour : "))
minutes = int(input("Enter minutes : "))
seconds = int(input("Enter Seconds : "))

minutes = minutes * 60
hour1 = hour * 60
hour2 = hour1 * 60

result = minutes + hour2 + seconds

print(result)

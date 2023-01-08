student = 0
counter = 0
while True:
    student_number = input("Enter your number : ")
    if student_number == "exit":
        break
    else:
        student = student + float(student_number)
        counter += 1

avrage = student / counter


print(avrage)
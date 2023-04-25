print("Welcome to find highest score in class")
students_score = input("Enter the score of each student like 84 56 89 90 ")
students_score = students_score.split()
# students_score = int(students_score)
for n in range(0, len(students_score)):
    students_score[n] = int(students_score[n])
print(students_score)
#students_score = ["40", "50", "20", "10", "65"]
a = 0
b = 0
a = int(a)
b = int(b)
for a in students_score:
    print(a)
    a = int(a)
    if a > b:
        b = a
        print("a is bigger so storing it in variables b")
    else:
        print("value of a is small")
print("max number is ", b)
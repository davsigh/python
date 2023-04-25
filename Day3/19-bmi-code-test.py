print("Welcome to BMI calculator2.0")
weight = int(input("Please Enter your weight "))
height = float(input("Please Enter your height "))
bmi = weight/(height ** 2)
print("My BMI is ", round(bmi,2))
if bmi <= 18.5:
    print("you are under weight")
elif bmi >=18.5 and bmi <=25:
    print("you have normal weight")
elif bmi >=25 and bmi <=30:
    print("you are over weight")
elif bmi >=30 and bmi <=35:
    print("you are obese")
else:
    print("you are clinically obese")

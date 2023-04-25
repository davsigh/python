print("Welcome to find leap year")
year = int(input("Enter the year"))
#leap_year = year%4
if year%4 == 0:
    print("first condition pass for leap year")
    if year%100 != 0:
        print("its a leap year because divide by 4 and not divided by 100")
    else:
        if year%400 == 0:
           print("its a leap year because divided by 400")
        else:
            print("its not a leap year bcoz not divided by 400 but divided by 100")
else:
    print ("its not a leap year because not devided by 4")
    

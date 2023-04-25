age = input("Enter your age ")
max_age = input("enter your age you wist to live")
max_age=int(max_age)
total_weeks=max_age*52
total_days=max_age*365

print(type(total_weeks),type(total_days))
print(total_days,total_weeks)
print(type(age))
print(age)
age = int(age)
year_left = max_age - age
days_left=total_days - (age*365)
weeks_left=total_weeks - (age*52)
print(type(age),type(year_left),type(days_left),type(weeks_left))
print(f"you have {days_left} days, {weeks_left} weeks, and {year_left} years left")

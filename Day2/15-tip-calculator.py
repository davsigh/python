print(" Welcome to the tip calculator")
total_bill= input("What was the total bill ")
per_tip = input("how much % of tip you want to give? 10, 12, or 15? ")
total_people = input("total number of people ")

total_bill_with_tip = float(total_bill) + float(total_bill) * (int(per_tip)/100)
print("Total bill after adding tip is ", total_bill_with_tip)
pay_bill = round(total_bill_with_tip/int(total_people),2)
print("how much each person to pay",pay_bill)
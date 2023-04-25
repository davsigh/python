print("Welcome to Love Calculator")
ur_name = input("Enter your name ").lower()
print ("Your name is ",ur_name)
her_name = input("Enter your love name ").lower()
print("Her name is ",her_name)
count = 0
true_count = 0
love_count = 0
count = ur_name.count("t")
true_count += count
count = ur_name.count("r")
true_count += count
count = ur_name.count("u")
true_count += count
count = ur_name.count("e")
true_count += count
count = her_name.count("t")
true_count += count
count = her_name.count("r")
true_count += count
count = her_name.count("u")
true_count += count
count = her_name.count("e")
true_count += count
print(true_count)
count = ur_name.count("l")
love_count += count
count = ur_name.count("o")
love_count += count
count = ur_name.count("v")
love_count += count
count = ur_name.count("e")
love_count += count
count = her_name.count("l")
love_count += count
count = her_name.count("o")
love_count += count
count = her_name.count("v")
love_count += count
count = her_name.count("e")
love_count += count
print(love_count)
true_count_str = str(true_count)
love_count_str = str(love_count)
print("your score is before integer",true_count_str + love_count_str)
percentage=true_count_str+love_count_str
print(percentage)

# if  ur_name.count("t"):
#     count += 1
# if ur_name.count("r"):
#     count += 1
# if ur_name.count("u"):
#     count += 1
# if ur_name.count("e"):
#     count += 1
# if her_name.count("t"):
#     count += 1
# if her_name.count("r"):
#     count += 1
# if her_name.count("u"):
#     count += 1
# if her_name.count("e"):
#     count += 1
# print(count)
# love = 0
# if ur_name.count("l"):
#     love += 1
# if ur_name.count("o"):
#     love += 1
# if ur_name.count("v"):
#     love += 1
# if ur_name.count("e"):
#     love += 1
# if her_name.count("l"):
#     love += 1
# if her_name.count("o"):
#     love += 1
# if her_name.count("v"):
#     love += 1
# if her_name.count("e"):
#     love += 1
# print(love)
# percentage = str(count)+str(love)
# print(percentage)
score=int(percentage)
if score < 10 or score > 90:
    print("your score is " , percentage + "you go together like coke and mentos")
    if score > 40 and score < 60:
        print("Your score is ", percentage + " you are alright together")
else:
    print("your score is ", percentage)
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want to put the treasure ")
position_a=position[0]
position_b=position[1]
print(str(position_a)+str(position_b))
print(position_a)
print(position_b)

horizontal = int(position_a)
vertical = int(position_b)

# selected_row = map[vertical - 1]
# selected_row[horizontal-1] = "X"
map[vertical - 1][horizontal-1]="X"
print(f"{row1}\n{row2}\n{row3}")
student_heights = [180, 124, 160, 133, 158]
sum_heights = 0
counter = 0
for a in student_heights:
    print(a)
    sum_heights += a
    counter += 1
print("Sum of all heights ",sum_heights)
print(counter)
x = student_heights.count
average_heights = sum_heights/counter
print("Average Height is ",round(average_heights))
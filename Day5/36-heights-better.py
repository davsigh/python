student_heights = [180, 124, 160, 133, 158]

# Use the built-in function `len` to get the number of elements in the list
num_students = len(student_heights)

# Use the built-in function `sum` to get the sum of all elements in the list
sum_heights = sum(student_heights)

# Calculate the average height
average_height = sum_heights / num_students

# Use f-strings to format the output string with the result rounded to the nearest integer
print(f"Sum of all heights: {sum_heights}")
print(f"Number of students: {num_students}")
print(f"Average height: {round(average_height)}")

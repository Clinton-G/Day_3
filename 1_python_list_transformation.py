# Task 1:


grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# sort in descending order
# print sorted list
grades.sort(reverse=True)
print(grades)

#----------------------------------------------------------------------------------------------------
# Task 2:

# Calculate Average Grade, then print it
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
average = sum(grades) / 10
print("The Average Grade is: ", (average))

#----------------------------------------------------------------------------------------------------
# Task 3:


grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

#replace grades < 80 with "Failed"

target_grade = grades.index (78)
grades[target_grade] = 'Failed'

target_grade = grades.index (76)
grades[target_grade] = 'Failed'

target_grade = grades.index (72)
grades[target_grade] = 'Failed'
# Print Results
print(grades)
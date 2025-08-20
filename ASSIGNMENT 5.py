
                            #task1


# Create a dictionary of student marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 88,
    "Ethan": 95
}

# Ask user for student name
student_name = input("Enter the student's name: ")

# Retrieve and display marks, or show error message if not found
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found in the records.")




                            #task2

    # Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Extract the first five elements using slicing
first_five = numbers[:5]

# Reverse the extracted elements
reversed_five = first_five[::-1]

# Print the results
print(f"Original list: {numbers}")
print(f"Extracted first five elements: {first_five}")
print(f"Reversed extracted elements: {reversed_five}")


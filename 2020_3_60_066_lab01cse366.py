# -*- coding: utf-8 -*-
"""2020-3-60-066_Lab01CSE366.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12hNFPda6-47-N_r9NeDDvgglmyzJUftr

Select Viva Students
1. Read the student IDs from a text file (e.g., student_ids.txt) containing
multiple student IDs, one per line, in the format YYYY-N-MM-xxx (e.g., 2024-1-05-
123).
"""

def read_student_ids(filename):
    try:
        with open(filename, 'r') as file:
            student_ids = file.readlines()
            # Strip any extra whitespace
            return [student_id.strip() for student_id in student_ids]
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []

# Printing file
filename = "student_ids.txt"
student_ids = read_student_ids(filename)

if student_ids:
    print("Student IDs from the file:")
    for student_id in student_ids:
        print(student_id)

"""2. Maintain a list of students who have not been selected yet.

"""

unselected_students = student_ids[:]
print("Students who have not been selected yet:")
for student_id in unselected_students:
        print(student_id)

"""3. Randomly select a student for viva from the list.

"""

import random
viva_counter = 0
selected_student = ""
def select_viva_students(student_ids):
    global viva_counter
    global selected_student
    if not student_ids:
        print("Error: No student IDs available to select.")
        return


    # Randomly select a student
    selected_student = random.choice(unselected_students)
    viva_counter += 1

    # Print the selected student's ID and viva number
    print(f"Selected Student: Viva #{viva_counter}: {selected_student}")
    return selected_student



if student_id in unselected_students:
    select_viva_students(student_ids)

"""4. Remove the selected student from the list."""

# Remove the selected student from the unselected list
unselected_students.remove(selected_student)
print("After removing selected student remaining students who have not been selected yet:")
for student_id in unselected_students:
        print(student_id)

"""5. Repeat steps 3 and 4 until all students have been picked."""

# Loop until all students are selected
while unselected_students:
    selected_student = select_viva_students(unselected_students)

    if selected_student:
        # Remove the selected student from the unselected_students list
        unselected_students.remove(selected_student)
        print(f"Viva #{viva_counter} complete: {selected_student} selected and removed.")
    else:
        print("No more students to select.")

"""6. When all students have been selected, reset the list to include all students
again.
"""

unselected_students = student_ids[:]
print("Reset Student list:")
for student_id in unselected_students:
        print(student_id)
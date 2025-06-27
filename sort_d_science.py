import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
student_details = [('Riyad', 9, 5.8), ('Osman', 8, 5.7), ('Ali', 7, 5.24), ('Ahmed', 7, 5.6), ('Hassan', 9, 5.9)]
students = np.array(student_details, dtype=data_type)
print("Original array:")
print(students)
print("\nSorted by class:\n", np.sort(students, order='class'))
print("\nSorted by height:\n", np.sort(students, order='height'))
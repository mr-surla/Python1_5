

# Task 1: Create a Dictionary of Student Marks
#
# Problem Statement: Write a Python program that:
# 1.   Creates a dictionary where student names are keys and their marks are values.
# 2.   Asks the user to input a student's name.
# 3.   Retrieves and displays the corresponding marks.
# 4.   If the student’s name is not found, display an appropriate message.



my_dict = {'Mike':45,'Alice':85,'Aman':75, 'Spiderman':95, 'Ironman':98, 'falcon':36 }

#print(my_dict['Mike'])


Student_name= input("Enter the Student's name ")
if Student_name in my_dict:
    print("{}'s marks:{}" .format(Student_name,my_dict[Student_name]))
else:
    print("Student not found")



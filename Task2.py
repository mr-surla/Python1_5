# Task 2: Demonstrate List Slicing
# Problem Statement: Write a Python program that:
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

list = []
for i in range(11):
    if i>0:
        list.append(i)

print('Original List :',list)

list_first_five = list[0:5]
print('Extracted first five elements :',list_first_five)
List_reverse = list_first_five
List_reverse.reverse()

print('Reversed extracted elements :',List_reverse)
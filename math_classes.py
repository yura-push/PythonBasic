math_class1 = int(input("Enter number of student`s in first class: "))
math_class2 = int(input("Enter number of student`s in second class: "))
math_class3 = int(input("Enter number of student`s in third class: "))

desks_for_two_students = (math_class1 + math_class2 + math_class3) // 2
remainding_desks = (math_class1 + math_class2 + math_class3) % 2

print("Total number of desks needed:", desks_for_two_students + remainding_desks)

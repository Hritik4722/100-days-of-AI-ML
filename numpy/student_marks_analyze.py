import numpy as np
# maths, eng, science

# student = np.array([[ 96,  45,  82],
#                     [ 65, 100,  58],
#                     [ 71,   8,  32],
#                     [ 29,  99,  51],
#                     [  7,   7,  26],
#                     [ 42,  69,   4],
#                     [ 42,  60,  84],
#                     [ 67,  76,   3],
#                     [ 75,  85,  93],
#                     [ 19,  79,  24]])


student = np.random.randint(0,101,size=(50,3))
print(student)
#Normal info about data

print("shape  of data ", student.shape)
print("All student marks in maths", student[:,0])
print("All student marks in English", student[:,1])
print("All student marks in Science", student[:,2])

#Average marks by students

student_num = 1
for i in student:
    print(f"student {student_num} average = {i.mean()}")
    student_num = student_num + 1

#total marks of each student with the topper

student_num2 = 1
topper_marks= 0
for i in student:
    sum = i.sum()
    if sum > topper_marks:
        topper_marks = sum
    print(f"student {student_num2} total marks = {sum}")
    student_num2= student_num2 + 1
print(f"Topper marks is {topper_marks}")

#average marks obtained in each subject

avg_marks_sub = np.array([student[:,0].mean(), student[:,1].mean(),student[:,2].mean()])
print("Average marks obtained in maths", avg_marks_sub[0])
print("Average marks obtained in English", avg_marks_sub[1])
print("Average marks obtained in Science", avg_marks_sub[2])

#easiest and hardest subject

easiest = avg_marks_sub.argmax()
hardest = avg_marks_sub.argmin()
print(f" hardest is {hardest} and easiest is {easiest}")
import pandas as pd

df = pd.read_csv("D:\AIML_python\pandas\student.csv")

#function to return topper name
def topper_name(max,subject):
    for i in range(0,10):
        maths = df.loc[i,subject]
        if maths == max:
            return (df.loc[i,"Name"])



#average of each student

average = []
for num in range(0,10):
    avg = df.iloc[num,1:4].mean()
    average.append(avg)
    
df["Average"] = average

#topper in each subject

max_m,max_e,max_s = df[["Maths","English","Science"]].max()
print("Topper of maths ",topper_name(max_m,"Maths"))
print("Topper of english ",topper_name(max_e,"English"))
print("Topper of science ",topper_name(max_s,"Science"))


#who scored more than 80 avg

honor_list = df[df["Average"] >= 80]
print(honor_list)

#grades assignment

grades = []
for i in range(0,10):
    f_grade = df.loc[i,"Average"]
    if f_grade < 50:
        grades.append("D")
    elif f_grade < 70:
        grades.append("C")
    elif f_grade < 85:
        grades.append("B")
    else:
        grades.append("A")
   
df["Grades"] = grades
print(df)

#export
# df.to_csv("D:\AIML_python\pandas\student_exported.csv")

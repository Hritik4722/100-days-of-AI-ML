import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\AIML_python\pand_mato\student.csv")


# Average
df["Average"] = df[["Maths", "English", "Science"]].apply(lambda row: row.mean(), axis=1)

#average of each subject
print(df[["Maths", "English", "Science"]].mean())

#above 75 in each subject
def more_t_75(subject):
    return df[df[subject] > 75].shape[0]

print(f"{more_t_75('Maths')} student scored more than 75 in mathematics")
print(f"{more_t_75('English')} student scored more than 75 in English")
print(f"{more_t_75('Science')} student scored more than 75 in Science")

#grade section
def grade(inp):
    if inp < 50:
        return "D"
    elif inp < 70:
        return "C"
    elif inp < 85:
        return "B"
    else:
        return "A"

df["Grade"] = df["Average"].apply(grade)

# total marks of each student
df["Total"] = df["Maths"]+df["Science"]+df["English"]

# df.to_csv("student_report.csv", index=False)

# visualization 

# average marks per subject
# x = ["Maths","English","Science"]
# y = df[["Maths", "English", "Science"]].mean()
# plt.bar(x,y,color="red",label="Average marks")
# plt.xlabel("Subjects")
# plt.ylabel("Average marks")
# plt.legend()
# plt.show()

#total marks per student
# x = df["Name"]
# y = df["Total"]
# plt.plot(x,y,marker="o",label="Student_Marks")
# plt.xlabel("Student name")
# plt.ylabel("Total marks")
# plt.legend()
# plt.show()
print(df)

#subplots method 1

fig, ax = plt.subplots(2,2,figsize=(10,5))

x_sub = ["Maths","English","Science"]
y_avg = df[["Maths", "English", "Science"]].mean()
ax[0,0].bar(x_sub,y_avg,color="red",label="Average marks")
ax[0,0].set_title("Average marks of student")
ax[0,0].set_xlabel("Subjects")
ax[0,0].set_ylabel("Average marks")
ax[0,0].legend()

x = df["Name"]
y = df["Total"]
ax[0,1].plot(x,y,marker="o",label="Student_Marks")
ax[0,1].set_xlabel("Student name")
ax[0,1].set_ylabel("Total marks")
ax[0,1].legend()

data_hist = df["Maths"]
ax[1,0].hist(data_hist,bins=5)


data_pie = df["Maths"]
data_name = df["Name"]
ax[1,1].pie(data_pie,labels=data_name,autopct='%1.1f%%')
ax[1,1].set_title("Maths marks distribution")
fig.suptitle("Marks analysis")

plt.tight_layout()
plt.savefig("Analysis.png",dpi=200,bbox_inches="tight")
plt.show()

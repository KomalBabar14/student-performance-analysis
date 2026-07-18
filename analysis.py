import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------
# Load Dataset
# ---------------------------------
df = pd.read_csv("data/students.csv")

# ---------------------------------
# Calculate Average
# ---------------------------------
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

# ---------------------------------
# Assign Grades
# ---------------------------------
def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

df["Grade"] = df["Average"].apply(assign_grade)

# ---------------------------------
# Statistics
# ---------------------------------
top_student = df.loc[df["Average"].idxmax()]
lowest_student = df.loc[df["Average"].idxmin()]
class_average = df["Average"].mean()

# Subject Toppers
math_topper = df.loc[df["Math"].idxmax()]
science_topper = df.loc[df["Science"].idxmax()]
english_topper = df.loc[df["English"].idxmax()]

# Pass Statistics
passed = len(df[df["Grade"] != "F"])
failed = len(df[df["Grade"] == "F"])
pass_percentage = (passed / len(df)) * 100

# ---------------------------------
# Console Report
# ---------------------------------
print("=" * 45)
print("      STUDENT PERFORMANCE REPORT")
print("=" * 45)

print(f"\nTotal Students : {len(df)}")
print(f"Class Average  : {class_average:.2f}")

print("\nOverall Performance")
print("-----------------------------")
print(f"Top Performer  : {top_student['Name']} ({top_student['Average']:.2f})")
print(f"Lowest Average : {lowest_student['Name']} ({lowest_student['Average']:.2f})")

print("\nSubject Toppers")
print("-----------------------------")
print(f"Math     : {math_topper['Name']} ({math_topper['Math']})")
print(f"Science  : {science_topper['Name']} ({science_topper['Science']})")
print(f"English  : {english_topper['Name']} ({english_topper['English']})")

print("\nPass Statistics")
print("-----------------------------")
print(f"Passed           : {passed}")
print(f"Failed           : {failed}")
print(f"Pass Percentage  : {pass_percentage:.1f}%")

print("\nGrade Distribution")
print("-----------------------------")
print(df["Grade"].value_counts())

# ---------------------------------
# Export Report
# ---------------------------------
df.to_csv("students_report.csv", index=False)

# ---------------------------------
# Chart 1 - Average Marks
# ---------------------------------
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Average"])
plt.title("Average Marks by Student")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/average_scores.png")
plt.close()

# ---------------------------------
# Chart 2 - Grade Distribution
# ---------------------------------
grade_counts = df["Grade"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    grade_counts,
    labels=grade_counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Grade Distribution")
plt.savefig("charts/grade_distribution.png")
plt.close()

# ---------------------------------
# Chart 3 - Subject Average
# ---------------------------------
subject_avg = df[["Math", "Science", "English"]].mean()

plt.figure(figsize=(6,4))
plt.bar(subject_avg.index, subject_avg.values)
plt.title("Average Score by Subject")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("charts/subject_distribution.png")
plt.close()

print("\n✔ Charts generated successfully.")
print("✔ students_report.csv exported successfully.")
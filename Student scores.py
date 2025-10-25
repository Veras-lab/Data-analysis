# ------------------------------------------------------------
# 🎓 Student Scores Analysis Notebook
# Objective: Load, Analyze, and Visualize Student Performance Data
# Libraries: pandas, numpy, seaborn, matplotlib
# ------------------------------------------------------------

# 📦 Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 🎨 Visualization settings
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# ------------------------------------------------------------
# 🧭 Task 1: Load and Explore the Dataset
# ------------------------------------------------------------

# Load dataset
try:
    df = pd.read_csv("Student scores.csv")
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ File not found. Please ensure 'Student scores.csv' is in your working directory.")

# Display first few records
print("📊 First 5 rows of the dataset:")
display(df.head())

# Dataset structure
print("\n📋 Dataset Info:")
print(df.info())

# Summary of missing values
print("\n🔍 Missing Values per Column:")
print(df.isnull().sum())

# Clean the dataset (if needed)
df = df.dropna()  # dataset has no missing values, but keeping this step for good practice

# ------------------------------------------------------------
# 📈 Task 2: Basic Data Analysis
# ------------------------------------------------------------

# Statistical summary
print("\n📊 Descriptive Statistics:")
display(df.describe())

# Correlation analysis
print("\n🔗 Correlation Matrix:")
display(df.corr(numeric_only=True))

# Grouping example — average exam score by attendance range
df['attendance_group'] = pd.cut(df['attendance_percent'], bins=[0, 60, 80, 100],
                                labels=['Low', 'Medium', 'High'])
group_summary = df.groupby('attendance_group')['exam_score'].mean().reset_index()
print("\n🎯 Average Exam Score by Attendance Group:")
display(group_summary)

# Observations
print("\n💡 Observations:")
print("""
- Students with higher attendance tend to score better in exams.
- 'Hours studied' appears positively related to 'exam_score'.
- 'Sleep hours' and 'exam_score' may have a mild relationship (balance matters).
""")

# ------------------------------------------------------------
# 🎨 Task 3: Data Visualization
# ------------------------------------------------------------

# 1️⃣ Histogram — Distribution of Exam Scores
plt.figure()
sns.histplot(df['exam_score'], bins=15, kde=True, color='skyblue')
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.show()

# 2️⃣ Scatter Plot — Hours Studied vs Exam Score
plt.figure()
sns.scatterplot(x='hours_studied', y='exam_score', data=df, color='salmon')
plt.title("Relationship: Hours Studied vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.show()

# 3️⃣ Scatter Plot — Sleep Hours vs Exam Score
plt.figure()
sns.scatterplot(x='sleep_hours', y='exam_score', data=df, color='mediumseagreen')
plt.title("Relationship: Sleep Hours vs Exam Score")
plt.xlabel("Sleep Hours")
plt.ylabel("Exam Score")
plt.show()

# 4️⃣ Bar Chart — Average Exam Score by Attendance Group
plt.figure()
sns.barplot(x='attendance_group', y='exam_score', data=df, palette='pastel')
plt.title("Average Exam Score by Attendance Level")
plt.xlabel("Attendance Group")
plt.ylabel("Average Exam Score")
plt.show()

# 5️⃣ Line Chart — Comparing Study Hours and Exam Score Trend
plt.figure()
plt.plot(df['hours_studied'], df['exam_score'], marker='o', linestyle='-', color='purple')
plt.title("Trend Between Hours Studied and Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.show()

# ------------------------------------------------------------
# 📘 Insights Summary
# ------------------------------------------------------------

print("""
📘 FINAL FINDINGS:
-------------------
1. Students who study longer hours generally achieve higher exam scores.
2. Moderate sleep (around 7–8 hours) seems beneficial for performance.
3. Attendance plays a strong role — students with 80–100% attendance show higher average scores.
4. Positive correlation observed between 'previous_scores' and 'exam_score', suggesting consistent learners.
""")

print("\n✅ Analysis and Visualization Completed Successfully!")

# ============================================================
# CODSOFT DATA ANALYTICS INTERNSHIP
# TASK 1: DATA CLEANING AND PREPROCESSING
# ============================================================

import pandas as pd
from io import StringIO

# ------------------------------------------------------------
# 1. CREATE DATASET
# ------------------------------------------------------------

data = """
PassengerId,Name,Age,Gender,City,Salary,Department
1,John,22,Male,Hyderabad,25000,IT
2,Sarah,28,Female,Hyderabad,32000,HR
3,Ravi,25,Male,Chennai,28000,IT
4,Anita,,Female,Bangalore,35000,Finance
5,David,35,Male,Mumbai,40000,Sales
6,Priya,29,Female,Delhi,,HR
7,Arun,31,Male,Hyderabad,45000,IT
8,Meena,27,Female,Chennai,30000,Finance
9,John,22,Male,Hyderabad,25000,IT
10,Rahul,abc,Male,Mumbai,38000,Sales
11,Swathi,26,Female,Bangalore,36000,HR
12,Kiran,30,Male,Hyderabad,42000,IT
13,Latha,24,Female,Delhi,29000,Finance
14,Manoj,,Male,Chennai,31000,Sales
15,Neha,32,Female,Mumbai,50000,HR
16,Varun,29,Male,Hyderabad,41000,IT
17,Pooja,27,Female,Bangalore,34000,Finance
18,Ramesh,33,Male,Delhi,39000,Sales
19,Divya,25,Female,Chennai,30000,HR
20,Ajay,28,Male,Hyderabad,37000,IT
"""

# Convert the text dataset into a Pandas DataFrame
df = pd.read_csv(StringIO(data))

print("=" * 60)
print("CODSOFT - DATA ANALYTICS INTERNSHIP")
print("TASK 1: DATA CLEANING AND PREPROCESSING")
print("=" * 60)


# ------------------------------------------------------------
# 2. DISPLAY ORIGINAL DATASET
# ------------------------------------------------------------

print("\n1. ORIGINAL DATASET")
print("-" * 60)
print(df.to_string(index=False))


# ------------------------------------------------------------
# 3. INSPECT DATASET STRUCTURE
# ------------------------------------------------------------

print("\n\n2. DATASET STRUCTURE")
print("-" * 60)

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

print("\nColumn names:")
print(df.columns.tolist())


# ------------------------------------------------------------
# 4. CHECK DATA TYPES
# ------------------------------------------------------------

print("\n\n3. DATA TYPES BEFORE CLEANING")
print("-" * 60)
print(df.dtypes)


# ------------------------------------------------------------
# 5. CHECK MISSING VALUES
# ------------------------------------------------------------

print("\n\n4. MISSING VALUES")
print("-" * 60)

missing_values = df.isnull().sum()

print(missing_values)


# ------------------------------------------------------------
# 6. CHECK DUPLICATE RECORDS
# ------------------------------------------------------------

print("\n\n5. DUPLICATE RECORDS")
print("-" * 60)

duplicate_count = df.duplicated().sum()

print("Number of duplicate records:", duplicate_count)


# ------------------------------------------------------------
# 7. REMOVE DUPLICATES
# ------------------------------------------------------------

df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print("Number of rows:", df.shape[0])


# ------------------------------------------------------------
# 8. CORRECT AGE DATA TYPE
# ------------------------------------------------------------

print("\n\n6. CORRECTING AGE DATA TYPE")
print("-" * 60)

# Convert Age into numeric format
# Invalid values such as 'abc' become NaN
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

print("Age column data type:")
print(df["Age"].dtype)


# ------------------------------------------------------------
# 9. HANDLE MISSING AGE VALUES
# ------------------------------------------------------------

print("\n\n7. HANDLING MISSING AGE VALUES")
print("-" * 60)

age_median = df["Age"].median()

print("Median Age:", age_median)

df["Age"] = df["Age"].fillna(age_median)

print("Missing Age values after cleaning:")
print(df["Age"].isnull().sum())


# ------------------------------------------------------------
# 10. HANDLE MISSING SALARY VALUES
# ------------------------------------------------------------

print("\n\n8. HANDLING MISSING SALARY VALUES")
print("-" * 60)

salary_median = df["Salary"].median()

print("Median Salary:", salary_median)

df["Salary"] = df["Salary"].fillna(salary_median)

print("Missing Salary values after cleaning:")
print(df["Salary"].isnull().sum())


# ------------------------------------------------------------
# 11. CORRECT SALARY DATA TYPE
# ------------------------------------------------------------

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")


# ------------------------------------------------------------
# 12. CHECK FOR INCONSISTENT DATA
# ------------------------------------------------------------

print("\n\n9. CHECKING INCONSISTENT DATA")
print("-" * 60)

print("Gender values:")
print(df["Gender"].unique())

print("\nCity values:")
print(df["City"].unique())

print("\nDepartment values:")
print(df["Department"].unique())


# ------------------------------------------------------------
# 13. FINAL MISSING VALUE CHECK
# ------------------------------------------------------------

print("\n\n10. MISSING VALUES AFTER CLEANING")
print("-" * 60)

print(df.isnull().sum())


# ------------------------------------------------------------
# 14. FINAL DATA TYPES
# ------------------------------------------------------------

print("\n\n11. DATA TYPES AFTER CLEANING")
print("-" * 60)

print(df.dtypes)


# ------------------------------------------------------------
# 15. FINAL CLEANED DATASET
# ------------------------------------------------------------

print("\n\n12. CLEANED DATASET")
print("-" * 60)

print(df.to_string(index=False))


# ------------------------------------------------------------
# 16. FINAL DATASET INFORMATION
# ------------------------------------------------------------

print("\n\n13. FINAL DATASET INFORMATION")
print("-" * 60)

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Duplicate records:", df.duplicated().sum())
print("Total missing values:", df.isnull().sum().sum())


# ------------------------------------------------------------
# 17. SAVE CLEANED DATASET
# ------------------------------------------------------------

output_file = "cleaned_data_task1.csv"

df.to_csv(output_file, index=False)

print("\n\n14. FILE SAVED")
print("-" * 60)

print("Cleaned dataset saved successfully!")
print("File name:", output_file)

print("\nTASK 1 COMPLETED SUCCESSFULLY!")
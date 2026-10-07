# codsoft-task1
# CodSoft Data Analytics Internship – Task 1

## Data Cleaning and Preprocessing

This project is completed as part of my **Data Analytics Virtual Internship at CodSoft**.

### Internship Details

- **Organization:** CodSoft
- **Domain:** Data Analytics
- **Task:** Task 1 – Data Cleaning and Preprocessing
- **Internship Duration:** 1 Month
- **Mode:** Virtual Internship
- **Batch:** October 2026

---

## Objective

The objective of this task is to perform basic data cleaning and preprocessing operations on a dataset.

The following activities were performed:

1. Import and inspect the dataset
2. Identify missing values
3. Identify duplicate records
4. Remove duplicate records
5. Handle missing values
6. Correct data types
7. Check inconsistent data
8. Prepare the cleaned dataset
9. Save the cleaned dataset as a CSV file

---

## Dataset

A sample dataset was created for this task containing information about individuals such as:

- Passenger ID
- Name
- Age
- Gender
- City
- Salary
- Department

The dataset contains **20 rows and 7 columns**.

---

## Technologies Used

- Python
- Pandas
- Pydroid 3

---

## Data Cleaning Process

### 1. Dataset Inspection

The original dataset was inspected to understand its structure, number of rows, columns, and data types.

### 2. Missing Values

Missing values were identified using:

```python
df.isnull().sum()

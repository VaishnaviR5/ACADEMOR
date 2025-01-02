# ACADEMOR_Data Science Internship

During my data science internship with ACADEMOR (Feb-March 2024), I successfully completed one minor project and one major project. Below are the details of the tasks and methodologies involved:

## Minor Project: Python Game Development

Objective: Develop a game in Python.
This project involved creating an interactive and engaging Python-based game which was a simple "Word Guessing Game". It served as an excellent introduction to applying programming logic, designing user interfaces, and enhancing user experience in Python.

## Major Project: Loan Approval Prediction

Objective: Build a machine learning model to predict loan approval status based on provided applicant information and created a dashboard in Tableau.

Overview
This project involves predicting loan approval status (Loan_Status) based on various customer details such as income, education, credit history, etc. It uses machine learning techniques, including data preprocessing, exploratory data analysis, feature engineering, and model training.

Dataset
The dataset used for this project contains 614 entries with 13 attributes:

Attributes:
Loan_ID, Gender, Married, Dependents, Education, Self_Employed
ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term
Credit_History, Property_Area, Loan_Status
Target Variable: Loan_Status (Approval Status - Yes/No)

Project Steps
1. Import Libraries
Libraries used: pandas, numpy, seaborn, matplotlib, scikit-learn
2. Load and Explore Dataset
Imported dataset using Pandas
Checked for missing values and performed basic statistical analysis:
Missing values were handled using mode, mean, and median imputation.
3. Exploratory Data Analysis (EDA)
Visualized categorical and numerical attributes using seaborn:
Distribution of Loan_Status, Gender, Married, Self_Employed, etc.
Derived new insights:
Total_Income as a combination of ApplicantIncome and CoapplicantIncome.
4. Feature Engineering
Applied transformations:
Log transformation on skewed features (LoanAmount, ApplicantIncome).
Categorical data encoded using LabelEncoder.
5. Model Training and Evaluation
Split data into training and test sets.
Trained a RandomForestClassifier.
Evaluated the model using:
Accuracy: accuracy_score
Confusion Matrix

Key Findings
Credit History is a significant predictor of loan approval.
Income and property area also impact loan approval status.

Visualizations
Distribution of Loan_Status and categorical variables.
Trends in loan amounts, income, and derived features.


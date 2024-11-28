"""from google.colab import files

# Upload the file
uploaded = files.upload()
import pandas as pd

# Replace 'heart (1).csv' with your uploaded file name
data = pd.read_csv('heart (1).csv')

import os
os.listdir()
"""
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('heart (1).csv')

# Heatmap to visualize correlations
plt.figure(figsize=(12, 10))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Feature Correlation Matrix")
plt.show()

# Distribution of cholesterol levels
plt.figure(figsize=(8, 6))
sns.histplot(data['chol'], kde=True, bins=30, color='blue')
plt.title("Cholesterol Distribution")
plt.xlabel("Cholesterol")
plt.ylabel("Frequency")
plt.show()

# Gender distribution and target comparison
plt.figure(figsize=(8, 6))
sns.countplot(x='sex', hue='target', data=data, palette='pastel')
plt.title("Gender vs Heart Disease")
plt.xlabel("Gender (0 = Female, 1 = Male)")
plt.ylabel("Count")
plt.legend(["No Disease", "Disease"])
plt.show()

# Age vs Max Heart Rate
plt.figure(figsize=(8, 6))
sns.scatterplot(x='age', y='thalach', hue='target', palette='viridis', data=data)
plt.title("Age vs Max Heart Rate by Heart Disease")
plt.xlabel("Age")
plt.ylabel("Max Heart Rate")
plt.legend(["No Disease", "Disease"])
plt.show()

# Chest Pain Type vs Target
plt.figure(figsize=(8, 6))
sns.countplot(x='cp', hue='target', data=data, palette='Set2')
plt.title("Chest Pain Type vs Heart Disease")
plt.xlabel("Chest Pain Type")
plt.ylabel("Count")
plt.legend(["No Disease", "Disease"])
plt.show()

# Pie chart of gender ratio
gender = ['Male', 'Female']
ratio = [data['sex'].value_counts()[1], data['sex'].value_counts()[0]]
plt.figure(figsize=(6, 6))
plt.pie(ratio, labels=gender, colors=['skyblue', 'lightgreen'], autopct='%1.1f%%', startangle=90)
plt.title("Gender Distribution")
plt.show()

"""
This code performs Exploratory Data Analysis (EDA) on a heart disease dataset using visualizations.
The selected columns for the analysis were chosen based on their significance and potential 
impact on predicting heart disease. Here's an explanation for each graph and the rationale 
behind the chosen columns:

1. **Correlation Heatmap**:
   - Purpose: To understand relationships between numerical features.
   - Columns: All numerical columns are included (`age`, `chol`, `thalach`, `trestbps`, etc.).
   - Why: A correlation heatmap highlights how strongly features are related to each other 
     and the target variable (`target`). Features with high correlation to the target can 
     be strong predictors.

2. **Cholesterol Distribution**:
   - Purpose: To analyze the distribution of cholesterol levels in the dataset.
   - Column: `chol` (serum cholesterol in mg/dl).
   - Why: High cholesterol levels are a known risk factor for heart disease. Understanding 
     its distribution helps identify common ranges and outliers.

3. **Gender vs Heart Disease**:
   - Purpose: To compare the prevalence of heart disease across genders.
   - Columns: `sex` (0 = Female, 1 = Male), `target` (0 = No Disease, 1 = Disease).
   - Why: Gender is a critical factor in cardiovascular research. This graph helps 
     visualize disparities between male and female patients in heart disease occurrence.

4. **Age vs Max Heart Rate (thalach)**:
   - Purpose: To explore the relationship between age and maximum heart rate achieved, 
     segmented by heart disease status.
   - Columns: `age`, `thalach`, `target`.
   - Why: Age and maximum heart rate are physiological metrics often linked to cardiac 
     health. This scatterplot shows if heart disease is more prevalent in certain age 
     groups or at specific heart rate levels.

5. **Chest Pain Type vs Heart Disease**:
   - Purpose: To analyze the frequency of different chest pain types and their association 
     with heart disease.
   - Columns: `cp` (chest pain type), `target`.
   - Why: Chest pain is a primary symptom of heart disease. The `cp` column categorizes 
     chest pain into types, which may correlate with the likelihood of heart disease.

6. **Gender Ratio Pie Chart**:
   - Purpose: To visualize the gender distribution in the dataset.
   - Column: `sex`.
   - Why: Knowing the dataset's gender composition ensures balanced analysis and fairness 
     in conclusions drawn from the data.

Overall, the chosen columns are either directly tied to cardiac health indicators (e.g., 
`chol`, `thalach`, `cp`) or demographic factors (e.g., `sex`, `age`) known to influence 
the likelihood of heart disease. These visualizations provide insights into patterns and 
trends in the data, supporting feature selection and model building for heart disease 
prediction.
"""


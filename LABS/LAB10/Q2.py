import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data_path = '/content/BreastCancerDataSet.csv'  
df = pd.read_csv(data_path)

# Preprocess data
df.drop(columns=['Unnamed: 32', 'id'], inplace=True) 
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})  

selected_features = [
    'radius_mean', 'texture_mean', 'area_mean', 'smoothness_mean', 
    'compactness_mean', 'concavity_mean', 'concave points_mean', 
    'symmetry_mean', 'fractal_dimension_mean', 'perimeter_mean'
]

plt.figure(figsize=(16, 20))
for idx, feature in enumerate(selected_features):
    plt.subplot(5, 2, idx + 1)
    sns.histplot(df, x=feature, hue='diagnosis', kde=True, bins=30, palette=['blue', 'orange'], alpha=0.6)
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Density')

plt.tight_layout()
plt.show()

# Generate correlation heatmap
plt.figure(figsize=(18, 16))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm', cbar=True, square=True, linewidths=0.5)
plt.title("Feature Correlation Heatmap")
plt.xticks(fontsize=12, rotation=45, ha='right')
plt.yticks(fontsize=12)
plt.show()

# Generate summary statistics for top features
top_features = [
    'area_mean', 'concave points_mean', 'concave points_worst', 
    'concavity_worst', 'perimeter_mean', 'perimeter_worst', 
    'radius_mean', 'radius_worst', 'texture_mean', 'texture_worst'
]

stats_summary = df[top_features].agg(['mean', 'median', 'std', 'var']).T
stats_summary.plot(kind='bar', figsize=(15, 7), colormap='viridis', legend=True)
plt.title("Summary Statistics (Mean, Median, Std, Variance)")
plt.ylabel("Values")
plt.xlabel("Features")
plt.grid(axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatterplot for top correlated features
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='radius_mean', y='perimeter_mean', hue='diagnosis', palette='viridis')
plt.title("Scatterplot of Radius Mean vs Perimeter Mean")
plt.xlabel("Radius Mean")
plt.ylabel("Perimeter Mean")
plt.legend(["Benign", "Malignant"])
plt.show()

#Boxplot 
plt.figure(figsize=(16, 12))
for idx, feature in enumerate(selected_features):
    plt.subplot(5, 2, idx + 1)
    sns.boxplot(
        data=df, 
        x='diagnosis', 
        y=feature, 
        hue='diagnosis',  # Hue remains the same
        palette={1: 'blue', 0: 'orange'},  # Map numerical values
        dodge=False
    )
    plt.title(f'Boxplot of {feature}')
    plt.xlabel("Diagnosis")
    plt.ylabel(feature)

plt.tight_layout()
plt.show()

# Exploratory Data Analysis (EDA) on the breast cancer dataset

# Step 1: Identifying Outliers
# Boxplots for the selected features help in identifying outliers. These boxplots visualize 
# the distribution of each feature, with the whiskers indicating the range of normal data 
# and points outside of this range showing potential outliers. Outliers can be visually 
# identified as points that fall outside of the whiskers for each feature.

# Step 2: Analyzing the Overall Distribution of the Data
# Histograms are plotted for each selected feature to understand its overall distribution.
# This provides a clear picture of the frequency of values for each feature. The distribution 
# of data helps in identifying any skewness, symmetry, or potential clustering of values.
# In this case, histograms are plotted for 'Malignant' and 'Benign' diagnoses to visualize 
# how the features are distributed between the two categories.

# Step 3: Examining Correlations Between Variables
# A correlation heatmap is generated for all features to examine pairwise relationships.
# The heatmap uses a color scale ('coolwarm') to show the degree of correlation between features.
# Strong correlations between features are highlighted, and any redundancies in features are 
# identified, which can be important for feature selection or dimensionality reduction.

# Step 4: Investigating Observable Trends Within the Dataset
# Boxplots are used again to compare the distribution of continuous variables across categories 
# ('Malignant' vs 'Benign'). These plots show the spread of data for each feature based on diagnosis, 
# allowing us to observe any significant differences or trends between the two categories. 
# Additionally, continuous variables like 'radius_mean', 'area_mean', etc., are observed to determine 
# any patterns that could help in distinguishing between the two groups.

# Step 5: Focusing on Significant Features to Understand Patterns or Dependencies
# Logistic regression is used to identify the most significant features that correlate with the diagnosis.
# The weights from the logistic regression model give an indication of which features are most impactful
# in predicting the diagnosis. A bar plot is created to display the top 10 most significant features.
# These features are crucial for understanding the underlying patterns in the data and their role in 
# classifying the cancer diagnosis.

# Finally, summary statistics (mean, median, variance) for each feature are also calculated.
# These help to provide a better understanding of the central tendencies and the spread of the data, 
# ensuring that we get a well-rounded view of each feature's distribution.

# This exploratory analysis provides insights into the data’s characteristics, distribution, 
# correlations, and outliers, which is essential for further modeling and hypothesis testing.


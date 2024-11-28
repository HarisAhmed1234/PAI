import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Load the dataset
data = pd.read_csv("heart (1).csv")

# Impute missing values 
imputer = SimpleImputer(strategy="most_frequent")
for col in ["ca", "thal"]:  
    data[col] = imputer.fit_transform(data[[col]])


x = data.drop(columns=["target"])  
y = data["target"]

categorical_columns = ["cp", "thal"] 
numerical_columns = [
    "age", "sex", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca"
]  

preprocessor = ColumnTransformer(
    transformers=[
        ("cat_encode", OneHotEncoder(), categorical_columns),
        ("num_scale", StandardScaler(), numerical_columns)
    ],
    remainder="passthrough"
)

x_transformed = preprocessor.fit_transform(x)

le = LabelEncoder()
y_transformed = le.fit_transform(y)

accuracies = []
seeds = range(1, 11)  
neighbors = range(1, len(x_transformed) // 2 + 1) 

for seed in seeds:
    x_train, x_test, y_train, y_test = train_test_split(
        x_transformed, y_transformed, test_size=0.2, random_state=seed
    )
    for k in neighbors:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(x_train, y_train)

        y_pred = knn.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)

        accuracies.append((seed, k, accuracy))

max_accuracy = max(accuracies, key=lambda x: x[2])
min_accuracy = min(accuracies, key=lambda x: x[2])

print("\nAll Accuracies:")
for seed, k, accuracy in accuracies:
    print(f"Seed: {seed}, k: {k}, Accuracy: {accuracy:.4f}")

print(f"\nHighest Accuracy: Seed: {max_accuracy[0]}, k: {max_accuracy[1]}, Accuracy: {max_accuracy[2]:.4f}")
print(f"Lowest Accuracy: Seed: {min_accuracy[0]}, k: {min_accuracy[1]}, Accuracy: {min_accuracy[2]:.4f}")

best_seed = [seed for seed, k, accuracy in accuracies if accuracy == max_accuracy[2]]
worst_seed = [seed for seed, k, accuracy in accuracies if accuracy == min_accuracy[2]]

print(f"Highest accuracy is at seed(s): {best_seed}")
print(f"Lowest accuracy is at seed(s): {worst_seed}")

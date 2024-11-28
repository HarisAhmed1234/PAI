# Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("heart (1).csv") 

x = data.drop(columns=["target"])
y = data["target"] 

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_scaled, y, test_size=0.2, random_state=42)

max_neighbors = len(x_train)
accuracies = []
neighbors = range(1, max_neighbors + 1)  

for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

max_accuracy = max(accuracies)
min_accuracy = min(accuracies)
best_k = [neighbors[i] for i, acc in enumerate(accuracies) if acc == max_accuracy]
worst_k = [neighbors[i] for i, acc in enumerate(accuracies) if acc == min_accuracy]

# Results
print(f"Highest accuracy: {max_accuracy:.4f}, achieved at k values: {best_k}")
print(f"Lowest accuracy: {min_accuracy:.4f}, observed at k values: {worst_k}")

#Accuracy vs Number of Neighbors
plt.figure(figsize=(10, 6))
plt.plot(neighbors, accuracies, marker='o', color='blue')
plt.title("K-Nearest Neighbors Accuracy vs Number of Neighbors")
plt.xlabel("Number of Neighbors (k)")
plt.ylabel("Accuracy")
plt.grid()
plt.show()

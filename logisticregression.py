import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample data: hours studied vs. pass (1) or fail (0)
data = np.array([[1.5, 0],
                 [2.0, 0],
                 [2.5, 0],
                 [3.0, 1],
                 [3.5, 0],
                 [4.0, 1],
                 [4.5, 1],
                 [5.0, 1]])

# Separate the features (hours studied) and target (pass or fail)
X = data[:, 0:1]
y = data[:, 1]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Logistic Regression model
model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Generate a classification report
report = classification_report(y_test, y_pred)
print("Classification Report:")
print(report)


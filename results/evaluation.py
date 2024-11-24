# This class creates a confusion matrix, classification report and the predicted probabilities of the model
# using both the test labels and predicted labels 

import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix

def evaluate_model(y_test, y_pred, probabilities, strategy):
    
    classifier = strategy.classifier
    # print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    
    p_result = pd.DataFrame(probabilities, columns=classifier.classes_)
    print("\nPredicted Probabilities:\n", p_result)
    print("\nClassification Report:\n", classification_report(y_test, y_pred))

    return p_result
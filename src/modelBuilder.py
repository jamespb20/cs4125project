# modelBuilder.py

from src.classifierFactory import ClassifierFactory
from data.data_preprocessing import load_and_preprocess_data, transform_text_data, split_data, transform_single_text
from results.evaluation import evaluate_model
import numpy as np

class ModelBuilder:
    def __init__(self):
        self.params = {}

    def set_learning_rate(self, learning_rate):
        self.params["learning_rate"] = learning_rate
        return self

    def set_max_iterations(self, max_iter):
        self.params["max_iter"] = max_iter
        return self

    def build(self, strategy_class):
        # Use the strategy to configure and return the classifier
        if "learning_rate" in self.params and hasattr(strategy_class.classifier, 'learning_rate'):
            strategy_class.classifier.learning_rate = self.params["learning_rate"]
        if "max_iter" in self.params and hasattr(strategy_class.classifier, 'max_iter'):
            strategy_class.classifier.max_iter = self.params["max_iter"]
        return strategy_class

    def get_params(self):
        return self.params

def change_model_params(model_type):
    model = ClassifierFactory.create_classifier(model_type)
    print("Configure model parameters:")

    # Initialize ModelBuilder
    builder = ModelBuilder()

    # Check if the model supports learning_rate
    if hasattr(model.classifier, 'learning_rate'):
        if model_type in ["sgd", "mlp"]:
            learning_rate = input("Enter the learning rate (constant, invscaling, adaptive) (leave blank to skip): ")
            if learning_rate not in ["constant", "invscaling", "adaptive", ""]:
                print("Invalid learning rate for model type", model_type)
                return
        else:
            learning_rate = input("Enter the learning rate (float) (leave blank to skip): ")
            if learning_rate:
                try:
                    learning_rate = float(learning_rate)
                    if learning_rate <= 0:
                        print("Learning rate must be a positive float.")
                        return
                except ValueError:
                    print("Invalid learning rate value.")
                    return
        if learning_rate:
            builder.set_learning_rate(learning_rate)

    # Check if the model supports max_iter
    if hasattr(model.classifier, 'max_iter'):
        max_iter = input("Enter the maximum iterations (integer) (leave blank to skip): ")
        if max_iter:
            try:
                max_iter = int(max_iter)
                if max_iter <= 0:
                    print("Maximum iterations must be a positive integer.")
                    return
            except ValueError:
                print("Invalid maximum iterations value.")
                return
        if max_iter:
            builder.set_max_iterations(max_iter)

    # Build the model with updated parameters
    model = builder.build(model)

    # Print out the new parameters
    updated_params = builder.get_params()
    print("Model parameters updated successfully.")
    print("Updated parameters:", updated_params)

    # Ask the user if they want to train the model
    train_model = input("Would you like to train the model using the new hyperparameters? (yes/no): ").strip().lower()
    if train_model == 'yes':
        print("Training the model...")

        # Load and preprocess data
        file_path = 'data/AppGallery_translatedWithoutSpam.csv'  # Adjust the file path as needed
        df = load_and_preprocess_data(file_path)
        X, y, tfidfconverter = transform_text_data(df)
        X_train, X_test, y_train, y_test = split_data(X, y)

        # Train the model
        y_pred, probabilities = model.classify(X_train, y_train, X_test)
        evaluate_model(y_test, y_pred, probabilities, model)

        # Predict example text
        example_text = input("Enter a text to predict its category: ")
        example_text_vectorized = transform_single_text(example_text, tfidfconverter)
        example_text_vectorized = np.hstack([example_text_vectorized, example_text_vectorized])
        category, category_probabilities = model.predict(example_text_vectorized)
        print(f"Predicted category: {category}")

        print("Training completed.")
    else:
        print("Model training skipped.")

    return model
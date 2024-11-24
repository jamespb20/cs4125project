#Necessary imports

from data.data_translation import createTranslate
from src.classifierFactory import ClassifierFactory
from src.cli import cli
from data.data_preprocessing import load_and_preprocess_data, transform_text_data, split_data, transform_single_text
from src.model_training import train_svm, predict_svm, train_histgb, predict_histgb, train_sgd, predict_sgd, train_adaBoosting, predict_adaBoosting, train_mlp, predict_mlp
from results.evaluation import evaluate_model
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


# The selected model is determined byt he cli() function which requires user input.
selected_model = cli()
file_path = createTranslate()
print(file_path)

# The following 3 lines, loads anad preprocesses the data, transforms text data into a more suitable format,
# and splits the data into two sets, one for training and one for testing.

df = load_and_preprocess_data(file_path)
X, y, tfidfconverter = transform_text_data(df)
X_train, X_test, y_train, y_test = split_data(X, y)

# Creates and trains a classifier based on selected model and then evaluates the model's performance on the test data set.
try:
    strategy = ClassifierFactory.create_classifier(selected_model)
    y_pred, probabilities = strategy.classify(X_train, y_train, X_test)
    evaluate_model(y_test, y_pred, probabilities, strategy)
    print("TF-IDF features after training:", X_train.shape[1])
    example_text = input("Enter a text to predict its category: ")
    example_text_vectorized = transform_single_text(example_text, tfidfconverter)
    if example_text_vectorized.shape[1] != 2418:
        example_text_vectorized = np.hstack([example_text_vectorized, example_text_vectorized])
    print("TF-IDF features during prediction:", example_text_vectorized.shape[1])
    print("Shape before calling predict:", example_text_vectorized.shape)
    print("Shape of example_text_vectorized before prediction:", example_text_vectorized.shape)
    print("Type of example_text_vectorized before prediction:", type(example_text_vectorized))
    category, category_probabilities = strategy.predict(example_text_vectorized)
    print(f"Predicted category: {category}")
    print(f"Category probabilities: {category_probabilities}")
except ValueError as e:
    print(e)
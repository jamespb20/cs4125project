#Necessary imports

from data.data_translation import createTranslate
from src.classifierFactory import ClassifierFactory
from src.cli import cli
from data.data_preprocessing import load_and_preprocess_data, transform_text_data, split_data
from src.model_training import train_svm, predict_svm, train_histgb, predict_histgb, train_sgd, predict_sgd, train_adaBoosting, predict_adaBoosting, train_mlp, predict_mlp
from results.evaluation import evaluate_model
import numpy as np

# The selected model is determined byt he cli() function which requires user input.
selected_model = cli()
file_path = createTranslate()
print(file_path)

# The following 3 lines, loads anad preprocesses the data, transforms text data into a more suitable format,
# and splits the data into two sets, one for training and one for testing.

df = load_and_preprocess_data(file_path)
X, y = transform_text_data(df)
X_train, X_test, y_train, y_test = split_data(X, y)

# Creates and trains a classifier based on selected model and then evaluates the model's performance on the test data set.
try:
    train_model = ClassifierFactory.create_classifier(selected_model)
    if selected_model == "mlp":
        #mlp is different because it needs both classifier and scaler
        classifier, scaler = train_model(X_train, y_train)
        y_pred, probabilities = predict_mlp(classifier, scaler, X_test)
    else:
        classifier = train_model(X_train, y_train)
        predict_model = globals()["predict_" + selected_model]
        y_pred, probabilities = predict_model(classifier, X_test)

    evaluate_model(y_test, y_pred, probabilities, classifier)
except ValueError as e:
    print(e)


evaluate_model(y_test, y_pred, probabilities, classifier)
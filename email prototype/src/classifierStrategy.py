# classification_strategy.py
from abc import ABC, abstractmethod
from sklearn.svm import SVC
from sklearn.ensemble import HistGradientBoostingClassifier, AdaBoostClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np

class classifierStrategy(ABC):
    @abstractmethod
    def classify(self, X_train, y_train, X_test):
        pass

    @abstractmethod
    def predict(self, text):
        pass

class SVMStrategy(classifierStrategy):
    def __init__(self):
        self.classifier = SVC(kernel='linear', probability=True, random_state=0)
        self.scaler = None

    def classify(self, X_train, y_train, X_test):
        self.classifier.fit(X_train, y_train)
        y_pred = self.classifier.predict(X_test)
        probabilities = self.classifier.predict_proba(X_test)
        return y_pred, probabilities

    def predict(self, text):
        return self.classifier.predict(text), self.classifier.predict_proba(text)

class HistGBStrategy(classifierStrategy):
    def __init__(self):
        self.classifier = HistGradientBoostingClassifier(max_iter=100, random_state=0)

    def classify(self, X_train, y_train, X_test):
        self.classifier.fit(X_train, y_train)
        y_pred = self.classifier.predict(X_test)
        probabilities = self.classifier.predict_proba(X_test)
        return y_pred, probabilities

    def predict(self, text):
        print("Input shape before reshaping:", text.shape)

        # Check if it's 3D and flatten it
        if text.ndim > 2:
            print("Input is 3D, flattening to 2D")
            text = text.reshape(text.shape[0], -1)  # Flatten to 2D: (n_samples, num_features)
        
        # If it's 1D (single sample), reshape to 2D
        elif text.ndim == 1:
            text = text.reshape(1, -1)
        return self.classifier.predict(text), self.classifier.predict_proba(text)

class SGDStrategy(classifierStrategy):
    def __init__(self):
        self.classifier = SGDClassifier(loss='log_loss', max_iter=1000, tol=1e-3, random_state=0)

    def classify(self, X_train, y_train, X_test):
        self.classifier.fit(X_train, y_train)
        y_pred = self.classifier.predict(X_test)
        probabilities = self.classifier.predict_proba(X_test)
        return y_pred, probabilities

    def predict(self, text):
        text = text.reshape(1, -1)
        return self.classifier.predict(text), self.classifier.predict_proba(text)

class AdaBoostingStrategy(classifierStrategy):
    def __init__(self):
        self.classifier = AdaBoostClassifier(n_estimators=50, random_state=0)

    def classify(self, X_train, y_train, X_test):
        self.classifier.fit(X_train, y_train)
        y_pred = self.classifier.predict(X_test)
        probabilities = self.classifier.predict_proba(X_test)
        return y_pred, probabilities

    def predict(self, text):
        text = text.reshape(1, -1)
        return self.classifier.predict(text), self.classifier.predict_proba(text)

class MLPStrategy(classifierStrategy):
    def __init__(self):
        self.classifier = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, random_state=0)
        self.scaler = StandardScaler()

    def classify(self, X_train, y_train, X_test):
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        self.classifier.fit(X_train_scaled, y_train)
        y_pred = self.classifier.predict(X_test_scaled)
        probabilities = self.classifier.predict_proba(X_test_scaled)
        return y_pred, probabilities

    def predict(self, text):
        text_scaled = self.scaler.transform(text)
        return self.classifier.predict(text_scaled), self.classifier.predict_proba(text_scaled)
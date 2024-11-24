from sklearn.svm import SVC
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

# Train the SVM model with the training data, returning the classifier and also return the redicated labels and probabilites.

def train_svm(X_train, y_train, kernel='linear', random_state=0):
    classifier = SVC(kernel=kernel, probability=True, random_state=random_state)
    classifier.fit(X_train, y_train)
    return classifier

def predict_svm(classifier, X_test):
    
    y_pred = classifier.predict(X_test)
    
    probabilities = classifier.predict_proba(X_test)
    return y_pred, probabilities


# Train the HistGradientBoosting Model, return the classifier, return predictated labels and probabilities

def train_histgb(X_train, y_train, max_iter=100, random_state=0):
    classifier = HistGradientBoostingClassifier(max_iter=max_iter, random_state=random_state)
    classifier.fit(X_train, y_train)
    return classifier

def predict_histgb(classifier, X_test):
    
    y_pred = classifier.predict(X_test)
    probabilities = classifier.predict_proba(X_test)
    return y_pred, probabilities


# Train the SGD Classifier model, return classifier, return predictated labels and probabilities

def train_sgd(X_train, y_train, max_iter=1000, tol=1e-3, random_state=0):
    classifier = SGDClassifier(loss='log_loss', max_iter=max_iter, tol=tol, random_state=random_state)
    classifier.fit(X_train, y_train)
    return classifier

def predict_sgd(classifier, X_test):
    
    y_pred = classifier.predict(X_test)
    
    probabilities = classifier.predict_proba(X_test)
    return y_pred, probabilities


#Train the AdaBoostClassifier, returnt he classifier, return the predictated labels and probabilities

def train_adaBoosting(X_train, y_train, n_estimators=50, random_state=0):
    classifier = AdaBoostClassifier(n_estimators=n_estimators, random_state=random_state)
    classifier.fit(X_train, y_train)
    return classifier

def predict_adaBoosting(classifier, X_test):
    
    y_pred = classifier.predict(X_test)
    
    probabilities = classifier.predict_proba(X_test)
    return y_pred, probabilities


##


# Train the MLP model and return the trained classifier and fitted scaler
def train_mlp(X_train, y_train, hidden_layer_sizes=(100,), max_iter=300, random_state=0):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    # Train the MLPClassifier
    classifier = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, 
                                max_iter=max_iter, 
                                random_state=random_state)
    classifier.fit(X_train_scaled, y_train)
    
    return classifier, scaler

# Predict using the trained MLP model and the fitted scaler
def predict_mlp(classifier, scaler, X_test):
    # Scale the test data using the same scaler fitted on training data
    X_test_scaled = scaler.transform(X_test)
    
    # Predict labels and probabilities
    y_pred = classifier.predict(X_test_scaled)
    probabilities = classifier.predict_proba(X_test_scaled)
    
    return y_pred, probabilities
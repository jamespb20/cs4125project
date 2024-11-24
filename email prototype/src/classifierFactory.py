#This class creates classifiers depending on the model type selected.

from src.model_training import train_svm, train_histgb, train_sgd, train_adaBoosting, train_mlp

class ClassifierFactory:
    @staticmethod
    def create_classifier(model_type):
        if model_type == "svm":
            return train_svm
        elif model_type == "histgb":
            return train_histgb
        elif model_type == "sgd":
            return train_sgd
        elif model_type == "adaBoosting":
            return train_adaBoosting
        elif model_type == "mlp":
            return train_mlp
        else:
            raise ValueError(f"Unknown model type: {model_type}")

from src.classifierStrategy import SVMStrategy, HistGBStrategy, SGDStrategy, AdaBoostingStrategy, MLPStrategy

class ClassifierFactory:
    @staticmethod
    def create_classifier(model_type):
        if model_type == "svm":
            return SVMStrategy()
        elif model_type == "histgb":
            return HistGBStrategy()
        elif model_type == "sgd":
            return SGDStrategy()
        elif model_type == "adaBoosting":
            return AdaBoostingStrategy()
        elif model_type == "mlp":
            return MLPStrategy()
        else:
            raise ValueError(f"Unknown model type: {model_type}")
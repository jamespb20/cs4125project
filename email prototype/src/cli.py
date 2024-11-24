#Function to determine which model is selcted.

def cli():
    model_choices = ['svm', 'histgb', 'sgd', 'adaBoosting', 'mlp']
    while True:
        print("Select a model to train and evaluate:")
        for i, model in enumerate(model_choices, 1):
            print(f"{i}. {model}")
        try:
            chosen_model = int(input("Enter the number of the model you want to use: ")) - 1 
            if 0 <= chosen_model < len(model_choices):
                return model_choices[chosen_model]
            else:
                print("Invalid choice. Please select a valid model number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
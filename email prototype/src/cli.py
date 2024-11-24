#Function to determine which model is selcted.
from src.Decorator import check_and_save_csv
def cli():
    while True:
        to_do = ["predict email", "remove spam and seperate urgent emails"]
        print("What would you like to do?")
        for i, task in enumerate(to_do, 1):
            print(f"{i}. {task}")
        try:
            choice = int(input("Enter the number of the task you want to perform: ")) - 1
            if 0 <= choice < len(to_do):
                return to_do[choice]
            else:
                print("Invalid choice. Please select a valid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def model_choose_cli():
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
import csv
import uuid
from datetime import datetime
from src.classifierStrategy import SVMStrategy, HistGBStrategy, SGDStrategy, AdaBoostingStrategy, MLPStrategy

class ClassifierFactory:
    def __init__(self):
        # Registry for reusing classifiers
        self.classifier_registry = {}
        self.categories_file = 'email prototype/data/AppGallery.csv'  # Path to the CSV file

    def register_classifier(self, category_name, classifier_instance):
        """Registers a classifier instance for reuse."""
        self.classifier_registry[category_name] = classifier_instance

    @staticmethod
    def create_classifier(model_type):
        """Creates and returns a classifier strategy based on model type."""
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

    def add_category(self, category_name, ):
       
        
        # Collect the information for the new category
        ticket_summary = input("Enter the Ticket Summary: ")
        interaction_content = input("Enter the Interaction Content: ")
        type_1 = input("Enter Type 1: ")
        type_2 = input("Enter Type 2: ")
        type_3 = input("Enter Type 3: ")
        type_4 = input("Enter Type 4: ")

        # Auto-generate Ticket id and Interaction id
        ticket_id = "NULL"  # Replace auto-generated UUID with "NULL"
        interaction_id = "NULL"  # Replace auto-generated UUID with "NULL"
        interaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Keep current timestamp for Interaction Date


        # Add the new data to the CSV file
        self.save_to_csv(ticket_id, interaction_id, interaction_date, ticket_summary, interaction_content, type_1, type_2, type_3, type_4)

        

    def save_to_csv(self, ticket_id, interaction_id, interaction_date, ticket_summary, interaction_content, type_1, type_2, type_3, type_4):
        """Save the new category data to the CSV file."""
        # Check if the file exists and write the header only if it's a new file
        try:
            with open(self.categories_file, 'r', newline='', encoding='utf-8') as f:  # Force UTF-8 encoding
                reader = csv.reader(f)
                # Check if header exists
                header = next(reader)
        except FileNotFoundError:
            # File doesn't exist, create it and add the header
            with open(self.categories_file, 'w', newline='', encoding='utf-8') as f:  # Force UTF-8 encoding
                writer = csv.writer(f)
                writer.writerow(['Ticket id', 'Interaction id', 'Interaction date', 'Mailbox', 'Ticket Summary', 'Interaction content', 'Innso TYPOLOGY_TICKET', 'Type 1', 'Type 2', 'Type 3', 'Type 4'])  # Write header
                print(f"Created new file and added header to {self.categories_file}.")

        # Append new categories to the CSV file
        with open(self.categories_file, 'a', newline='', encoding='utf-8') as f:  # Force UTF-8 encoding
            writer = csv.writer(f)
            # You can add other default values for columns such as "Mailbox" and "Innso TYPOLOGY_TICKET"
            mailbox = ""  # Empty value for mailbox
            innso_typology_ticket = ""  # Empty value for "Innso TYPOLOGY_TICKET"
            writer.writerow([ticket_id, interaction_id, interaction_date, mailbox, ticket_summary, interaction_content, innso_typology_ticket, type_1, type_2, type_3, type_4])

        print(f"New category data saved to {self.categories_file}.")
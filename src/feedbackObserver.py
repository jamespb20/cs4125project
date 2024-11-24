import csv

class FeedbackManager:
    def __init__(self, translated_file_path, reported_file_path):
        self.translated_file_path = translated_file_path
        self.reported_file_path = reported_file_path

    def search_ticket_by_id(self, ticket_id):
        """
        Searches for a ticket ID in the AppGallery_translated file and returns the email content if found.
        """
        try:
            with open(self.translated_file_path, mode='r', newline='', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                for row in csv_reader:
                    if row[0] == ticket_id:  # Assuming Ticket ID is the first column
                        return row  # Return the full row (Ticket ID, Email Content, etc.)
                print("Ticket ID not found in translated data.")
                return None
        except Exception as e:
            print(f"Error reading AppGallery_translated file: {e}")
            return None

    def submit_feedback(self, ticket_id, email_content, feedback):
        """
        Writes the ticket ID, email content, and user feedback (spam/not spam) to the AppGalleryReported file.
        """
        try:
            with open(self.reported_file_path, mode='a', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([ticket_id, email_content, feedback])  # Append to the reported file
                print(f"Feedback submitted for Ticket ID {ticket_id}: {feedback}")
        except Exception as e:
            print(f"Error writing to AppGalleryReported file: {e}")

def interactive_feedback_workflow(feedback_manager):
    """
    Allows the user to search by Ticket ID in the AppGallery_translated file and submit feedback to the AppGalleryReported file.
    """
    ticket_id = input("Enter the Ticket ID to search: ")
    result = feedback_manager.search_ticket_by_id(ticket_id)

    if result:
        # Assuming row contains [Ticket ID, Email Content, ...]
        email_content = result[5]  # Adjust column index if needed
        print(f"Email Content: {email_content}")
        feedback = input("Enter your feedback (e.g., 'spam', 'not spam'): ").strip().lower()
        feedback_manager.submit_feedback(ticket_id, email_content, feedback)
    else:
        print("No email found for the provided Ticket ID.")

# Example usage
translated_file = "AppGallery_translated.csv"  # Replace with the actual file path
reported_file = "AppGalleryReported.csv"       # Replace with the actual file path

feedback_manager = FeedbackManager(translated_file, reported_file)

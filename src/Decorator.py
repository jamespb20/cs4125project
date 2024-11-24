# Decorator.py

import csv

def check_and_save_csv(input_file_path, output_file_path, output_urgent, output_reported):
    try:
        # Ask the user for the character cutoff for spam detection
        spam_cutoff = int(input("Enter the character cutoff for spam detection: "))

        with open(input_file_path, mode='r', encoding='utf-8') as input_file, \
             open(output_file_path, mode='w', newline='', encoding='utf-8') as output_file, \
             open(output_urgent, mode='w', newline='', encoding='utf-8') as urgent_file, \
             open(output_reported, mode='w', newline='', encoding='utf-8') as reported_file:

            csv_reader = csv.reader(input_file)
            csv_writer = csv.writer(output_file)
            csv_writer_urgent = csv.writer(urgent_file)
            csv_writer_reported = csv.writer(reported_file)

            # Loop through each row in the input CSV
            for row in csv_reader:
                # Check if the email content length exceeds the spam cutoff
                if len(row[5]) > spam_cutoff:
                    # Write the reported email to the 'AppGallery_Reported.csv' file
                    csv_writer_reported.writerow(row)
                    print(f"Email reported as spam: {row[:5]}...")  # Log first 5 columns for reference

                # If the email is urgent, write to the urgent file
                elif any('urgent' in entry.lower() for entry in row):
                    csv_writer_urgent.writerow(row)
                
                # Otherwise, write to the regular file if it meets other criteria
                elif all(len(entry) <= spam_cutoff for entry in row):
                    csv_writer.writerow(row)
                else:
                    print(f"Skipped row: {row[:5]}...")  # Log skipped rows for reference

        print("Urgent emails saved to", output_urgent)
        print("Reported emails saved to", output_reported)
    except Exception as e:
        print(f"Error processing CSV files: {e}")
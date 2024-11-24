import csv

#Reads in csv files and has the output files paths
def check_and_save_csv(input_file_path, output_file_path, output_urgent):
    #Open the orginial translated csv(makes more sense so the word urgent can be checked easier)
    with open(input_file_path, mode='r', newline='', encoding='utf-8') as input_file:
        csv_reader = csv.reader(input_file)
        
        #Open both new csv files 
        with open(output_file_path, mode='w', newline='', encoding='utf-8') as output_file, \
             open(output_urgent, mode='w', newline='', encoding='utf-8') as output_urgent:
            #Writes to normal output file(without spam)
            csv_writer = csv.writer(output_file)
            #Writes to file containing urgent messages
            csv_writer_urgent = csv.writer(output_urgent)

            #Go row by row
            for row_number, row in enumerate(csv_reader, start=1):
                #Go through each column of the selected row
                for col_number, entry in enumerate(row, start=1):
                    entry_length = len(entry)

                    #Creating a csv file with any emails containing urgent so they can be priority
                    if 'urgent' in entry.lower():
                        print("Entry contains the word urgent, added to urgent email listing")
                        csv_writer_urgent.writerow(row)
        
                    #Using 7000 characters in entry as the spam point, greater than 7000 makred as spam otherwise carry on executing 
                    if entry_length > 7000:
                        print(f"Row {row_number}, Column {col_number}: This entry is marked as SPAM (length {entry_length} characters).")
                        break  
                else:
                    #Write result
                    csv_writer.writerow(row)
    print("CSV files saved successfully.")
    print("Urgent emails can be found in the file: ", output_file_urgent)
    print("Emails without spam can be found in the file: ", output_file_path)


#All the different file paths.
input_file_path = "email prototype/data/AppGallery_translated.csv"  
output_file_path = "email prototype/data/AppGallery_translatedWithoutSpam.csv"  
output_file_urgent = "email prototype/data/AppGallery_UrgentList.csv"

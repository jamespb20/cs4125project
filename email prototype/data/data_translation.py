from deep_translator import GoogleTranslator
import pandas as pd
import os

# Load the data from the CSV file
df = pd.read_csv("email prototype\data\AppGallery.csv")
# Initialize the translator
translator = GoogleTranslator(source='auto', target='en')

def translate(text):
    max_chunk_size = 4000  # Max characters allowed for translation API
    
    if pd.isna(text):
        return text

    # If text length exceeds the limit, we split it into chunks
    if len(text) > max_chunk_size:
        # Split text into chunks of the max allowed size
        chunks = [text[i:i + max_chunk_size] for i in range(0, len(text), max_chunk_size)]
        
        translated_chunks = []
        for i, chunk in enumerate(chunks):
            try:
                print(f"Translating chunk {i+1}/{len(chunks)}...")  # Debugging print
                translated = translator.translate(chunk)
                translated_chunks.append(translated)
            except Exception as e:
                print(f"Error translating chunk {i+1}: {e}")
                translated_chunks.append(chunk)  # If translation fails, add the original chunk
        
        # Combine the translated chunks back into a single string
        translated_text = ''.join(translated_chunks)
        return translated_text
    else:
        # If text is within the limit, translate it directly
        try:
            translated = translator.translate(text)
            return translated
        except Exception as e:
            print(f"Error translating text: {e}")
            return text  # Return original text in case of an error

def createTranslate():
    translated_file_path = 'email prototype/data/AppGallery_translated.csv'
    
    if os.path.isfile(translated_file_path):
        # Check the number of rows in both files
        num_rows = len(df)
        num_rows_translate = len(pd.read_csv(translated_file_path))
        
        # If the translated file has the same number or more rows, return the existing file path
        if num_rows_translate >= num_rows:
            print(f"Translation already done. Returning existing file: {translated_file_path}")
            return translated_file_path
        else:
            print("Translated file is outdated, reprocessing...")
            os.remove(translated_file_path)  # Remove outdated file
            return createFile()  # Create new translation
        
    else:
        # If the translated file doesn't exist, create it
        return createFile()

def createFile():
    # Apply translation to the 'Interaction content' column
    print("Translating the content...")
    df['Interaction content'] = df['Interaction content'].apply(translate)

    # Apply translation to the 'Ticket Summary' column
    df['Ticket Summary'] = df['Ticket Summary'].apply(translate)

    # Save the translated data to a new CSV file
    translated_file_path = 'email prototype/data/AppGallery_translated.csv'
    df.to_csv(translated_file_path, index=False)
    
    print(f"Translation completed and saved to: {translated_file_path}")
    return translated_file_path
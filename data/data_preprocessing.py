

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

df = pd.read_csv("data\AppGallery.csv")



#load and preprocess the data from csv file

def load_and_preprocess_data(file_path):
    
    df = pd.read_csv(file_path)

    

    # convert to string format
    df['Interaction content'] = df['Interaction content'].astype('U')
    df['Ticket Summary'] = df['Ticket Summary'].astype('U')

    # two new columns, to represent type 2 and interaction content respectively.
    df["y"] = df["Type 2"]
    df["x"] = df['Interaction content']

    # filters dataframe, removes rows where y is empty or doesnt contain a number
    df = df.loc[(df["y"] != '') & (~df["y"].isna()), ]

    return df


#transform the text data into numerical

def transform_text_data(df):
    # Initialize vectorizer to convert text data into numerical
    tfidfconverter = TfidfVectorizer(max_features=2000, min_df=4, max_df=0.90)

    # Fit the vectorizer on the combined text data
    combined_text = df["Interaction content"].tolist() + df["Ticket Summary"].tolist()
    tfidfconverter.fit(combined_text)

    # Convert the two columns into numerical
    x1 = tfidfconverter.transform(df["Interaction content"]).toarray()
    x2 = tfidfconverter.transform(df["Ticket Summary"]).toarray()

    # Concatenate the two results
    X = np.concatenate((x1, x2), axis=1)

    # Extract y
    y = df["y"].to_numpy()

    # Return matrix X, target variable y, and the vectorizer
    return X, y, tfidfconverter

def transform_single_text(text, tfidfconverter):
    # Transform a single text entry using the provided tfidfconverter
    return tfidfconverter.transform([text]).toarray()


#split the data into training and test sets, 80% and 20% respectively.
def split_data(X, y, test_size=0.2, random_state=0):
    
    return train_test_split(X, y, test_size=test_size, random_state=random_state)
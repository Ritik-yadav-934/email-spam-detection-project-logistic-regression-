import pandas as pd
from preprocess import clean_text

# Load the data
df = pd.read_csv("data/raw/emails.csv")

# Apply text cleaning
df["clean_text"] = df["text"].apply(clean_text)
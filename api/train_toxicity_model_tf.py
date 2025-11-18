import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import TextVectorization, Embedding, Dense, GlobalAveragePooling1D
import os

print("---AI Tools Imported Successfully---")
print(f"Tensorflow Version: {tf.__version__}")

print("Loading Data Set...")
try:
    data_path = 'toxic_data.csv'

    df = pd.read_csv(data_path)

    print("Data Set Loaded Successfully. Here are the  first 5 rows:")
    print(df.head())

except FileNotFoundError:
    print(f"Error: Data Set not found at {data_path}")
    exit()

except Exception as e:
    print(f"Error loading Data Set: {e}")
    exit()

print("\n---Cleaning Data---")

try:
    df = df[['tweet', 'class']]
    print("Kept only 'tweet' and 'class' columns..")
except KeyError:
    print("Error: Could not find 'tweet' or 'class' columns in the CSV.")
    exit()

df['label'] = df['class'].apply(lambda x: 0 if x == 2 else 1)
df = df.drop(columns=['class'])

print("Cleaned data. Here are the first 5 rows with new labels:")
print(df.head())

x = df['tweet']
y = df['label']

print("\nData separated into X (tweets) and Y (labels).")
print(f"Total tweets: {len(x)}, Total labels: {len(y)}")

print("\n---Building Model---")

MAX_FEATURES = 10000

SEQUENCE_LENGTH = 250

vectorize_layer = TextVectorization(
    max_tokens = MAX_FEATURES,
    output_mode  = 'int',
    output_sequence_length = SEQUENCE_LENGTH
)

print("TextVectorization layer created.")

print("Adapting the vectorizer (building the dictionary)...")
vectorize_layer.adapt(x)
print("Vectorizer adapted. Dictionary is built.")
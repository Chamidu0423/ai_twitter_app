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

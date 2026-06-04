import pandas as pd

def load_data():
    return pd.read_csv(
        "data/Teen_Mental_Health_Dataset.csv"
    )

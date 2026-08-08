import pandas as pd

def load_data(filepath):
    """Load the Ames Housing dataset from CSV file."""
    return pd.read_csv(filepath)

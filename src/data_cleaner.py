import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

def clean_data(df):
    """Clean the Ames Housing dataset."""
    
    # Drop unnecessary columns
    df = df.drop(['Order', 'PID', 'Alley', 'Pool QC', 'Fence', 'Misc Feature', 'Garage Cond'], axis=1, errors='ignore')
    
    # Handle basement missing values
    df['Has_Bsmt'] = df['Bsmt Qual'].notna().astype(int)
    
    # Fill numerical missing values with 0
    numeric_cols = ['BsmtFin SF 1', 'BsmtFin SF 2', 'Bsmt Unf SF', 'Total Bsmt SF', 
                    'Garage Cars', 'Garage Area', 'Garage Yr Blt', 
                    'Bsmt Full Bath', 'Bsmt Half Bath']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].fillna(0)
    
    # Fill categorical missing values with 'None'
    categorical_cols = ['Bsmt Qual', 'Bsmt Cond', 'Bsmt Exposure', 'BsmtFin Type 1', 
                        'BsmtFin Type 2', 'Garage Type', 'Garage Finish', 
                        'Garage Qual', 'Fireplace Qu']
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].fillna('None')
    
    # Label Encoding for categorical columns
    encode = LabelEncoder()
    for col in categorical_cols:
        if col in df.columns:
            df[f'{col}_Encoded'] = encode.fit_transform(df[col])
            df = df.drop(col, axis=1)
    
    return df
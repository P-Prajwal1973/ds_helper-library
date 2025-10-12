"""
Column type detection for pandas DataFrames.
Automatically identifies numerical, categorical, and text columns.
"""

import pandas as pd
import numpy as np

def detect_column_types(df: pd.DataFrame, categorical_threshold: int = 20) -> dict:
    """
    Detect the types of columns in a pandas DataFrame.
    
    Args:
        df: pandas DataFrame to analyze
        categorical_threshold: maximum number of unique values for a numeric column
                            to be considered categorical (default: 20)
    
    Returns:
        dict: Mapping of column names to their detected types ('numerical', 'categorical', or 'text')
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
        
    column_types = {}
    
    for column in df.columns:
        # Get column data and type
        col_data = df[column]
        dtype = str(col_data.dtype)
        
        # Skip columns that are all null
        if col_data.isna().all():
            column_types[column] = 'unknown'
            continue
            
        # Check if numeric
        if np.issubdtype(col_data.dtype, np.number):
            unique_count = col_data.nunique()
            if unique_count <= categorical_threshold:
                column_types[column] = 'categorical'
            else:
                column_types[column] = 'numerical'
            continue
            
        # Check if datetime
        try:
            pd.to_datetime(col_data)
            column_types[column] = 'datetime'
            continue
        except (TypeError, ValueError):
            pass
            
        # Check if categorical/text based on unique values
        unique_count = col_data.nunique()
        if unique_count <= categorical_threshold:
            column_types[column] = 'categorical'
        else:
            column_types[column] = 'text'
            
    return column_types
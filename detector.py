"""detector.py
Utilities to detect column types in a pandas DataFrame.

Public API:
 - detect_column_types(df, categorical_threshold=20) -> dict

This module is safe to import (no heavy side-effects). Use the CLI to run
on a CSV file: python -m ds_helper_library.detector path/to/file.csv
"""
from typing import Dict
import pandas as pd

__all__ = ["detect_column_types"]


def detect_column_types(df: pd.DataFrame, categorical_threshold: int = 20) -> Dict[str, str]:
    """Detect simple column types for a DataFrame.

    Types: 'numerical', 'categorical', 'text'

    Args:
        df: pandas DataFrame to inspect.
        categorical_threshold: number of unique values below which a numeric column
            is considered categorical.

    Returns:
        dict mapping column name -> detected type.
    """
    column_types = {}
    for col in df.columns:
        num_unique = df[col].nunique(dropna=False)
        dtype = df[col].dtype

        if dtype == "object" or dtype == "string":
            column_types[col] = "text"
        elif pd.api.types.is_numeric_dtype(dtype):
            if num_unique < categorical_threshold:
                column_types[col] = "categorical"
            else:
                column_types[col] = "numerical"
        else:
            column_types[col] = "categorical"
    return column_types


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Detect column types in a CSV file")
    parser.add_argument("csv", nargs="?", default=None, help="Path to CSV file")
    args = parser.parse_args()

    if args.csv is None:
        print("Please provide a CSV file path. Example: python detector.py Titanic.csv")
    else:
        df = pd.read_csv(args.csv)
        print(detect_column_types(df))
import pandas as pd

# Load the Titanic dataset
df = pd.read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\ds_helper library\Titanic-Dataset.csv")

def detect_column_types(df, categorical_threshold=20):
    column_types = {}
    for col in df.columns:
        num_unique = df[col].nunique(dropna=False)
        dtype = df[col].dtype

        if dtype == 'object' or dtype == 'string':
            column_types[col] = 'text'
        elif pd.api.types.is_numeric_dtype(dtype):
            if num_unique < categorical_threshold:
                column_types[col] = 'categorical'
            else:
                column_types[col] = 'numerical'
        else:
            column_types[col] = 'categorical'
    return column_types

# Detect column types in the Titanic dataset
result = detect_column_types(df)
print(result)

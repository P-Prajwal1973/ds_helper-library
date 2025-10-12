"""
Automatic data visualization for pandas DataFrames.
Generates appropriate plots based on column types.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from .column_detector import detect_column_types

def visualize(df: pd.DataFrame, categorical_threshold: int = 20):
    """
    Automatically create visualizations for each column in a DataFrame.
    
    Args:
        df: pandas DataFrame to visualize
        categorical_threshold: threshold for categorical detection (passed to detect_column_types)
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
        
    # Set style
    plt.style.use('seaborn')
    
    # Detect column types
    col_types = detect_column_types(df, categorical_threshold)
    
    # Create visualizations based on column types
    for col, col_type in col_types.items():
        plt.figure(figsize=(10, 6))
        
        if col_type == 'numerical':
            # For numerical columns: histogram and box plot
            plt.subplot(2, 1, 1)
            sns.histplot(data=df, x=col, kde=True)
            plt.title(f'Distribution of {col}')
            
            plt.subplot(2, 1, 2)
            sns.boxplot(data=df, x=col)
            plt.title(f'Box Plot of {col}')
            
        elif col_type == 'categorical':
            # For categorical columns: bar plot
            value_counts = df[col].value_counts()
            sns.barplot(x=value_counts.index, y=value_counts.values)
            plt.title(f'Value Counts for {col}')
            plt.xticks(rotation=45, ha='right')
            
        elif col_type == 'text':
            # For text columns: frequency plot of most common values
            value_counts = df[col].value_counts().head(20)  # Top 20 most common
            sns.barplot(x=value_counts.values, y=value_counts.index)
            plt.title(f'Top 20 Most Common Values in {col}')
            
        plt.tight_layout()
        plt.show()
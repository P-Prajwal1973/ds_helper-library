import re
from typing import List
import pandas as pd

# Only use the given stopwords: 'uh', 'um', 'like'
STOPWORDS = set(['uh', 'um', 'like'])

def clean_text(text: str) -> str:
    """
    Cleans text by removing punctuation and the given stopwords ('uh', 'um', 'like').
    Args:
        text (str): Input text string.
    Returns:
        str: Cleaned text string.
    """
    # Lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize
    words = text.split()
    # Remove given stopwords
    words = [w for w in words if w not in STOPWORDS]
    return ' '.join(words)

def clean_texts(texts: List[str]) -> List[str]:
    """
    Cleans a list of text strings using punctuation and given stopwords removal.
    Args:
        texts (List[str]): List of text strings.
    Returns:
        List[str]: List of cleaned text strings.
    """
    return [clean_text(t) for t in texts]

if __name__ == "__main__":
    # Load Titanic dataset
    df = pd.read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\ds_helper library\Titanic-Dataset.csv")
    # Clean all text columns
    text_columns = df.select_dtypes(include=['object']).columns
    cleaned_df = df.copy()
    for col in text_columns:
        cleaned_df[col] = clean_texts(df[col].astype(str).tolist())
    print(cleaned_df[text_columns].head(10).T)  # Transposed view: columns as rows

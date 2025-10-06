import re
from typing import List

# Only use the given stopwords: 'uh', 'um', 'like'
STOPWORDS = set(["uh", "um", "like"])


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


__all__ = ["clean_text", "clean_texts"]


if __name__ == "__main__":
    import argparse
    import pandas as pd

    parser = argparse.ArgumentParser(description="Clean text columns in a CSV file")
    parser.add_argument("csv", nargs="?", help="Path to CSV file to clean")
    parser.add_argument("--save", action="store_true", help="Save cleaned CSV alongside original")
    args = parser.parse_args()

    if not args.csv:
        print("Provide a CSV file path to clean. Example: python text_cleaner.py Titanic-Dataset.csv")
    else:
        df = pd.read_csv(args.csv)
        # Clean all text columns
        text_columns = df.select_dtypes(include=["object"]).columns
        cleaned_df = df.copy()
        for col in text_columns:
            cleaned_df[col] = clean_texts(df[col].astype(str).tolist())
        print(cleaned_df[text_columns].head(10).T)
        if args.save:
            out_path = args.csv.replace('.csv', '-cleaned.csv')
            cleaned_df.to_csv(out_path, index=False)
            print(f"Saved cleaned CSV to {out_path}")

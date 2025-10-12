"""
Text cleaning utilities for data preprocessing.
Removes punctuation and specified filler words from text.
"""

import string
from typing import List, Union

def clean_text(text: str) -> str:
    """
    Clean a single text string by removing punctuation and specified filler words.
    
    Args:
        text: String to clean
        
    Returns:
        str: Cleaned text
    """
    if not isinstance(text, str):
        return str(text)
        
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))
    
    # Split into words
    words = text.split()
    
    # Remove specific filler words
    filler_words = {'uh', 'um', 'like'}
    words = [word for word in words if word not in filler_words]
    
    # Rejoin words
    return ' '.join(words)

def clean_texts(texts: List[str]) -> List[str]:
    """
    Clean a list of text strings.
    
    Args:
        texts: List of strings to clean
        
    Returns:
        List[str]: List of cleaned texts
    """
    return [clean_text(text) for text in texts]
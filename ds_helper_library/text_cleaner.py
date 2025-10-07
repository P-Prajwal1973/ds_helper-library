import re
from typing import List

# Only use the given stopwords: 'uh', 'um', 'like'
STOPWORDS = set(["uh", "um", "like"])

def clean_text(text: str) -> str:
    """Cleans text by removing punctuation and the given stopwords."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    words = [w for w in words if w not in STOPWORDS]
    return ' '.join(words)

def clean_texts(texts: List[str]) -> List[str]:
    return [clean_text(t) for t in texts]

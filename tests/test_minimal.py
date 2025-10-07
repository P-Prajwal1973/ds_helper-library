import pandas as pd
from detector import detect_column_types
from text_cleaner import clean_texts


def test_pipeline_on_titanic():
    df = pd.read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\ds_helper library\Titanic-Dataset.csv")
    # detect types
    types = detect_column_types(df)
    assert 'Name' in types and types['Name'] in ('text',)
    # clean text columns
    text_cols = df.select_dtypes(include=['object']).columns
    cleaned = {}
    for col in text_cols:
        cleaned[col] = clean_texts(df[col].astype(str).tolist())
    # simple assertions: same number of rows and non-empty entries for Name
    assert len(cleaned['Name']) == len(df)
    assert any(s.strip() for s in cleaned['Name'])

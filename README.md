# DS Helper

A Python package providing utilities for data science tasks, including automatic data visualization, text cleaning, and column type detection.

## Features

- Auto Visualizer: Automatically generate visualizations for numerical, categorical, and text columns in pandas DataFrames
- Column Detector: Smart detection of column types (numerical, categorical, text) based on content
- Text Cleaner: Simple text preprocessing utilities including punctuation removal and filler word filtering

## Installation

```bash
# Clone the repository
git clone https://github.com/P-Prajwal1973/DS_Helper.git
cd DS_Helper

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Install in editable mode
pip install -e .
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/P-Prajwal1973/DS_Helper.git
```

## Usage

```python
import pandas as pd
from DS_Helper import detect_column_types, clean_texts, visualize

# Load your data
df = pd.read_csv('your_data.csv')

# Detect column types
types = detect_column_types(df)
print("Column types:", types)

# Clean text in a column
if 'text_column' in df.columns:
    cleaned_texts = clean_texts(df['text_column'].tolist())
    print("Cleaned texts:", cleaned_texts[:5])

# Generate automatic visualizations
visualize(df)
```

## Example Output

Column types are detected as:
- Numerical: Continuous numeric data (e.g., age, salary)
- Categorical: Limited-value numeric or text data (e.g., gender, department)
- Text: Free-form text content

Visualizations are automatically generated based on column type:
- Numerical: Histogram with KDE and box plot
- Categorical: Bar plot of value counts
- Text: Frequency plot of top 20 most common values

## Requirements

- Python 3.7+
- pandas >= 1.0.0
- numpy >= 1.18.0
- matplotlib >= 3.3.0
- seaborn >= 0.11.0

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
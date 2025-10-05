import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from detector import detect_column_types  # Import from detector.py

def visualize(df):
    column_types = detect_column_types(df)
    for col, col_type in column_types.items():
        plt.figure(figsize=(8,5))
        plt.title(f"{col} ({col_type})")

        if col_type == 'numerical':
            plt.subplot(1,3,1)
            sns.histplot(df[col].dropna(), kde=False)
            plt.title("Histogram")

            plt.subplot(1,3,2)
            plt.scatter(df.index, df[col])
            plt.title("Scatter plot")

            plt.subplot(1,3,3)
            sns.boxplot(x=df[col])
            plt.title("Boxplot")

        elif col_type == 'categorical':
            value_counts = df[col].value_counts()
            plt.subplot(1,2,1)
            value_counts.plot.bar()
            plt.title("Bar chart")

            plt.subplot(1,2,2)
            sns.countplot(x=col, data=df)
            plt.title("Count plot")

        elif col_type == 'text':
              text = ' '.join(df[col].dropna().astype(str))
              # Frequency plot for most common words
              from collections import Counter
              words = text.split()
              word_freq = Counter(words)
              most_common = word_freq.most_common(20)
              words, freqs = zip(*most_common) if most_common else ([],[])
              plt.bar(words, freqs)
              plt.xticks(rotation=45, ha='right')
              plt.title('Top 20 Word Frequency')
              plt.ylabel('Frequency')

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    import pandas as pd
    # Load Titanic dataset from CSV
    df = pd.read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\ds_helper library\Titanic-Dataset.csv")
    visualize(df)

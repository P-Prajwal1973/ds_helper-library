import pandas as pd
from detector import detect_column_types
from text_cleaner import clean_text
from visualizer import visualize


def test_detect_column_types_on_small_df():
    df = pd.DataFrame({
        'num': [1, 2, 3],
        'cat': ['a', 'b', 'a'],
        'txt': ['hello', 'uh like me', 'um ok']
    })
    types = detect_column_types(df, categorical_threshold=3)
    assert types['num'] in ('numerical', 'categorical')
    assert types['cat'] in ('categorical', 'text')
    assert types['txt'] == 'text'


def test_clean_text_removes_stopwords():
    assert clean_text('Hello uh like world!') == 'hello world'


# visualizer is harder to test for plots; here we call it to ensure no exceptions
def test_visualize_runs():
    df = pd.DataFrame({
        'num': [1, 2, 3],
        'cat': ['a', 'b', 'a'],
        'txt': ['hello there', 'foo bar', 'baz qux']
    })
    # call visualize but do not show plots in tests; visualizer uses plt.show() which will block,
    # so we monkeypatch it temporarily
    import matplotlib
    matplotlib.use('Agg')
    visualize(df)

"""
DS_Helper: Python utilities for data science tasks
"""

__version__ = "0.1.0"

from .column_detector import detect_column_types
from .text_cleaner import clean_text, clean_texts
from .auto_visualizer import visualize

__all__ = ['detect_column_types', 'clean_text', 'clean_texts', 'visualize']
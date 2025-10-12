from setuptools import setup, find_packages

setup(
    name="DS_Helper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
        "matplotlib>=3.3.0",
        "seaborn>=0.11.0",
    ],
    author="P-Prajwal1973",
    author_email="your.email@example.com",  # Update with your email
    description="A Python package providing utilities for data science tasks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/P-Prajwal1973/DS_Helper",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
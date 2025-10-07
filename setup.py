from setuptools import setup, find_packages

setup(
    name='ds_helper_library',
    version='0.1.0',
    description='Small helper utilities for data exploration and text cleaning',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn'
    ],
    python_requires='>=3.8',
)

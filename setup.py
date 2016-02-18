from setuptools import setup

setup(
    name='FileGrouper',
    version='1.1',
    py_modules=['filegrouper'],
    install_requires=[
        'Click',
    ],
    entry_points="""
    [console_scripts]
    groupfiles=filegrouper:cli
    """
)

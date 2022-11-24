# Stock Performance

The trading company you are working for, `Godel Trading`, wants to analyze a batch of stocks in order to determine the upcoming year's trading strategy.

You've been tasked with creating a Python script that accomplishes this. This script will request financial data for 2022 from an API, save this data into a csv, and then generate a comprehensive report using this generated csv. 

Specifically, this script will utilize the [Polygon API](https://polygon.io/) in order to request stock data. Next, we will write data into a csv file using the [csv](https://docs.python.org/3/library/csv.html) module. This subsequent csv file will then be used to generate descriptive statistics, similarily recorded in a seperate csv file. 

Since the computing environment at `Godel Trading` does not include 3rd party modules such as `pandas` or `numpy`, we will have to solely rely on the built-in [functions](https://docs.python.org/3/library/functions.html) and [modules](https://docs.python.org/3/py-modindex.html) of Python.

## Data and Output

You will focus on analyzing 5 stock ticker names of your choice in order to demonstrate the functionality of this pipeline. For example, if you'd like to analyze Google, Amazon, Coursera, Netflix, and Facebook, you would utilize the following names within your code: `GOOG`, `AMZN`, `COUR`, `NFLX`, and `META`.

You will use these names to load daily stock data from into a csv from April 1 2021 - April 1 2022 [Polygon](https://polygon.io/). You will then use this subequent csv file to generate a report on each respective stock's standard deviation for both 2021 & 2022.

## Part 1

For the very first part of this project you will work on getting a GitHub repository set up, that will include the following files:

* extract.py
* config.py
* .gitignore
* README.md

These files will include the following:

### extract.py

This Python file will import the key from `config.py` and constact a URL that gets the closing price of one of your stocks for a singular date. For example, `AAPL` stock for `11-08-2022`.

You can import a variable from another Python file using
```python
from config import key
```

### config.py

This file will only contain a variable called `key` that is a string of your API Polygon key. Make sure that this is not pushed to your GitHub repository!

### .gitignore

This will be a .gitignore file that tells `git` to ignore your `config.py` file. Think about which pattern you must include in this file to ensure that all files named `config.py` are ignored. Recall how we placed `states_all.csv` in our .gitignore previously to ignore that data file.

### README.md

For now this file will only include the title of your repo along with a short description of what your code does so far.

Feel free to name this repository any descriptive name that describes the goal of this project!

## FAQ

### Using an API

To complete this project, you will need to sign up for a free API key via [Polygon](https://polygon.io/). 

## Documentation

Ensure that your project is appropriately commented with all necessary comments and docstrings. That is, if you have created a class, this class must also contain a docstring. Singular functions must also contain a docstring if they are not attached to a class.




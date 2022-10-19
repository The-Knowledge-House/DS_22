# Stock Performance

The trading company you are working for, `Godel Trading`, wants to analyze a batch of stocks in order to determine the upcoming quarter's trading strategy.

You've been tasked with creating a Python script that accomplishes this. This script will request financial data for 2022 from an API, save this data into a csv, and then generate a comprehensive report using this generated csv. 

Specifically, this script will utilize the [Polygon API](https://polygon.io/) in order to request stock data. Next, we will write data into a csv file using the [csv](https://docs.python.org/3/library/csv.html) module. This subsequent csv file will then be used to generate descriptive statistics, similarily recorded in a seperate csv file. 

Since the computing environment at `Godel Trading` does not include 3rd party modules such as `pandas` or `numpy`, we will have to solely rely on the built-in [functions](https://docs.python.org/3/library/functions.html) and [modules](https://docs.python.org/3/py-modindex.html) of Python.

## Data and Output

You will focus on analyzing 5 stock ticker names of your choice in order to demonstrate the functionality of this pipeline. For example, if you'd like to analyze Google, Amazon, Coursera, Netflix, and Facebook, you would utilize the following names within your code: `GOOG`, `AMZN`, `COUR`, `NFLX`, and `META`.

You will use these names to load 2022 daily stock data into a csv from  [Polygon](https://polygon.io/). You will then use this subequent csv file to generate a report on each respective stock's standard deviation, average opening price, and average closing price per year.

## FAQ

### Using an API

To complete this project, you will need to sign up for a free API key via [Polygon](https://polygon.io/). 

### Using the CSV Module

To write & read data, we will be utilizing the [csv](https://docs.python.org/3/library/csv.html).

## Documentation
### DocStrings & Comments

Ensure that your project is appropriately commented with all necessary comments and docstrings. That is, if you have created a class, this class must also contain a docstring. Singular functions must also contain a docstring if they are not attached to a class.

### README.md

As you complete this project, you will also need to document usage & findings. Ensure that you have the following 3 sections listed in your `README.md` file.

```
# Stock Analysis

[insert project summary here]
[mention how this project should be used briefly]

## Usage

[document how to properly use this project. Does the user need to input any data? How do they run this project?]

## Findings

[document your observations here]
Which stock rose the most?

Which stock decreased the most?
```

## Validation
### Expected Output

Your output should like the screenshot below.

### Testing

To test the resiliency of your pipeline, run the following command to run a comprehensive testing suite.
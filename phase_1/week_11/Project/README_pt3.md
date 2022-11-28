# Stock Performance
## Part 3 

Now that we have our data loaded and saved, let us compute the standard deviation via the `statistics` module of each week. One week will be defined as a date range from `Monday` to `Friday`.

For this part of the project, you will create the following files:

* analysis.py

### analysis.py

Within this file. you will load in all your data from the 5 `csv` files you've created, and create a subsequent `list` of population standard deviations for each week (Monday to Friday).

We will utilize the `open()` function and `csv` module to once again read in data from our previously created csv files:

```python
stock1_data = []
with open("STOCK1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    # save this dictReader object into a list of dictionaries to analyze
    for row in reader:
        stock1_data.append(row)

# get each week of stock data, 5 iterations at a time
i = 0
stock1_stdev = []
while i < len(stock_data):
    day1 = stock_data[i]
    day2 = stock_data[i + 1]

    # how can I get days 3, 4, and 5?

    # how can I analyze the pop std dev on all these closing prices?
    
    # how can I save this std dev into the list `stock1_stdev`

    # how can i increment my "i" by 5 to represent 5 day skips?

```

Once you have created this list of standard deviations, graph and **save** a line plot to represent the volatality of this stock from March 2021 to March of this year.

You will create and save one line plot for each stock that you've analyzed. Be sure to apply appropriate labels to the title, x-axis, and y-axis. These plots do not have to be on the same figure.

## FAQ

### Using the CSV Module

To write & read data, we will be utilizing the [csv](https://docs.python.org/3/library/csv.html).

### Population Standard Deviation

Be sure to utilize the `population standard deviation` function that is available in the [statistics](https://docs.python.org/3/library/statistics.html#measures-of-spread) module. Keep in mind, this simply measures how volatile a stock is.

### Matplotlib

To create a line chart, consult the [matplotlib](https://matplotlib.org/stable/index.html) docs.



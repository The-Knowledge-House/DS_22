# Stock Performance

## Part 2

Once you have set your project up, you will create Python code within `extract.py` that requests the closing price of your 5 companies from the Polygon API from April 1 2021 to April 1 2022, and saves each day and price into two seperate lists (one called `day` and one called `closing price`). 

```
[6.81, 6.43, 6.21, ...]
["2021-04-01T00:00:00.000Z", "2021-04-02T00:00:00.000Z", "2020-04-03T00:00:00.000Z", ...]
```

Alternatively you can also save each price and day to a list of dictionaries that have the keys `day` and `price`. 

```
[
    {"date"; "2021-03-29", "price": 6.81},
    {"date"; "2021-03-30", "price": 6.43},
    ...
]
```

Consider how either data-structure will influence the format of your csv file.

Now that you have this data loaded into a data-structure, you will write it into a csv file via the `open()` function and the `csv` module.

The code below should serve as a template as to how we could do this:

```python
with open("STOCK.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    # how can I take either my two lists or my dictionary and write them to my outfile?
```

This should result in five newly created CSV files in your folder. 

* STOCK1.csv
* STOCK2.csv
* STOCK3.csv
* STOCK4.csv
* STOCK5.csv

For example, if you decided to analyze `AMZN`, `META`, `DIS`, `HD`, and `TSLA`, you will have the following files after this extraction:

* AMZN.csv
* META.csv
* DIS.csv
* HD.csv
* TSLA.csv

## FAQ

### Using the CSV Module

To write & read data, we will be utilizing the [csv](https://docs.python.org/3/library/csv.html).

## Documentation

Ensure that your project is appropriately commented with all necessary comments and docstrings. That is, if you have created a class, this class must also contain a docstring. Singular functions must also contain a docstring if they are not attached to a class.
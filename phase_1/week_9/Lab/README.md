# Education Analysis Part 2

Now that you have your filtered data prepared, you will utilize this list of dictionaries to analyze the percent change of average mathematics or reading scores from year to year of your state!

For example, if your data includes the following years: `2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008`, then you will analyze the percent change of your scores from `2001-2002`, `2002-2003`, `2003-2004`, `2004-2005`, `2005-2006`, and so on.

If you have a year missing from your data, you will calculate the percent change of the years you have available. For example, if you had data for the years `2001, 2002, 2004, 2005, 2007` (notice how the 2003 and 2006 are missing), you will generate the following columns: `2001-2002`, `2002-2004` `2004-2005`, and `2005-2007`. 

You will save this data in a list of dictionaries where the keys are `range` and `percent-change`. For the above example, you will generate the following list of dictionaries:

```
[
    {"range": "2001-2002", "percent-change": ...},
    {"range": "2002-2004", "percent-change": ...},
    ...
]
```

After you generate this list of dictionaries you could write this data-structure to a csv file using the csv module as part of your challenge.

Below are the specific goals that you will complete in this project.

## Requirements

### Get Available Years

Firstly, you must extract your avaialable years from your list of dictionaries into a list.

Keep in mind, our filtered `list_data` list will use the following structure in our code (assuming we decided to select `AVG_MATH_4_SCORE`):

```
[
    {"STATE": "NEW_YORK", "YEAR": "2001", "AVG_MATH_4_SCORE": 239},
    {"STATE": "NEW_YORK", "YEAR": "2003", "AVG_MATH_4_SCORE": 231},
    {"STATE": "NEW_YORK", "YEAR": "2005", "AVG_MATH_4_SCORE": 250},
]
```

Consider how you can loop through this list of dictionaries and save each year to a list. Using the above example, we could potentially loop through each row and append only the value of our `YEAR` key.

The following template should get you started on a solution:

```python
years = []
for row in list_data:
    # get the value of YEAR by accessing the dictionary
    # save it into years
```

Consider how you could potentially translate this to list comprehension.

### Percent Change

For this project, you will create a function called `def percent_change(list_data, year1, year2)` that takes in your list of dictionaries `list_data`, and two string years `year1` and `year2` and will return the percent change from year1 to year2.

For reference, percent change is the following [formula](https://www.wallstreetmojo.com/percentage-change-formula/). 

Consider the structure of our data.

```
[
    {"STATE": "NEW_YORK", "YEAR": "2001", "AVG_MATH_4_SCORE": 239},
    {"STATE": "NEW_YORK", "YEAR": "2003", "AVG_MATH_4_SCORE": 231},
    {"STATE": "NEW_YORK", "YEAR": "2005", "AVG_MATH_4_SCORE": 250},
]
```

Given year `2001` and year `2003`, how can we get the `AVG_MATH_4_SCORE` of both years and apply the above formula using Python?

## Applying Percent Change

You will utilize your list of `years` to get each possible sequenced pair of years. There are a number of ways we can get this, the easiest method is to use the range function and get every even year from our list of years, which we can associate with the next avaialble year.

For example:

```python
for i in range(0, len(years), 2):
    year1 = years[i]
    year2 = years[i+1]

    # calc the percent change by calling your `percent_change() function
```

Keep in mind, this implementation might not be perfect! Consider how this will fail for lists of 2 years, or 4 years.

### Documentation

Ensure that any function that you create utilizes our docstring! For reference, our docstring outlines the following:

```python
def func():
    """summary of function

    Parameters
    ----------
    x : type
        Description of parameter `x`.
    y
        Description of parameter `y` (with type not specified).

    Returns
    -------
    int
        Description of anonymous integer return value.
    """
```

In addition, all of our code should be appropriately commented, and your `README.md` should be updated to describe any additional functionality in your code.

### (Optional) Write to CSV

Using the csv module, consider how we can take this newly created list of dictionaires and write it to a file. This part of the code is optional.
## GDP Analysis

Within this project you will create a csv file that describes which state had the highest GDP for each year.

We will create our list of years using the following line of code:

```python
years = [str(year) for year in range(1997, 2021)]
```


## Challenge

Create a function called `get_percent_change` that calculates the [percent change](https://www.investopedia.com/terms/p/percentage-change.asp) of a specific state from one year to another. 

`def get_percent_change(state, year1, year2):`
    This function will get the percent change of gdp for a specific state from one specific year `year1`, to another `year2`.

    Ex: get_percent_change("New York", 2018, 2020) 

We will use this function to create a csv file of percent changes from 2019 to 2020 for each state.
  

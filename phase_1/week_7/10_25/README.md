## GDP Analysis

For this practice, you will create the following 2 functions:

`def get_highest_gdp(data, year):`  
  This function will return the name of the state had the highest GDP for a specified year. It takes in a string `year` 
  as an argument. `data` will be a `DictReader` object containing data.

`def get_lowest_gdp(data, year):`  
  This function will return the name of the state had the lowest GDP for a specified year. It takes in a string `year` 
  as an argument. `data` will be a `DictReader` object containing data.

After creating these functions, we will also need to open our data labeled `state_gdp_analysis.csv` using the `with open()` control flow statement. 

Inside of this statement, we will pass in our variable from `DictReader` to the `get_highest_gdp` and `get_lowest_gdp` functions and find the state with both the highest & lowest gdp's for the year 2020.
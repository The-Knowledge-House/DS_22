## GDP Analysis

For this practice, you will create the following 2 functions:

`def get_highest_gdp(data, year):`  
  This function will return the name of the state had the highest GDP for a specified year. It takes in a string `year` 
  as an argument. `data` will be a `DictReader` object containing data.

`def get_lowest_gdp(data, year):`  
  This function will return the name of the state had the lowest GDP for a specified year. It takes in a string `year` 
  as an argument. `data` will be a `DictReader` object containing data.

Code to read in this data will already exist. We simply need to modify our filepath to ensure that we are reading data in correctly. This data is being saved to a list called `list_data`.

We will pass this `list_data` list to the `get_highest_gdp` and `get_lowest_gdp` functions and find the state with both the highest & lowest gdp's for the year 2020.
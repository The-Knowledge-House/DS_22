import csv

# code to get years from 1997 to 2020
years = [str(y) for y in range(1997, 2021)]
col_names = ["Year", "State"]

# create empty dictionaries
year_highest = {}
year_lowest = {}

def get_highest_gdp(data, year):
    pass

def get_lowest_gdp(data, year):
    pass

# save each row into a list (TODO: do not modify code! Remove this before pushing)
list_data = []
with open("data/state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

for year in years:
    # save each result in the year_highest & year_lowest dictionaries
    pass

with open("highest_gdp.csv", "w", newline='') as outfile:
    pass

with open("lowest_gdp.csv", "w", newline='') as outfile:
    pass

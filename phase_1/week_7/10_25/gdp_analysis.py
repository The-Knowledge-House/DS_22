import csv

def get_highest_gdp(data, year):
    pass

def get_lowest_gdp(data, year):
    pass

# save each row into a list (TODO: change to your path!)
list_data = []
with open("data/state_gdp_analysis.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    # go through each year and get highest and lowest gdp
    for row in reader:
        list_data.append(row)

# get highest gdp for 2020 using "get_highest_gdp(list_data, '2020')"


# get lowest gdp for 2020 using "get_lowest_gdp(list_data, '2020')"

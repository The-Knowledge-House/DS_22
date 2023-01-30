# Flight Delays & Cost Analysis

The FAA, in its effort to modernize its technology stack, has hired your employer `AeroTrack` as a consultant to analyze its historic data and calculate performance metrics regarding the amount of delays that occur in one month.

To engineer such a pipeline, we will be using historical data pulled from the following kaggle page: https://www.kaggle.com/datasets/divyansh22/flight-delay-prediction?select=Jan_2020_ontime.csv 

To directly download this file, access the following google link: https://drive.google.com/file/d/1bschOxcTqg-Yk3-X8g5MKrew7dfjgQU0/view?usp=share_link 

Note: This file is 70 MB large, so it might take a few minutes to download. 

This csv file will be saved to our postgresql server, as explained in the section below labeled `Steps`. 

This pipeline should accomplish the following requirements: 
1. Pull the rows from our postgresql database using `psycopg2` for flights that were not diverted nor cancelled.
2. Clean the data by removing all flights which have `NaN` values in `ARR_DEL15` or `DEP_DEL15`.
3. Generate the average (ratio) of delayed flights for each airline.
4. Generate the average (ratio) of delayed flights for each airport.

These steps are further expanded below.

Make sure this pipeline is thoroughly documented and your `README` provides a brief description of this scripts functionality & purpose.

## The Data

This dataset has ~600,000 rows and contains the following 21 columns:
* DAY_OF_MONTH: day of month
* DAY_OF_WEEK: day of week (1 is Monday, 2 is Tuesday, etc)
* OP_UNIQUE_CARRIER: Unique Carrier Code. 
* OP_CARRIER_AIRLINE_ID: An identification number assigned by US DOT to identify a unique airline (carrier).
* OP_CARRIER: Code assigned by IATA and commonly used to identify a carrier.
* TAIL_NUM: Tail number of flight
* OP_CARRIER_FL_NUM: Flight Number
* ORIGIN_AIRPORT_ID: An identification number assigned by US DOT to identify a unique airport.
* ORIGIN_AIRPORT_SEQ_ID: An identification number assigned by US DOT to identify a unique airport at a given point of time.
* ORIGIN: Origin Airport
* DEST_AIRPORT_ID: An identification number assigned by US DOT to identify a unique airport.
* DEST_AIRPORT_SEQ_ID: An identification number assigned by US DOT to identify a unique airport at a given point of time.
* DEST: Destination airport
* DEP_TIME: Departure time (this should be expressed as a string)
* DEP_DEL15: 1 if departure time is delayed past 15 mins, otherwise 0.
* DEP_TIME_BLK: Departure Time Block, Hourly Intervals (this should be expressed as a string)
* ARR_TIME: Arrival time (this should be expressed as a string)
* ARR_DEL15: 1 if arrival time is delayed past 15 mins, otherwise 0.
* CANCELLED: Whether or not this flight was cancelled (1 or 0).
* DIVERTED: Whether or not this flight was diverted (1 or 0).
* DISTANCE: Miles traveled for this flight.

We are namely focused on the columns labeled `ARR_DEL15` and `DEP_DEL15`, since these two columns are our indicators if a flight was delayed either in its departure or arrival. For this pipeline, we will not consider these two types of delays to be different from one another.

The dataset is further described here: https://www.kaggle.com/datasets/divyansh22/flight-delay-prediction?select=Jan_2020_ontime.csv 

## Steps

### Step 0: Setup

To begin this project, we must firstly set up our csv file within our postgres database.

Log into pgAdmin and create a table that describes a table named `real_flight` in your `flights` database.

To create this table, you must first utilize the `CREATE TABLE` query to specify the table name & it's attributes. Keep in mind that we **must** include the present columns mentioned in the section titled `The Data` as attributes. Consider what attribute types are associated with each attribute?

For example, `DAY_OF_MONTH` might be an `INT`, while `OP_UNIQUE_CARRIER` could be described as a `CHAR(2)` since the maximum characters of this column is seemingly 2. 

Ex:
```sql
CREATE TABLE real_flight(
    DAY_OF_MONTH INT,
    DAY_OF_WEEK INT,
    OP_UNIQUE_CARRIER ...
    OP_CARRIER_AIRLINE_ID ...
	OP_CARRIER ...
	TAIL_NUM ...
	OP_CARRIER_FL_NUM ...
	ORIGIN_AIRPORT_ID ...
	ORIGIN_AIRPORT_SEQ_ID ...
	ORIGIN ...
	DEST_AIRPORT_ID ...
	DEST_AIRPORT_SEQ_ID ...
	DEST ...
	DEP_TIME ...
	DEP_DEL15 ...
	DEP_TIME_BLK ...
	ARR_TIME ...
	ARR_DEL15 ...
	CANCELLED ...
	DIVERTED ...
	DISTANCE ...
);
```

You should execute this query once within your database.

After we execute this query, we will then work on populating this table using the data saved within our csv file.

To accomplish this we will directly import our csv file using pgAdmin using the section labeled `To import CSV to PostgreSQL with pgAdmin, follow the below steps` within the following link: https://blog.skyvia.com/complete-guide-on-how-to-import-and-export-csv-files-to-postgresql/ 

After setting up your database, create a GitHub repository within your profile & clone it to your computer.

Once you have this repository created & cloned, create the following files:
* README.md
* get_delays.py

All subsequent code will be written in Python within `get_delays.py`.

### Step 1: Pull the Table

Now that you have your table loaded into your database, pull in your data using `psycopg2` and save it into a pandas dataframe. Be sure to only select rows for flights that were **not diverted nor cancelled** using your SQL query.

### Step 2: Clean the Data

Using your `pandas`, drop all rows that contain `NaN` values in either `ARR_DEL15` or `DEP_DEL15`. 

### Step 3: Generate Ratios for Airline

Using `pandas`, create a new column within your original dataframe labeled `DELAYED` that will be marked as `1` if either `ARR_DEL15` or `DEP_DEL15` are `True`, and be marked as `0` if both `ARR_DEL15` and `DEP_DEL15` are `False`.

After creating this column, create a new dataframe that groups each airline (`OP_UNIQUE_CARRIER`) into groups and calculates the ratio of delays (`DELAYED`) for each airline.

Keep in mind that an average of 1's and 0's creates a ratio that represents how many values are `1` (delayed flights) and how many values are `0` (non-delayed flights).

Sort this delay ratio from highest to lowest, and save this dataframe as a `csv` file within your repository labeled `delayed_airlines.csv`.

### Step 4: Generate Ratios for Airports

After creating this column, create a new dataframe that groups each origin airport (`ORIGIN_AIRPORT_ID`) into groups and calculates the ratio of delays (`DELAYED`) for each airline.

Keep in mind that an average of 1's and 0's creates a ratio that represents how many values are `1` (delayed flights) and how many values are `0` (non-delayed flights).

Sort this delay ratio from highest to lowest, and save this dataframe as a `csv` file within your repository labeled `delayed_airports.csv`.

# Challenge (Optional): Airline Rating vs. Delays

In addition to our delayed flights data, we also have a csv file representing the "JD Powers" ranking of airlines:  https://drive.google.com/file/d/1HqnYzqqh9UvTf-fVH0AF6plHuAEqdKpe/view?usp=share_link 

Load this csv file into your `get_delays.py` file, and [join](https://pandas.pydata.org/docs/user_guide/merging.html#database-style-dataframe-or-named-series-joining-merging) it to your dataframe that describes the ratio of delays per airline. You will use pandas to align each airline with its appropriate ratio of delays, and rating.

Once you create this new joined dataframe, use [linear regression](https://www.statology.org/r-squared-in-python/) to generate an R^2 value for ratio of delays vs. JD powers score. An R^2 value below 0.5 is not significant, aka indicates that ratio of delays might not predict customer satisfaction.

What do you notice about your generated R^2 value? 


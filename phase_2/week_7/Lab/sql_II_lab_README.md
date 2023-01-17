# Flight Delays & Cost Analysis

The FAA, in its effort to modernize its technology stack, has hired your employer `AeroTrack` as a consultant to analyze its historic data and calculate performance metrics regarding the amount of delays that occur in one month.

To engineer such a pipeline, we will be using historical data pulled from the following kaggle page: https://www.kaggle.com/datasets/divyansh22/flight-delay-prediction?select=Jan_2020_ontime.csv 

To directly download this file, access the following google link: https://drive.google.com/file/d/1bschOxcTqg-Yk3-X8g5MKrew7dfjgQU0/view?usp=share_link 

Note: This file is 70 MB large, so it might take a few minutes to download. 

This csv file will be saved to our postgresql server, as explained in the section below labeled `Steps`. 

This pipeline should accomplish the following requirements: 
1. Pull the rows from our postgresql database using `psycopg2` for flights that were not diverted nor cancelled.
2. Clean the data by removing all flights which have `NaN` values in `ARR_DEL15` or `DEP_DEL15`
3. Generate the average (ratio) of delayed flights for each airline 
4. Save this table back into our database

And remember, make sure this pipeline is thoroughly documented.

These steps are further expanded below.

## The Data

This dataset has ~600,000 rows and contains the following 21 columns:
* DAY_OF_MONTH
* DAY_OF_WEEK
* OP_UNIQUE_CARRIER
* OP_CARRIER_AIRLINE_ID
* OP_CARRIER
* TAIL_NUM
* OP_CARRIER_FL_NUM
* ORIGIN_AIRPORT_ID
* ORIGIN_AIRPORT_SEQ_ID
* ORIGIN
* DEST_AIRPORT_ID
* DEST_AIRPORT_SEQ_ID
* DEST
* DEP_TIME
* DEP_DEL15
* DEP_TIME_BLK
* ARR_TIME
* ARR_DEL15
* CANCELLED
* DIVERTED
* DISTANCE

We are namely focused on the columns labeled `ARR_DEL15` and `DEP_DEL15`, since these two columns are our indicators if a flight was delayed either in its departure or arrival. For this pipeline, we will not consider these two types of delays to be different from one another.

The dataset is further described here: https://www.kaggle.com/datasets/divyansh22/flight-delay-prediction?select=Jan_2020_ontime.csv 

## Steps

### Step 0: Setup

To begin this project, we must firstly set up our csv file within our postgres database.

Log into pgAdmin and create a table that describes a table named `flights` 

After we complete this

Files to create:
* README.md
* 
* 

### Step 1: Pull the Table



### Step 2 & 3: Clean the Data



### Step 4: Generate Ratio



### Step 5: Save the Table



# Challenge (Optional): Airline Rating vs. Delays


# End of Phase Project 2 Outcomes & Hints

## extract.py

After implementing your `extract.py` file, you should have a dataframe of 11,206 rows & 19 columns. You wll have 5999 missing values in your `work_from_home` column.

You should have the following columns in your joined dataframe as well:
```
'id', 'salary_pay', 'salary_rate', 'salary_avg', 'salary_min',
'salary_max', 'salary_hourly', 'salary_yearly', 'salary_standardized',
'title', 'company_name', 'location', 'via', 'extensions', 'posted_at',
'schedule_type', 'work_from_home', 'date_time', 'description_tokens'
```

Lastly, the first 5 rows of your dataframe should look like the following (this image excludes all columns after `schedule_type`):

![image](https://user-images.githubusercontent.com/26397102/223221189-eb74db09-8db5-4bf6-89ba-9e66d8e98aaf.png)

This dataframe should be saved into your `data` folder (ex: `data/joined_data.csv`). 

**Hints**
* We must use the same exact `sqlalchemy` objects from our [notes](https://github.com/The-Knowledge-House/DS_22/blob/main/phase_2/week_9/1_31/intermediate_sql_II_notes.ipynb) to get our data imported. 
    * Take note of the different login information!
* How can we [join](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html) these 3 dataframes on the primary_key?

## transform.py

Firstly, we must replace all missing values in `work_from_home` with false. We will go from having `5999` missing values to `0` in our `work_from_home` column.

Next, we will encode our `description_tokens`. This step is tricky, but doable. A technique that we must use, but did not cover explicitly is `encoding`.

We have a column labeled `description_tokens` that describes a list of technical skills. For example, a job that requires `Python`, `SQL` and `Tableau` will have the following values in a list: `["python", "sql", "tableau"]`.

Our goal is to "encode" each skill into a column of 1's and 0's. That is, the `["python", "sql", "tableau"]` list should become a new dataframe where we have `1`'s in the `python`, `sql`, and `tableau` columns. The other columns such as `excel`, `vba`, `postgres`, etc will contain the values of zero.

Ex:

| description_tokens                |
| --------------------------------- | 
| ["python", "sql", "tableau"]      | 
| ["python", "r"]                   | 
| ["sql", "tableau"]                | 
| ["sql", "tableau", "excel]        |  

Becomes...

| python | sql   | tableau  | excel | r  | ... |
| ------ | ----- | -------- | ----- | -- | --- |
| 1      | 1     | 1        | 0     | 0  | ... |
| 1      | 0     | 0        | 0     | 1  | ... |
| 0      | 1     | 1        | 0     | 0  | ... |
| 0      | 1     | 1        | 1     | 0  | ... |

The bottom image is a sample of what this dataframe should look like:

![image](https://user-images.githubusercontent.com/26397102/223249103-0de2bf74-ca28-4cf5-aad1-a11c649bcb2e.png)


By the end of this encoding, we will have 107 new columns. In total, we will have a new dataframe of 11206 rows and 137 columns.

After these two transformations, we will save our dataframe into a csv file in our `data/` folder and label it `encoded_data.csv`. This data will be used within the `eda.ipynb` step of our project.

We are not done, however, with our transformations. In the final step of this file, we will drop all rows that contain null values in the `salary_standardized` column. we will then save this dataframe as `clean_data.csv` in preparation for the `predict.ipynb` step of our project 

**Hints**
* Look up how to "fill null values" in a column to accomplish the first step where we transform the `work_from_home` column.
* A major hurdle with our `description_tokens` column is the fact that this is a **string** that represents a list. Preferably, we would want this column to express a list, so that we can apply the [MulitLabelBinarizer](https://stackoverflow.com/questions/45312377/how-to-one-hot-encode-from-a-pandas-column-containing-a-list) to our column
    * To figure out how we can accomplish this, try googling the following:
        * "pandas convert string representation of list to list"
        * "convert string list to list in pandas"
        * etc
* After converting this column into a list, we can then utilize a sklearn [encoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MultiLabelBinarizer.html) to encode this data
* Lastly, look up how you can "drop" rows that have null values in a specific column to accomplish the final transformation


## eda.ipynb

While we will comprehensively go over this step tomorrow, your `eda` step should entail the following similair visualizations:


**Standard Salaries Distribution**
![image](https://user-images.githubusercontent.com/26397102/223257145-44846b2a-2c7c-4697-b012-64435a6635e2.png)

**Standard Salaries Remote Distribution**
![image](https://user-images.githubusercontent.com/26397102/223257468-15ab944b-95b2-4380-a884-3a5c23fce269.png)


**Standard Salaries Non-remote Distribution**
![image](https://user-images.githubusercontent.com/26397102/223257647-171cc59e-bc13-4680-8c1f-728146e4bc0c.png)

**Python Salaries Box-Plots**
![image](https://user-images.githubusercontent.com/26397102/223258178-3f2331d8-5183-4ebf-ab89-3ffafc08b74e.png)

**SQL Salaries Box-Plots**
![image](https://user-images.githubusercontent.com/26397102/223258565-8065645c-fc80-4008-842e-73c2994a27bd.png)

**Bar-Chart Skills**
![image](https://user-images.githubusercontent.com/26397102/223259022-f6a72f13-bb5c-4300-ac96-297b41f3d25b.png)
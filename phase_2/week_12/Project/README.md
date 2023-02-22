# End of Phase Project 2 

Your analytics consulting company, `Central Tendecy` has recently been awarded a contract from the recruitment-advertisement tech-company `InRecruit`. You've been tasked with working on a team of other analysts in order to generate a comprehensive pipeline & analysis of **real** job-data that they've scraped since `11/4/2022`.

Mainly, `InRecruit` seeks to address the following inferential questions:

* What are the most sought-after skills for data-analyst positions?
* Which **cities** are hiring the most data-analysts?
* Which **companies** are hiring the most data-analysts?
* How do salary outcomes differ between remote-work & non-remote work?

As well as make the following predictive models:

* Can we predict standardized salary using a regression model if we know the skills required, schedule, & option for remote work?

To better help understand this dataset & the requirements of this project the companies [planning documents](https://drive.google.com/drive/folders/1z4EwdbyfUzf-FuRTJfVMaRSm5-R25viA?usp=share_link) have been shared with you.

While you are not allowed to directly log into the companies `aws` account, you will be given credentials to directly pull tables from their [AWS Relational Database](https://aws.amazon.com/rds/). To get the password please directly request the pseudo-staff of `InRecruit` (Mo & Farukh) either during class-time or during office-hours.

Keep in mind that these credentials **must** be hidden!

## Requirements

For this project, you must create the outlined files in a **GitHub repository**:

* extract.py
* transform.ipynb
* eda.ipynb
* predict.ipynb
* config.py & gitignore
* README.md

the following folders must also be created

* data/
* images/

You will be submitting a link to your GitHub repo as the finished product. Below describes the specifications & requirements for each file:

### config.py & .gitignore

Considering that we are working with priveledged information stored on a secure database, we want to ensure that the login information is **never** exposed. As soon as you start your project, create a `config.py` file with your connection information that you ignore via `.gitignore`.

### extract.py

This `py` file will utilize `sql-alchemy` to extract data kept in the database. The root user for this database is `postgres`, the hostname is `rds-pg-jobs.chfavwsr5bmp.us-east-1.rds.amazonaws.com`, the port is `5432` and the database name is `postgres`. As the password is sensitive information, we ask that you get it from one of us and then use in it a secure way (no commiting the password directly to GitHub!).

To find out more about the tables that you are working with, check out the [planning documents](https://drive.google.com/drive/folders/1z4EwdbyfUzf-FuRTJfVMaRSm5-R25viA?usp=share_link).

**Requirements**
* Extract all 3 tables from the `Amazon RDS postgres` database.
* Create 3 new pandas `dataframes` using these 3 tables.
* Join all 3 tables together on their `primary key` (take a look at your planning documents).
* Write this joined dataframe to the `data/` folder as a csv file.

**Tools Used**
* sqlalchemy

**Relevant Notes**
* [Phase 2 Week 9 2/01](https://classroom.google.com/u/0/c/NTQ2NzMzMDQwMDM5/m/NTg4MDk1NTE2NDU4/details)
* [Phase 2 Week 9 1/31](https://classroom.google.com/u/0/c/NTQ2NzMzMDQwMDM5/m/NTg3ODExMzM0Mzk0/details)

### transform.ipynb

Looking at this dataframe, we notice that there are a lot of `sparse` (null-filled) rows. In addition our `description_tokens` is unhelpful in displaying what skills are required for a job. Let's clean up our dataset by doing the following.

**Requirements**
* Create a new column for each possible skill specified in the `description_tokens` column
    * For example, if the `description_tokens` column contains `['python', 'excel', 'sql']`, you will mark 3 columns labeled `description_tokens_python`, `description_tokens_excel`, `description_tokens_sql` to all  be 1, while all other skills that might appear will be labeled 0 (ex: `description_tokens_tableau`, `description_tokens_java`, etc)
    * This is called getting [dummy variables](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html) or [one-hot-encoding](https://www.educative.io/answers/one-hot-encoding-in-python)
    * Utilize the internet to figure out how to accomplish this task, we will be providing minimal guidance
    * Save this dataframe with newly engineered features back into the `data/` folder for later use in `eda.ipynb`
* Create a new dataframe that drops all rows that contain `null` values in the `salary_standardized` column from the newly engineered dataframe above
    * Save this dataframe to your `data/` folder for later use in `predict.ipynb`
* Fill in all missing values in the `work_from_home` column to be `False`.

**Tools Used**
* pandas

**Relevant Notes**
* [Phase 2 Week 2 12/12](https://classroom.google.com/u/0/c/NTQ2NzMzMDQwMDM5/m/NTc4NTE5NDcxMTc5/details)
* [Phase 2 Week 2 12/13](https://classroom.google.com/u/0/c/NTQ2NzMzMDQwMDM5/m/NTc4OTE3NTM3MjEw/details)
* [Phase 2 Week 5 01/03](https://classroom.google.com/u/0/c/NTQ2NzMzMDQwMDM5/a/NTA5Mjc5MjQyMDcx/details)
* [Phase 2 Week 6 01/09](https://classroom.google.com/u/0/c/NTQ2NzMzMDQwMDM5/m/NTgyMDgxMTY5NTQ4/details)

### eda.ipynb

Now that we have cleaned and prepared data, we will get to work answering our `inferential` questions:
* What are the most sought-after skills for data-analyst positions?
* Which **cities** are hiring the most data-analysts?
* Which **companies** are hiring the most data-analysts?
* How do salary outcomes differ between remote-work & non-remote work?

**Requirements**
* Perform distribution testing & visualization on `standard_salaries`
* Perform distribution testing & visualization on `standard_salaries`, grouping `work_from_home == TRUE` and `work_from_home == FALSE` positions together
* Calculate & visualize the frequency of skill-occurence in your dataframe
    * What are the top 5 most-requested skills?
    * Visualize the distribution of `standard_salaries` for `sql` positions
    * Visualize the distribution of `standard_salaries` for `python` positions
    * Visualize the distribution of `standard_salaries` for `tableau` positions
* Calculate & visualize the frequency of city-occurence in your dataframe
    * What are the top 5 cities for data analyst positions?
    * Visualize the distribution of `standard_salaries` for `Los Angeles` positions
    * Visualize the distribution of `standard_salaries` for `New York City` positions
    * Visualize the distribution of `standard_salaries` for `Atlanta` positions
* Calculate & visualize the frequency of company-occurence in your dataframe
    * What are the top 5 companies for data analyst positions?
    * Visualize the distribution of `standard_salaries` for 3 companies of your choice (that can be found in the dataframe)
* Create write-up in your `README` of the trends, statistics, & visualizations you've noticed

**Tools Used**
* seaborn
* pandas
* matplotlib

**Relevant Notes**
* [Phase 2 Week 10 02/06](https://classroom.google.com/u/0/c/NTQ2NzMzMDQwMDM5/m/NTkxMjUzNDg1Mjkw/details)
* [Phase 2 Week 10 02/07](https://classroom.google.com/u/0/c/NTQ2NzMzMDQwMDM5/m/NTkxNDkwMTU3NTk2/details)

### predict.ipynb

Lastly, you will create a multivariate regression model using the csv file that contains no null-values in your `standard_salaries` column. 

**Requirements**
* Create a linear regression model with `standard_salaries` as your dependent variable, and all listed `description_token_skills`, `schedule`, & `work_from_home` as your independent variables.
* Print out it's accuracy (R2 value)
* Print out it's coefficients `lin.coef_`
* Create a writeup of the predictive power of your model in your `README`. Does this have good predictive power (is the r2 value high)?

**Tools Used**
* sklearn

**Relevant Notes**
* [Phase 2 Week 12 02/21](https://classroom.google.com/u/0/c/NTQ2NzMzMDQwMDM5/m/NTk0MDU5MDg3MTgw/details)


### README.md

After completing your analysis, you **must** create a README describing your **methodology**, **visuals**, **results**, & **next-actions**. Any repository without a README will not be accepted.

## Structure

Your repository will be required to abide by the following structure:

```yaml
├── data
│   ├── job_salary_skills.csv
├── images
│   ├── remote_work_dist.png
│   ├── nonremote_work_dist.png
│   ├── ...
├── config.py
├── .gitignore
├── extract.ipynb
├── transform.ipynb
├── eda.ipynb
├── predict.ipynb
```

## Sprint 7 Deliverables

### Begin EDA 
 
Using `sqlalchemy`, you will create a jupyter notebook titled `eda.ipynb` that extracts data from your Amazon database and prepares it for data analysis. You will use your understanding of sqlalchemy to create a session and automap data tables as objects in Python. You will then apply all relevant data transformations to support your EDA.

After loading this data in, you will begin your univariate analysis which will entail:
* histograms
* qq-plots
* ks-tests
* confidence intervals

For the next sprint, you will complete bivariate analysis.

This will be completed via the script:

* `eda.ipynb`

### Implement pl/sql Functions

Within your database, you will also implement 3 named procedures that calculate important metrics that a non-technically minded manager might want to discover (ex: average salary of job, number of comments in a day, etc). You will create a `sql` file in your `sql` folder that will contain pl/pgsql syntax that implements these 3 procedures. After completing this file, you will then create a `.py` file that loads these procedures into your schema.

Since you are writing `sql` syntax in a vaccuum, it is a good idea to test out your queries as you write them via `pgAdmin`. To discover how we can connect our `postgresql` database to pgAdmin, check out the following documentation: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToPostgreSQLInstance.html 

Since each group has a fundamentally different dataset, we will prompt you to engineer specific functions within your breakout rooms.

This section will be completed via the following scripts

* `sql/function.sql`
* `sql/function_load.sql`

### Implement SQLAlchemy Script to call Functions from Command Line

In addition to this script, you will also implement a command-line-interface python file that allows a manager to clone your repository and simply get information on your database by running a script.

Utilize the skeleton code labeled `query_ex.py` located within this folder to discover how we can accomplish this. 

This script will prompt the command-line for input. A respective sql function will be called based on what input is provided from the command line.

### Further Develop Documentation

As always, ensure that you are properly documenting code and updating your README as you develop your codebase.

### Ensure Branching

Going forward we will check commit history to ensure that each team member is contributing equally to the codebase, so be sure to work solely in a branch-based environment!

### Collect More Data (If Applicable) & Integrate

Remember! The more data the better. Always be on the lookout for ways to increase your statistical power.

### Tackle Recommended Next Actions

Lastly, if you are complete with all above listed tasks, you should revisit recommended next actions to ensure code quality. 

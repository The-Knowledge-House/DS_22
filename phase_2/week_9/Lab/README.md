## EPI & Various Metrics

For this project, we will continue utilizing our 2010 `EPI` dataset in order to explore which metrics might correlate with EPI scores such as water health or air health.

Instead of using the GDP dataframe however, we will choose from one of the following datasets.

* [Corruption Index](https://drive.google.com/file/d/1KccvnTLBHNR4nnkO6vpwc_Bf1kr49K4r/view?usp=sharing)
* [HDI](https://drive.google.com/file/d/1U2xwG_roCdRYwt3pxcWaxtD8tfgDSeTC/view?usp=share_link)
* [Life Expectancy (same dataset as above)](https://drive.google.com/file/d/1U2xwG_roCdRYwt3pxcWaxtD8tfgDSeTC/view?usp=share_link)

We will be saving these datasets into our pipeline using the `read_csv` function from `pandas`.

Alternatively, if you would like to use your own dataset that describes some quantitative measure for countries in 2010, you may do so as well.

This pipeline should accomplish the following requirements: 
1. Pull EPI data from your postgres databases using `sqlalchemy`, and save it into a dataframe.
2. Load your chosen csv file into your pipeline as a dataframe via `pandas`, and then save it as a table to your postgres database.
3. Filter your data according to a specific geographic subregion.
4. Analyze the relationship visually between one column in your geographic `epi` dataframe (such as `water_h` or `air_h`) and one column in your chosen new dataframe.
5. Generate documentation.
6. (Optional) Create a linear regression model to predict how your chosen metric influences the dependent `epi` metric.

We will be using the following packages to create this pipeline
* [pandas](https://pandas.pydata.org/docs/)
* [sqlalchemy](https://www.sqlalchemy.org/)

Use the above documentation to complete this project!

## Step 0 : Setup your repo

To set up this project, you will create a GitHub repository where you will commit and push all your changes.

For a refresher as to how to use GitHub, check out the following link: https://www.youtube.com/watch?v=JPKOESR1k04&t=5s&ab_channel=DevTips 

Within this GitHub repo, you will have the following files:

* README.md
* eda.py

## Step 1 : Extract your data

Using sqlalchemy, extract your `epi` dataframe into your `eda.py` file.

After saving your `epi` table as a dataframe, you will then create a new dataframe using the `pandas` package, which will be your newly downloaded csv file. This could be the `corruption index` or the `hdi` csv file, or any other dataset that contains quantitative infromation for each country in 2010.

After importing your new pandas dataframe, save it back into your `postgres` database.

## Step 2

Next, you will filter your `epi` dataframe to only include one geographic subregion. For example, we could only include epi data from central europe by running the code

```python
epi_ce = epi_df[epi_df["GEO_subregion"] == "Central Europe"]
```

After filtering your epi dataframe, join it on your newly chosen dataframe that describes some sort of quantitative measure for each country. 

## Step 3

Next, generate 3 visualizations (scatter-plots, bar-graphs, histograms) that describe the relationship between variables in your imported dataframe and some metric from your `epi` dataframe. 

For example, you could generate 3 visualizations on `water_h` and `gdp`.

Be sure to save these visualizations to your repository and include reference to them in your README.

Finally, write up a brief summary of your findings and tools used in your README.

## Step 4 (Optional Challenge)

Using your joined dataframe, create a linear regression model that will create a statistical-learning model between one target column from your `epi` dataframe and one independent variable from your newly created dataframe.

https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
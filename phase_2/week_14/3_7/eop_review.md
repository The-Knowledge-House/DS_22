# End of Phase Project 2 Outcomes & Hints

**Erratum**

* When doing the EDA step, please be sure to utilize your **cleaned** dataframe. Leaving nulls will result in `nan` values for your statistical measures.
* When doing EDA, choose 3 locations that are not `NY`, `LA`, or `ATL`. Unfortunately our cleaned dataframe removes columns that describe positions located in these cities. Either skip this step completely or just use 3 other locations.
* When doing your predict step, only use a subset of skills & features that you notice lead to higher (or lower) salary. For example, it looks like `remote` work might actually stipulate a lower salary, whereas `sql` seems to lead to a higher salary..
    * Basically, utilize your EDA to determine which features to use.

# eda.ipynb

Your `eda` step should guarantee the following outcomes (excluding the optional visualizations):

---------------------------------------

## Full Standard Salaries Visualizations & Statistics

**Histogram**  
![image](https://user-images.githubusercontent.com/26397102/223506867-617d1413-6a92-4957-8054-02c48f4ed84e.png)  

**Box-Plot**  
![image](https://user-images.githubusercontent.com/26397102/223507102-04956d64-176b-4622-bf50-674990792790.png)  

**KS Test**  
```
KstestResult(statistic=0.0884061189073454, pvalue=1.3144684207219956e-15)
```  

---------------------------------------

## Remote Standard Salaries Visualizations & Statistics

**Dimensions**  
```
Non_Remote
(897, 137)
```  
**Histogram**  
![image](https://user-images.githubusercontent.com/26397102/223507872-f745ee90-398e-4fdd-aed2-d464194649a3.png)  


**KS Test**  
```
KstestResult(statistic=0.07387056224442179, pvalue=9.112003142853433e-07)
```   

---------------------------------------

## Non-remote Standard Salaries Visualizations & Statistics

**Dimensions**  
```
Remote
(1332, 137)
```  
**Histogram**  
![image](https://user-images.githubusercontent.com/26397102/223509564-9acf4a13-9a81-4a35-b40d-03caf179eb91.png)

**KS Test**  
```
KstestResult(statistic=0.18113066066731165, pvalue=3.184538697598516e-26)
```   

---------------------------------------

## Comparison Of Remote + Non-remote  

**Box-Plot**  
![image](https://user-images.githubusercontent.com/26397102/223509311-6f123e65-46f0-4433-b8bb-b0e34b68e366.png)  

**KDE Plot (Optional)**  
![image](https://user-images.githubusercontent.com/26397102/223527535-e24ac1e4-4018-4049-ad38-9b2fc87b2c79.png)

**Confidence Interval (Optional)**  
![image](https://user-images.githubusercontent.com/26397102/223516344-664ad368-230f-4e8a-b4b1-c25c1a143ab6.png)  

**T-Test (Optional)**  
```
Ttest_indResult(statistic=-3.9625310257616233, pvalue=7.649327941393824e-05)
```

## Ranked Skills

**Bar-Chart**   
![image](https://user-images.githubusercontent.com/26397102/223510916-738552d6-f015-4d28-9475-b434ea317bd7.png) 

---------------------------------------

## SQL Visualizations & Statistics

**Box-Plot**  
![image](https://user-images.githubusercontent.com/26397102/223519210-c0f1e2f0-093a-4cad-abf7-c46ca4470b04.png)

**Histogram**  
![image](https://user-images.githubusercontent.com/26397102/223527774-d47b7f6c-9894-478b-8d75-f97240550552.png)

**KS Test**  
```
KstestResult(statistic=0.14859694970660242, pvalue=2.428624055011539e-22)
```   

**KDE Plot (Optional)**  
![image](https://user-images.githubusercontent.com/26397102/223528338-50cb3da4-e948-4464-9164-df714c212815.png)

**Confidence Interval (Optional)**   
![image](https://user-images.githubusercontent.com/26397102/223519320-1c7f927d-97d7-4317-9749-460ba0509563.png)  

**T-Test (Optional)**  
```
Ttest_indResult(statistic=-7.200932462946706, pvalue=8.163860422881086e-13)
```

--------------------------------------- 

## Python Visualizations & Statistics

**Box-Plot**  
![image](https://user-images.githubusercontent.com/26397102/223530004-488027d2-4e02-406d-9c54-98676a864678.png)


**Histogram**  
![image](https://user-images.githubusercontent.com/26397102/223529190-32710886-1aa9-4121-9416-a7a8478d1da5.png)

**KS Test**  
```
KstestResult(statistic=0.10816134598371768, pvalue=5.1004787412886686e-05)
```   

**KDE Plot (Optional)**  
![image](https://user-images.githubusercontent.com/26397102/223529323-fb0e270d-c0f0-4795-8884-55780ecef6ac.png)

**Confidence Interval (Optional)**   
![image](https://user-images.githubusercontent.com/26397102/223529620-955e81c8-772c-443c-b77d-ecfb8264ecb9.png)

**T-Test (Optional)**  
```
Ttest_indResult(statistic=-4.764643115726993, pvalue=2.013804061910089e-06)
```

---------------------------------------

## Tableau Visualizations & Statistics

**Box-Plot**  
![image](https://user-images.githubusercontent.com/26397102/223537866-f6e84561-1ded-4841-aed6-b29d895a6ee8.png)

**Histogram**  
![image](https://user-images.githubusercontent.com/26397102/223538222-3ec10081-777a-475a-8e7d-70a82183ed8b.png)

**KS Test**  
```
KstestResult(statistic=0.22652993258106247, pvalue=1.9059409500066205e-33)
```   

**KDE Plot (Optional)**  
![image](https://user-images.githubusercontent.com/26397102/223538322-e182d8f2-de07-453b-8e1f-51e661b8290c.png)

**Confidence Interval (Optional)**   
![image](https://user-images.githubusercontent.com/26397102/223538512-3f30437b-aaa1-4649-b879-f3a5d195afad.png)

**T-Test (Optional)**  
```
Ttest_indResult(statistic=-2.6199543704935193, pvalue=0.008853883572145777)
```

---------------------------------------

## Ranked Cities

**Bar-Chart**   
![image](https://user-images.githubusercontent.com/26397102/223538873-b2c28ab8-0860-4b19-8c0a-cc8fb26bfa07.png)

---------------------------------------

## Location 1, 2, & 3 Visualizations & Statistics
**Box-Chart**   
![image](https://user-images.githubusercontent.com/26397102/223540571-6d67d764-cc9b-4dc5-ae6c-3da0e9be7973.png)

**Confidence Interval (Optional)**  
![image](https://user-images.githubusercontent.com/26397102/223540802-a957034a-9544-4d9d-a517-421b5fdbdbb2.png)

---------------------------------------

## Ranked Companies

**Bar-Chart**   
![image](https://user-images.githubusercontent.com/26397102/223538807-2f33b865-2b98-4d4a-b5cb-61febe1a7688.png) 

---------------------------------------

## Company 1, 2, & 3 Visualizations & Statistics

**Box-Chart**   
![image](https://user-images.githubusercontent.com/26397102/223541193-d485bded-9862-4f56-a958-90390e35d2a6.png)

**Confidence Interval (Optional)**  
![image](https://user-images.githubusercontent.com/26397102/223541589-6fdf0300-fde1-4927-bb4f-1e1015647a95.png)

---------------------------------------

## Hints
* Documentation is your friend! Utilize the following links to figure out how to create the above visualizations.
    * [Bar-Plots](https://seaborn.pydata.org/generated/seaborn.barplot.html)
    * [Histogram](https://seaborn.pydata.org/generated/seaborn.histplot.html)
    * [KS-Test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.kstest.html)
    * [KDE-Plot](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)
    * [T-Test](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)

# predict.ipynb
For this step, create a multi-variate regression model using `sklearn` using the features that you've visualized in order to predict salary.

After creating this model, print out the `R2` value to gauge accuracy. Keep in mind, this isnt the **most** important metric. Print out model coefficients as well to check which features result in higher or lower salaries.

## Hints
* [Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

# README

After completing your EDA & predictions, you must write up a README discussing your observations & results. You can detail the following sections in this file:
```
# Project Title
A summary of your project, along with which tools you used to accomplish this. (A Python ETL & EDA pipeline to analyze the current job market for data analysts. I utilize Amazon PostgreSQL, sqlalchemy, seaborn, and sklearn to figure out which skills are the most valuable.)

## Methodology
A step by step outline of what you did in this project.

## Visuals
Visuals of distribution & what you noticed from the visualization

## Results
What is the end result of this project? Which skills are the most valuable? Which features predict for higher wages?

## Next Actions
What could you do next to make this project even more "powerful."

```

# Optional Challenges

* You'll notice that I compute the following metrics & visualizations in each category. Try this out as well if you'd like to add more validity to your analysis. We will discuss the mathematical foundations of these metrics & how they contribute to our machine learning models.
    * [Confidence Interval](https://www.scribbr.com/statistics/confidence-interval/): What are the chances of this mean appearing 95% of the time we sample randomly? You'll notice that every non-overlapping confidence interval results in greater significance in our model.
        * [Plotting Confidence Intervals](https://seaborn.pydata.org/generated/seaborn.barplot.html)
    * [T-Tests](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html): what are the chances that the difference in means from these two groups occured due to pure random chance?
* You'll also notice that our `salary_standardized` column is right-skewed. Feel free to go ahead and ignore these outliers using a one of methodologies listed below. Keep in mind that removing outliers allows our models & inferences to be more accurate:
    * [Utilize z-score](https://stackoverflow.com/questions/23199796/detect-and-exclude-outliers-in-a-pandas-dataframe)
    * [IQR](https://stackoverflow.com/questions/35827863/remove-outliers-in-pandas-dataframe-using-percentiles)
* There are a lot of jobs posted by recruiting agencies collected from this web-scraper. Go ahead and ignore these jobs.
    * This includes jobs posted by the following companies: 
    ```
    ignore_comps = ["Upwork", "Corporate", "Talentify.io", "Dice", "Staffigo Technical Services, LLC", "Insight Global", "Harnham", "WayUp", "Jobot", 
                "Addison Group", "Applicantz", "Analytic Recruiting Inc.", "Confidential"]
    ```
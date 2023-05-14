## Sprint 8 Deliverables

### Complete EDA 

For sprint 8, continue your `EDA` by completing the bivariate portion of your analysis. This is your exploration of the relationship between your target variable & your predictor variables. This should also include the relationships between your predictors to check for correlation.

Your bivariate analysis will entail:
* scatter-plots
* correlation heat-maps
* box-plots
* line-plots

This will be completed within the same script as in Sprint 7:

* `eda.ipynb`

### Begin CDA

Once completing `EDA`, you should utilize the insights gleaned from this exploration to further transform your data and confirm your findings by utilizing statistical learning models and hypothesis tests.

For example, did your data display non-normality? This could indicate that you should normalize your dataset through the removal of outliers or log-normalization.

Perhaps you can also utilize a non-parametric regressor to discover patterns & insights.

You should create at least 4 prediction-tasks for your data & select the model that displays the least error within your test set. However, you should also utilize the statistical inference from the other 3 models to motivate your discussion & findings.

Depending on your prediction-task, you should either utilize regressors or classifiers.

For regressors you could use:
* Linear Regression
* LASSO
* Ridge
* Elastic-net (a combination of LASSO & Ridge)
* Random Forest Regressors

Whereas for classifiers you could use:
* Logistic Regression
* Decision Trees
* Random Forest Classifiers

Feel free to utilize powerful statistical learning methods that we have not yet learned about! However, be cautious with utilizing complex non-parametric models, as these could lead to over-fit predictions that do not generalize will to the real world.

These 4 models should be implemented in 4 seperate scripts:

* `model1.ipynb`
* `model2.ipynb`
* `model3.ipynb`
*` model4.ipynb`

Feel free to name these jupyter notebooks appropriately (e.g. linear regression could be called `linreg.ipynb`).

### CDA Example

The following describes an example `CDA` workflow for 4 methods of predicting salaries based on job-training requirements.

* Remove outliers for salaries, log-normalize bootcamp duration, and utilize a linear regressor with backward selection
* Remove outliers for salaries, log-normalize bootcamp duration, and utilize the LASSO for automatic selection
* Remove outliers for salaries, keep bootcamp duration, and utilize the LASSO for automatic selection
* Remove outliers for salaries, keep bootcamp duration, and utilize a RandomForestRegressor with a max-depth of 3

By observing all selected features for these 4 models, we could potentially observe that bootcamp features predict for higher bootcamp salaries.

### Draft Findings

After completing your `EDA`, draft your observations in a succint document (at most 3 graphs!) that detail what information you've gleaned from your visual analysis. This document must answer describe the following aspects of the dataset.

Please ensure that this section is well-edited and concise. Think of this as a formal report that multiple individuals will utilize for business decisions. Do NOT include the place-holder text below.

> ## Distributions
> (place-holder text) What distributions did you notice throughout your dataset? Were any
> attributes normally distributed? If not, what methods can you take to force normality?
> 
> ## Metrics
> What interesting metrics did you glean from your dataset? Did any box-plots or confidence intervals
> seem significant? 
>
> ## Relationships
> Did 

### Further Develop Documentation

As always, ensure proper documentation. You must be able to understand the motivation for your code one year after this project completes.

### Ensure Branching

Going forward we will check commit history to ensure that each team member is contributing equally to the codebase, so be sure to work solely in a branch-based environment!

### Collect More Data (If Applicable) & Integrate

Remember! The more data the better. Always be on the lookout for ways collect relevant data to increase the statistical power of your observations.

### Tackle Recommended Next Actions

Lastly, if you are complete with all sprint specifications, a good chunk of next actions would be the recommnended code-quality changes as listed in your feedback.

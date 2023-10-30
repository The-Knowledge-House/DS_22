# sheets-lab

Reminder: when opening this file, hit "ctrl + shift + v" or "cmd + shift + v" to make it pretty.

## Objective
This lab aims to reinforce your skills in basic sheets operations. By the end of this exercise, you will practice:
1. Creating basic formulas
2. Creating visualizations
3. Creating Pivot Tables

You will be using the `hotel_100_2022.csv` file for this lab. This csv file represents a collection of the top 100 hotels from various parts of the world and their attributes.

This file should be loaded into your Google Drive for you to be able to complete this lab.

## Part 1 : Metrics

First, we will be calculating metrics on each row of this dataset, as well as as on the entire dataset. Follow along with the steps below to practice creating functions.

1. For each row in this dataset (excluding the header), calculate the difference between the `Past_Rank` column and the `Rank` column. Save this calculation in the immediate column after `Past_Rank`. Apply this calculation to every single row.
2. Below the table, you will calculate summary statistics. Feel free to create this calculation anywhere in the sheet below the table. The first calculation you will be creating is the `median` amount of rooms on the `Rooms` column.
3. Next, you will calculate the `average` amount of rooms on the `Rooms` column. 
4. Likewise calculate the `median` of the `Score` column in a brand new cell.
5. Likewise calculate the `average` of the `Score` column in a new cell.
6. And lastly, count the number of hotels that the "The Oberoi Group" owns based on the `Company` column and the [COUNTIF function](https://support.google.com/docs/answer/3093480?hl=en).

## Part 2 : Pivot Table

1. Next, create a pivot table that contains `Theme` as a row and `COUNT` of `Score` as the value. Here we simply want to see what is the most common type of hotel by theme.
2. Afterwards, you will create a new value which is the `AVERAGE` of `Rooms`, while still keeping the previous settings untouched.

By the end of this part, your pivot table shoulld look like the following below:

![pivot](/1.05/10_31/lab/images/pivotpng.png)

## Part 3 : Visualizations

Finally, you will create a pie chart that displays the count from your pivot table. Your visualization should look like the pie chart below:

![pie](/1.05/10_31/lab/images/pie_chart.png)

## Bonus :

With minimal guidance, create a 100% stacked area chart that shows the breakdown of theme and country. 

Note: You should create a pivot chart first before creating this visualization. 

Your chart should look like the visualization below:

![100](/1.05/10_31/lab/images/100.png)

## Submission

This exercise will **not** be submitted for grading.

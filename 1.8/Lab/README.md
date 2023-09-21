# Education Analysis

Data on the condition of American education has been collected [ever since the 1870s](https://nces.ed.gov/naal/lit_history.asp). Today we will utilize our Python skills to afford some insight into historical patterns of the US educational system.

Eventually, we will calculate the percent change of test-score outcomes on 4th or 8th graders utilizing this dataset called `states_all.csv`.

For this week of the lab we will begin prepping this data by loading and filtering it. See the steps listed below:

## Step 1

You will create a GitHub repository called `edu-analysis` & then clone this to your own computer. 

https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository 

https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository 

## Step 2

After cloning this repository, you will create the following files in your repository:

* .gitignore
* analysis.py
* README.md
* states_all.csv

All of these files, except for `states_all.csv`, will be *empty*.

## Step 3

Next you will begin setting up your files:

### .gitignore

Ensure that your .gitignore is set up so that we are ignoring the `states_all.csv` file!

### analysis.py

Create a file called `analysis.py` which will read in your csv data and save it to a list of dictionaries called `list_data`. Remeber to use your `open` function!

```python
list_data = []
with open("states_all.csv", "r") as infile:
    # load in data as DictReader
    reader = csv.DictReader(infile)
    for row in reader:
        list_data.append(row)
```

### README.md

Set up your `README` using the below template. Replace the text in square-brackets with your own text!

```
# edu-analysis

[a quick description of your intent & project goal]
```

## states_all.csv

We will leave this file unchanged.

## Step 4

After loading in and setting up your files, commit all your changes using our established git workflow:
```
git add *
git commit -m "Initial commit"
git push
```

## Step 5

After making your initial commit, you will begin accomplishing the following specifications for your `analysis.py` file. 

0. Print out how many rows your data contains. Keep in mind, you have a list of dictionaries. How can we get the `len()` of data?

1. Select one state to analyze. Once you have this state, filter out your `list_data` to only contain that state! Remember, you can use list comprehension to quickly implement this!

```python
state_data = [row for row in list_data if condition]
```

2. Decide which one of these columns you want to analyze. `AVG_MATH_4_SCORE`, `AVG_MATH_8_SCORE`, `AVG_READING_4_SCORE`, `AVG_READING_8_SCORE`. Take a look at the following link to find out more information on these columns: https://www.kaggle.com/datasets/noriuk/us-education-datasets-unification-project. 

3. Filter out your `state_data` to only contain dictionaries that contain values for your chosen column! Once again, you can utilize list comprehension.
 
4. Print out how many rows your data contains after your filtering.

5. Document your code.

6. (Optional Challenge) combine all the above logic into one function that takes in `state` and `column` strings:
```python
def filter(state, column):
```

Utilize your peers, notes, and the internet to help you accomplish these specifications.

Rememeber, organization counts! So be sure to have a "clean" code by the time you push your final commit (no print functions, no erroneous code.)

## Step 6

Add + push as you develop your code!
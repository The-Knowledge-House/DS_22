# actions-lab

Reminder: when opening this file, hit "ctrl + shift + v" or "cmd + shift + v" to make it pretty.

## Objective
This lab aims to reinforce your skills in basic GitHub actions. By the end of this exercise, you will be able to: 
1. Create your own GitHub Actions
2. Run automated GitHub actions on your second TLAB

## Part 1: Code Along

Before beginning, be sure to create a GitHub repository for your `bank-activity` lab. You will not be able to complete this lab without creating this GitHub project.

To ensure that the `validate.yaml` GitHub action works correctly, we first have to modify our `code/test/validate.py` script to include the `os` package, which we will use to recreate our path.

In the import section of this script, add the line of code `import os` so that the top of your module looks like this:

```python
import sys
import os
```

Afterwards, add the line of code `file_path = os.path.join("data", "raw", "amzn.csv")` above our object instatiation. This goes back to the concept of filepath differences b/w Mac/Linux & Windows. 

Once you've complete this, your object instantiation code will look like the following.

```python
# Create a Metrics object
file_path = os.path.join("data", "raw", "amzn.csv")
metrics = StockMetrics(file_path)
```

## Part 2: Set up GitHub Action

To complete this part of the project, you will access the cloned `bank-activity` repository that you've just interacted with, and you will follow the steps below.

1. Create a folder called `.github` in your repository. **NOTE**: You must have the dot in front of this folder name.
2. Within this folder, create a folder called `workflows`.
3. Next, you will create a file called `validate.yaml`. Leave this empty for the time being.
4. After creating this file, you will copy over the contents from `lab/copyme.yaml` into `validate.yaml`.
5. Lastly, you will `git add .github`, `git commit -m "..."` and `git push`. If you see a check-mark appearing in your GitHub project, you are good to go!

## Submission

This exercise will **not** be submitted for grading.
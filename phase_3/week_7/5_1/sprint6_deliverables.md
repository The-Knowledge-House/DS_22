## Sprint 6 Deliverables

### Implement Extract & Transform

After completing the setup of your Amazon rds databases from Sprint 5, you will then implement code to extract data from your csv files (multiple hopefully), perform transformations such as cleaning, and then load your csv file into your database.

This will be completed via 2 seperate scripts:

* `transform_data.ipynb`
* `send_data.py`

Each file should encapsulate it's own logic. For example, `transform_data.ipynb` should only be extracting your data from csv files, per ions, and then should save these `csv` files back into your `data` folder. Your `send_data.py` file should be loading this cleaned data in-bulk to your setup databases. Check out `bulk_example.py` to see an example.

Your `transform_data.ipynb` file should be an expansion on the code that you implemented during the `mvp` phase. If you do not have any additional transformations to make, you can simply use the code you implemented during the `mvp` phase. But remember, your analysis is only as exhaustive as your transformation code.  

### Further Develop Documentation

As you implement your code & plan out your database, you should also succinctly describe these additional features in your respective `README`. In addition, you should ensure that your code is properly documented as you push your changes.

### Continue Branching

If you haven't started doing so already, each team member should be working on their own branch and then integrating these changes up to the main branch. We will be checking commit history to ensure that each team member is pushing purposeful code.

### Collect More Data (If Applicable) & Integrate

Lastly, you should aim to collect at least one more csv file to throw in the mix of your analysis. After all, our statistical power only increases with the sample size.

This additional csv file should be appropriately cleaned and transformed to fall in line with the rest of your data that you've gathered so far. 

If you've hit a "ceiling" as to the amount of data that can be collected (on the account of not having the appropriate resources, or just not being able to find more data), feel free to skip this step.

### Tackle Recommended Next Actions

And lastly, you've all been given recommended changes after your first presentations. Please ensure that all these recommended next actions have been implemented.

All of these changes should be reflected on your GitHub repository. 

You will be submitting a link to your GitHub profile as part of your Sprint 5 deliverables. This will be due on Wednesday `5/2`.
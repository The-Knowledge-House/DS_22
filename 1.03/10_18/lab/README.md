# csv-lab

Reminder: when opening this file, hit "ctrl + shift + v" or "cmd + shift + v" to make it pretty.

## Objective
This lab aims to reinforce your skills in OOP and working with CSV files. By the end of this exercise, you will be able to: 
1. Implement basic objects
2. Implement methods
3. Read data from CSV files

## Prerequisites
* VSCode. If you have not installed VSCode yet, click [here](https://code.visualstudio.com/download) and select your operating system (OS).
* Understand basic Python assignment
* Understand conditionals & for-loops

## Part 1 : StockData.py

Utilize the [csv](https://docs.python.org/3/library/csv.html) documentation to assist you in this project. Specifically, note the example code provided for you. Aim to recreate the example code. 

Access the file labeled `StockData.py`:
1. In the `read_csv` method, replace the `None` to correctly read the CSV file using the `csv.reader` function.
2. Skip the header of the CSV file. (You might have to do some googling for this).
3. In the `calculate_lengths` method, count the number of valid (non-empty) entries in each row and update the `length` variable.

## Part 2

Still in the `StockData.py` file:
1. Instantiate the StockData class with the filename `data/amzn.csv`.
2. Call the `read_csv` method on the instantiated object.
3. Print the `data` attribute of the object to see the loaded CSV data.
4. Call the `calculate_lengths` method on the instantiated object and print the resulting list of lengths.

## Bonus

For those who want an additional challenge:

1. In the `StockMax.py` file, you will find a class named `StockMax` that inherits from the `StockData` class.
2. Implement the `find_max_value` method to extract the maximum value from each row (excluding the 'Date' column and missing values) and return these maximums as a list.
3. Test the new methods by creating an instance of `StockMax`, reading the CSV, converting the data to floats, and then extracting the maximum values.

## Submission

This exercise will **not** be submitted for grading.

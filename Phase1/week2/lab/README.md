![Step on no pets](https://www.rd.com/wp-content/uploads/2021/03/palindromes-13-scaled.jpg)

# Lab: Palindromes

For this lab you will create a program that detects whether an integer or a decimal is palindrome. 

```
python palnumber.py 10001
True

python palnumber.py 123
False

python palnumber.py 1.0001
True

python palnumber.py 1.0002
False
```

## Background

Number [palindromes](https://en.wikipedia.org/wiki/Palindrome) work exactly like word palindromes. Reading them forward (left-to-right) gives the same exact number as reading it backwards (right-to-left). A couple of examples are listed below.

```
121
1221
1234321
```

For this lab, we will also expand the definition of a palindrome to include floating point numbers! The following are positive examples of float palindromes:

```
1.001
123.321
12.3321
```

Notice how our algorithm does not care about decimal places.

## Exploration

### What to do with that decimal?



### What makes a palindrome?



### 

## Specifications

* 
* 
* 

In the following lab, you will be utilizing your knowledge of conditionals, data-types, loops, & **type-casting** in order to check if a number is in fact a palindrome. 

I encourage you all to *iteratively* develop your code and continuously test! That is, write a bit of code, test out your code, & repeat until you've acheived a 100%! 

## Problem Set

### Part 1: Integer Palindromes



### Part 2: Floating Point Palindromes



### Challenge: Prime Palindromes



## Setting up the lab

To set up your lab, you must first create a GitHub repository in your profile named `Palindromes`. This is where all of your work will be *committed*. 

Once you've created this repository, go ahead download the *zip* file located in this folder and extract. This is how we will get all our starter-files and test-files.

## Testing

To test out your solutions, run the following in your terminal:
```
cd Phase1/week2/lab
python -m unittest test_palnumber.py
```

Feel free to explore this testing code! While you shouldn't necessarily understand each line of code, you should see the underpinnings of *test-driven* development.

If you'd like to test out the additional challenge, run
```
cd Phase1/week2/lab
python -m unittest test_challenge.py
```

## Submission

To submit, simply provide a link to your GitHub link containing completed code. Be sure to include comments, and ensure that your code passes all tests!

The following files should be modified for this lab:
* palnumber.py
* primepalnumber.py (optional)
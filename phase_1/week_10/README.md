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

<br/>

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

<br/>

Notice how our algorithm does not care about decimal places.

## Problem Set

### Part 1: Integer Palindromes

Create an algorithm within the `main()` function of the `palnumber.py` file to check if an integer is a palindrome. Notice that we take in user input automatically via `sys.argv[1]`.

Once you've completed this code, you can try out your code by running `python palnumber.py 10001`, which should print out `True`.

### Part 2: Floating Point Palindromes

Improve upon your `main()` function of the `palnumber.py` to now also take in "floating point numbers" aka "floats." Keep in mind that we can ignore the decimal when checking for palindromic numbers.

Once you've completed this code, you can try out your code by running `python palnumber.py 10.001`, which should print out `True`.

### Challenge: Prime Palindromes

If you've completed both features above, feel free to try out the *prime palindromes* challenge. Once again you'll be checking if an integer is a palindrome, but this time with a twist: you will also be checking if the number is a prime number! 

There are a variety of methods to finding out if a problem is prime. I encourage you all to explore the [FAQ Section](#FAQ) in order to explore these different paths to success.

Once you've completed this code, you can try out your code by running `python palnumber.py 757`, which should print out `True`.

<br/>

## FAQ

### How do you check for a palindrome?

Defining a problem is only half the battle in programming. 

### I've completed Part 1, how can I use this for floats in Part 2?

Once you've completed Part 1, 

### What to do with that decimal?



### (Challenge) What makes a prime?

This question is a fundemental component of the study of computers, and specifically cryptography. While there are a few clever methods out there to check if a number is indeed prime, there are easier routes we can take.

Let's consider the following prime numbers

<br/>

## Specifications

* Program always only prints `true` or `false` once.
* Program will take in an integer or a floating point number.
* 

In the following lab, you will be utilizing your knowledge of conditionals, data-types, loops, & **type-casting** in order to check if a number is in fact a palindrome. 

I encourage you all to *iteratively* develop your code and continuously test! That is, write a bit of code, test out your code, & repeat until you've acheived a 100%! 

<br/>

## Setting up the lab

To set up your lab, you must first create a GitHub repository in your profile named `Palindromes`. This is where all of your work will be *committed*. 

Once you've created this repository, go ahead download the *zip* file located in this folder and extract. This is how we will get all our starter-files and test-files.

<br/>

## Testing

To score your solution, run the following in your terminal:
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

<br/>

## Submission

To submit, simply provide a link to your GitHub link containing completed code. Be sure to include comments, and ensure that your code passes all tests!

Only the following files should be modified for this lab:
* palnumber.py
* primepalnumber.py (optional)
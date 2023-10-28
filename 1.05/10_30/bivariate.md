## Bivariate Calculatons


### Part 1

We will be doing two bivariate calculations. One by hand together and one using Python.

In this first step, we will calculate by hand.

| Test Score (out of 10) | Hours Playing Video Games |
|------------------------|---------------------------|
| 8                      |2                          |
| 3                      |2                          |
| 5                      |1.5                        |     
| 7                      |1                          |
| 1                      |2.5                        |
| 2                      |3                          |
| 6                      |1.5                        |
| 7                      |2                          |
| 4                      |2                          |
| 9                      |1.5                        |


As a reminder, here are the steps (refer to PowerPoint for graphics):

1. Calculate the x mean (x_bar) and y mean (y_bar)
2. subtract each value of x by the mean of x (x_i - x_bar) deviance of x
3. subtract each value of y by the mean of y (y_i - y_bar) deviance of y
4. multiply each value of (2) and (3) together for each x, y pair (x_i - x_bar) * (y_i - y_bar)
5. add all the values of (4) together
6. square the values of (2) squared deviance of x
7. square the values of (3) squared deviance of y
8. multiply (6)and (7) for each x,y pair (similar to step 4)
9. Add the values of (8) all together
10. Take the sqrt of (9)
11. Divide (5) by (10)

### Part 2 Python Calculation

Open the `bivar.ipynb` file and follow the instructions in the notebook as you do the same calculations but using Python!

We will first do a step-by-step method and then use pandas to help us out with the same steps but in a more efficient manner.


library(mltools)
library(rpart)
library(rpart.plot)
library(caret)

# R : a programming language (built in C) that specializes in statistical inference

# load data
df <- read.csv("C:/Users/saidmf/Desktop/TKH/DS_22/phase_3/week_7/data/bank-cleaned.csv")

# split amongst training & test
samp1 <- createDataPartition(df$y, p = 0.8, list = FALSE)

train <- df[samp1, ]
test <- df[-samp1, ]

# logistic regression
log <- glm(y ~ ., data = train, family = "binomial")
summary(log)
"Deviance Residuals:
    Min       1Q   Median       3Q      Max
-2.1419  -0.5083  -0.3879  -0.2604   3.7814

Coefficients: (8 not defined because of singularities)
                      Estimate Std. Error z value Pr(>|z|)
(Intercept)         -3.448e+00  2.948e-01 -11.697  < 2e-16 ***
age                  4.804e-05  2.179e-03   0.022  0.98241
balance              7.539e-05  9.203e-06   8.192 2.58e-16 ***
campaign            -1.146e-01  9.780e-03 -11.721  < 2e-16 ***
pdays                3.625e-04  3.062e-04   1.184  0.23645
previous             9.966e-03  6.334e-03   1.573  0.11563
job_admin.           1.230e-01  2.249e-01   0.547  0.58439
job_blue.collar     -1.104e-01  2.239e-01  -0.493  0.62189    
job_entrepreneur    -1.826e-01  2.456e-01  -0.744  0.45717
job_housemaid       -2.189e-01  2.485e-01  -0.881  0.37826
job_management      -1.325e-04  2.230e-01  -0.001  0.99953
job_retired          5.474e-01  2.292e-01   2.389  0.01692 *
job_self.employed   -1.004e-01  2.388e-01  -0.420  0.67429    
job_services        -3.425e-02  2.284e-01  -0.150  0.88078
job_student          6.215e-01  2.364e-01   2.629  0.00858 **
job_technician      -6.992e-02  2.232e-01  -0.313  0.75407
job_unemployed       1.521e-01  2.377e-01   0.640  0.52239    
job_unknown                 NA         NA      NA       NA
marital_divorced    -1.362e-01  6.554e-02  -2.077  0.03777 *
marital_married     -3.060e-01  4.494e-02  -6.811 9.73e-12 ***
marital_single              NA         NA      NA       NA
education_primary   -1.820e-01  1.030e-01  -1.767  0.07723 .  
education_secondary -6.921e-02  9.141e-02  -0.757  0.44894
education_tertiary   1.559e-01  9.590e-02   1.626  0.10405
education_unknown           NA         NA      NA       NA
default_no           1.206e-01  1.594e-01   0.756  0.44939
default_yes                 NA         NA      NA       NA    
housing_no           5.761e-01  3.930e-02  14.659  < 2e-16 ***
housing_yes                 NA         NA      NA       NA
loan_no              4.812e-01  5.868e-02   8.201 2.39e-16 ***
loan_yes                    NA         NA      NA       NA
contact_cellular     9.476e-01  5.604e-02  16.910  < 2e-16 ***
contact_telephone    7.610e-01  8.658e-02   8.789  < 2e-16 ***
contact_unknown             NA         NA      NA       NA
poutcome_failure     3.047e-03  9.147e-02   0.033  0.97343
poutcome_other       3.297e-01  1.048e-01   3.145  0.00166 **
poutcome_success     2.267e+00  8.703e-02  26.048  < 2e-16 ***
poutcome_unknown            NA         NA      NA       NA
---
Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

(Dispersion parameter for binomial family taken to be 1)

    Null deviance: 25705  on 35572  degrees of freedom
Residual deviance: 22084  on 35543  degrees of freedom
AIC: 22144

Number of Fisher Scoring iterations: 6
"

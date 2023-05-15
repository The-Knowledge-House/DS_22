# same as import xyz
library(fitdistrplus)
library(logspline)
library(moments)

# small tutorial in R: https://machinelearningmastery.com/r-crash-course-for-developers/

# same as pd.read_csv
df <- read.csv("phase_3/week_9/data/winequality-red.csv")

# commenting in R is the same as Python

# same as print(df["density"])
print(df$density)

# get kurtosis
print(kurtosis(df$density))

# view dharacteristics of density via a Cullen & Fey Graph
# https://stats.stackexchange.com/questions/404633/understanding-the-cullen-and-frey-plot
descdist(df$density, discrete = FALSE)

# this distribution appears to model something called "logsistic distribution"
# https://www.sciencedirect.com/topics/mathematics/logistic-distribution
# https://www.statisticshowto.com/logistic-distribution/

# Download: https://posit.co/download/rstudio-desktop/
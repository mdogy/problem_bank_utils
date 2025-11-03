
1. The advantages of python for data science do **not** include that it is

    a) flexible as a general programming language
    b) easy to learn (relative to other languages)
    *c) one of the fastest executing programming languages
    d) extensive support for data science through libraries

2. For which operation might an array (like a numpy array) **not** be ideally suited if you need to do this operation many times and quickly?

    *a) appending elements to the end
    b) randomly reading elements by index
    c) reading from the data structure in an order
    d) changing an an arbitrary element by its index

3. If "labels" is a python list of labels, and you want to remove duplicates you can 

    a) Store them in a Python Tuple
    *b) Store them in a python Set
    c) Use the built-in "uniq" function
    d) Call list.remove_dups()


4. Which is **not** true of a Data a NumPy array x

    a) A NumPy array can hold characters
    b) If x is a NumPy array, x[0] can be a NumPy array
    c) A NumPy array is mutable 
    *d) x[0] can be a boolean and x[1] can be in integer

5. If the variable "sampleArray" is a numpy array with rows and columns so that len(sampleArray.shape)==2. What is len(sampleArray) equal to?

    *a) sampleArr.shape[0]
    b) sampleArr.shape[1]
    c) sampleArr.shape[0]*sampleArr.shape[1] (total number of elements)
    d) sampleArr.size()

6. The most crucial first step after data cleaning in a data project is

    a) Performing regressions along every variable pair.
    b) Splitting the data into test and training sets.
    *c) Exploratory Data Analysis
    d) Normalizing the data by subtracting the mean 

7. If "df" is a dataframe, what does df.describe() do?

    a) It returns a dataframe with the statistics for every column
    b) It returns a dataframe with the statistics for every row
    *c) It returns a dataframe with the statistics for every column with numerical data type
    d) It returns the type information for each column and the number of missing values

8. Which problem would **not** be considered part of data cleaning

    a) standardizing inconsistently labeled data
    *b) computing the summary statistics of a dataset
    c) filling in missing values in some columns
    d) dropping rows having invalid data due to measurement error (eg. negative mass)

9. Which is **not** true of a data frame .info() function in pandas?

    *a) info only shows numerical data 
    b) info does not show mean
    c) info shows the number of non-null values
    d) info shows the information on columns containing strings

10. How would you get the second through the fourth row (inclusive) of a data frame df?

    a) df.loc[3:5]
    b) df.head(1)
    c) df[[2:4]]
    *d) df.iloc[1:4]


11. In standard hypothesis testing, what does it mean when a result is statistically significant?

    a) When the correlation is 1.
    b) When the probability is within 95% of the null hypothesis.
    c) When the result has not been observed before.
    *d) When the probability of the result is outside 95% of the null hypothesis

12. Assuming df = pandas.DataFrame({'ind':[1,2,3], 'letter':['c','d','e']}), what is type(df['letter'])?

    a) DataFrame
    b) ndarray
    *c) Series
    d) list


13. Which statistical method involves sampling your original data at random where you are allowed to draw the same data point multiple times

    a) direct simulation
    b) shuffling
    *c) bootstrap
    d) jackknife

14. Which kind of graph would you **not** use to show number of scoops of ice cream sold in a month (y) by flavor (x)? 

    a) Scatter plot
    *b) Line plot
    c) Bar chart
    d) Histogram

15. Which visualization is better for exploring the distribution of a single numerical variable?

    a) Scatter Plot
    *b) Histogram
    c) A pie chart
    d) Line chart

16. Suppose we had 100 people. Each person had three meals a day and we asked them to tell us whether they had 0, 1, 2, 3 or 4 cups of water since they woke up (if it was breakfast), or since the prior meal. We plotted this as a simple scatter plot (default matplotlib settings) with the x axis being 1, 2, or 3 representing the meal and the y axis being 0, 1, 2, 3, or 4 representing how many cups of water. Each person is represented as a point. What problem would we certainly be seeing?

    a) the data could not be correleated
    *b) due to overplotting almost nothing would be visible
    c) the x axis would have to start at 0
    d) a lack of data to plot

17. Suppose we had 100 people. Each person had three meals a day and we asked them to tell us whether they had 0, 1, 2, 3 or 4 cups of water since they woke up (if it was breakfast), or since the prior meal. We plotted this as a simple scatter plot (default matplotlib settings) with the x axis being 1, 2, or 3 representing the meal and the y axis being 0, 1, 2, 3, or 4 representing how many cups of water. Each person is represented as a point. What problem would we certainly be seeing?

    a) the data could not be correleated
    *b) due to overplotting almost nothing would be visible
    c) the x axis would have to start at 0
    d) a lack of data to plot


18. In scraping web pages it is most common to obtain the HTML via the request library and then parse it with the library

    a) scrapy
    b) regexp 
    *c) Beautifulsoup
    d) parsely

19. What is a difference between *Exploratory* Data Analysis and *Explanatory* Data Visualization?

    a) Exploratory is only statistical analysis, Explanatory is only visual analysis
    *b) Exploratory is to understand data, Explanatory presents the outcome
    c) Explanatory Visualization is the prerequisite for EDA
    d) They are two terms are interchangeable

20. Lag plots are typically used to

    a) Show relationships between different variables in time-independent data
    b) The lag effect of a change between a switch from the control group to treatment group
    c) periodic noise in an image
    *d) relationship between values at a fixed separation within a time series


21. Times series analysis is least able to

    a) predict values of a trend
    b) identify seasonality
    *c) predict black swans
    d) detect outliers

22. A common way to detect seasonality or periodic behavior in time series is to use

    *a) plots on a sin/cos basis (spectral)
    b) the correlation coefficient
    c) a violin plot
    d) a moving average

23. Suppose we are analyzing ER admissions over time during a pandemic and we are trying to separate the typical patients from accidents, heart attacks, strokes, and violence from patients suffering from infectious disease. We would likely consider a time series

    a) multiplicative decomposition
    *b) additive decomposition
    c) moving average
    d) PCA

24. When building models on time series (as opposed to other data) an extra consideration is 

    a) that the validation/testing occurs on different data than was used to fit the model
    b) that the validation/testing occurs on data with earlier timestamps than was used to fit the model
    *c) that the validation/testing occurs on data with later timestamps than was used to fit the model
    d) that sequential data is not used in fitting to avoid overfitting

25. Data storytelling is most important when

    *a) presenting the results of the analysis
    b) brainstorming during exploratory data analysis
    c) identifying outliers
    d) interpreting a model

26. Which of the following is **not** type of filtering?

    a) Gaussian blur
    *b) rescaling brightness values
    c) convolving with an edge kernel
    d) taking the median in a sliding window



27. Determining the derivative of an image (the change lets say the y direction) in the presence of some noise is most easily done with
    
    a) a curve that remaps gray values to a new range
    b) a histogram
    c) a median filter
    *d) convolution with the y-derivative of a gaussian kernel

28. Some times a camera may fail to acquire a useful image and produce a mostly black (no light), or all white (sun is shining in the lense), close to constant color. Which of the following could most useful to detect this kind of thing:

    a) a Gaussian kernel
    b) segmenting the image into regions
    *c) the histograms of each channel
    d) object detector

29. Then the Principal components derived from the data using PCA are sorted from largest eigenvalue to smallest, the last components are generally **not**

    a) the components with the least variance
    b) random noise
    c) perpendicular (orthogonal) to the components with the greatest variance
    *d) the components with the largest variance

30. Which would be the best use dimension reduction 

    a) to predict the temperature from historic temperatures
    *b) in order to make a 2D scatter plot of data with 10,000 columns (attributes) and 1000 observations
    c) in order to make a 2D scatter plot of temperature and pressure with 10,000 rows (observations)
    d) to identify output variables that are critical for classification

31. When we fit a line using linear regression we are trying to optimize

    a) the number of points a line passes through
    *b) sum of the square of the difference of the y value of the data points and the y value of the proposed line at each x value of the data points
    c) sum of the square of the distance between the each data point and the closest point proposed line (perpendicular to the line)
    d) The probability of an error

32. Which component(s) of data storytelling is(are) particularly critical (but often overlooked)?

    a) Providing a comprehensive view of the data
    b) Proper modulation of your voice
    *c) evoking emotion and providing story (plot) structure
    d) the quality of the data visualizations

33. Stop words are important concepts when processing text they are

    a) words that tend to end sentences
    b) words with control characters that often break learning algorithms
    c) useful places to break longer sentences into parts
    *d) common words that usually don't indicate the topic

34. If we want to break a document up into a list of words we use a

    *a) tokenizer
    b) lexicon
    c) splitter
    d) corpora

35. To blur an image we can

    a) multiply the image by 0.24
    b) replace each value with a random number
    *c) convolve using a constant function in a sliding window
    d) take the square root of each value


36. Why must random numbers be seeded?

    a) otherwise they become less random and clump
    b) it speeds up the generation of such numbers
    c) it allows you to use different distributions (like the normal distribution)
    *d) it allows you to reproduce a result exactly

37. Both a stack and a queue are most naturally implemented using

    *a) a linked list
    b) a key value data structure
    c) a fixed size array
    d) a python Set

38. Which of the following is likely the best strategy (preserving the structure of the data) when you have a large number of rows and a small number of missing values spread across different columns? 

    *a) drop the rows with missing values
    b) drop the columns with missing values
    c) fill in the missing values with the row mean
    d) fill in the missing values with zero


39. One-hot encoding of n-labels represents each label, tag or string by a

    a) unique random number between 0 and 1
    *b) a vector with n-1 zeros and a single 1
    c) integers between 0 and n-1
    d) the eigenvalue of the label

40. When we can represent a 2-D array of numbers as an image, where each row, column value is represented as pixel and, for example, larger numbers are redder and smaller numbers are darker. This is kind of representation is called a

    a) histogram
    b) scatter plot
    c) line plot
    *d) heat map 

41. In the case of linear regression, solving Xa = y for a, we can use a linear algebra solution based on a "linear algebra" solution a=(X^TX)^{-1}X^Ty and another more general but iterative solution based on

    *a) gradient descent
    b) the normal distribution
    c) dynamic programming
    d) tree search

42. In text pre-processing we often remove stopwords. stopwords are

    a) words that tend to end sentences
    b) words with control characters that often break learning algorithms
    c) useful places to break longer sentences into parts
    *d) common words that usually don't indicate the document topic

43. In order to visualize the potential dependency between one variable and another we are most likely to use a

    a) violin plot
    *b) scatter plot
    c) a bar graph
    d) a line plot

44. Suppose we have a statistic from two groups, group A and group B and we want to know if the difference between the two groups is statistically significant. We do not know any thing about the distributions of these two groups and cannot thus use a direct simulation. We would most likely use

    *a) the permutation test
    b) a linear regression
    c) a matrix of scatter plots
    d) the covariance

45. Sam is a data scientist. Sam has a moderate amount of data (rows in the 10s of thousands). Sam is trying to do a regression problem with multiple numerical variables (lets say linear regression). The 5 variables are known to be correlated with the target variable, y. Sam has the opportunity to get 100 more variables which may or may not be correlated with y. Sam reasons more data is always better. Sam is wrong. If so why?

    a) Sam is not wrong, more data is always better
    b) Sam is wrong because the new variables will be correlated with the old variables
    c) Sam is wrong 100 variables will cause numerical overflow
    *d) Sam is wrong because more data may create sperious correlations (curse of dimensinality)

46. If we perform polynomial regression (one variable). Given a set of data, we can fit the training data better and better by increasing the degree of the polynomial. However, this is not a good idea. Why?

    a) the computation explodes with the degree
    b) high degree polynomials result in underfit of the training data (generalizing to test data poorly)
    *c) high degree polynomials result in overfit of the training data (generalizing to test data poorly)
    d) the fit only takes into account the y values and not the x values. When both are used high degrees have poorer fit.

47. The pandas library is most useful for

    a) text data such as a novel
    b) image data
    c) data cubes (like 3D volumetric MRI data)
    *d) structured data (tablular form)

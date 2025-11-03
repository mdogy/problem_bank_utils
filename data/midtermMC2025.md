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


5. If "df" is a dataframe, what does df.describe() do?

    a) It returns a dataframe with the statistics for every column
    b) It returns a dataframe with the statistics for every row
    *c) It returns a dataframe with the statistics for every column with numerical data type
    d) It returns the type information for each column and the number of missing values


6. Which is **not** true of a data frame .info() function in pandas?

    *a) info only shows numerical data 
    b) info does not show mean
    c) info shows the number of non-null values
    d) info shows the information on columns containing strings



7.  In standard hypothesis testing, what does it mean when a result is statistically significant?

    a) When the correlation is 1.
    b) When the probability is within 95% of the null hypothesis.
    c) When the result has not been observed before.
    *d) When the probability of the result is outside 95% of the null hypothesis

8.  Assuming df = pandas.DataFrame({'ind':[1,2,3], 'letter':['c','d','e']}), what is type(df['letter'])?

    a) DataFrame
    b) ndarray
    *c) Series
    d) list


9.  Which visualization is better for exploring the distribution of a single numerical variable?

    a) Scatter Plot
    *b) Histogram
    c) A pie chart
    d) Line chart

10. In scraping web pages it is most common to obtain the HTML via the request library and then parse it with the library

    a) scrapy
    b) regexp 
    *c) Beautifulsoup
    d) parsely

11. What is a difference between *Exploratory* Data Analysis and *Explanatory* Data Visualization?

    a) Exploratory is only statistical analysis, Explanatory is only visual analysis
    *b) Exploratory is to understand data, Explanatory presents the outcome
    c) Explanatory Visualization is the prerequisite for EDA
    d) They are two terms are interchangeable

12. Lag plots are typically used to

    a) Show relationships between different variables in time-independent data
    b) The lag effect of a change between a switch from the control group to treatment group
    c) periodic noise in an image
    *d) relationship between values at a fixed separation within a time series


13. When building models on time series (as opposed to other data) an extra consideration is 

    a) that the validation/testing occurs on different data than was used to fit the model
    b) that the validation/testing occurs on data with earlier timestamps than was used to fit the model
    *c) that the validation/testing occurs on data with later timestamps than was used to fit the model
    d) that sequential data is not used in fitting to avoid overfitting

14. Data storytelling is most important when

    *a) presenting the results of the analysis
    b) brainstorming during exploratory data analysis
    c) identifying outliers
    d) interpreting a model

15. When we fit a line using linear regression we are trying to optimize

    a) the number of points a line passes through
    *b) sum of the square of the difference of the y value of the data points and the y value of the proposed line at each x value of the data points
    c) sum of the square of the distance between the each data point and the closest point proposed line (perpendicular to the line)
    d) The probability of an error

16. Which component(s) of data storytelling is(are) particularly critical (but often overlooked)?

    a) Providing a comprehensive view of the data
    b) Proper modulation of your voice
    *c) evoking emotion and providing story (plot) structure
    d) the quality of the data visualizations

17. Why must random numbers be seeded?

    a) otherwise they become less random and clump
    b) it speeds up the generation of such numbers
    c) it allows you to use different distributions (like the normal distribution)
    *d) it allows you to reproduce a result exactly


18. Which of the following is likely the best strategy (preserving the structure of the data) when you have a large number of rows and a small number of missing values spread across different columns? 

    *a) drop the rows with missing values
    b) drop the columns with missing values
    c) fill in the missing values with the row mean
    d) fill in the missing values with zero



19. In order to visualize the potential dependency between one variable and another we are most likely to use a

    a) violin plot
    *b) scatter plot
    c) a bar graph
    d) a line plot

20. Suppose we have a statistic from two groups, group A and group B and we want to know if the difference between the two groups is statistically significant. We do not know any thing about the distributions of these two groups and cannot thus use a direct simulation. We would most likely use

    *a) the permutation test
    b) a linear regression
    c) a matrix of scatter plots
    d) the covariance

21. If we perform polynomial regression (one variable). Given a set of data, we can fit the training data better and better by increasing the degree of the polynomial. However, this is not a good idea. Why?

    a) the computation explodes with the degree
    b) high degree polynomials result in underfit of the training data (generalizing to test data poorly)
    *c) high degree polynomials result in overfit of the training data (generalizing to test data poorly)
    d) the fit only takes into account the y values and not the x values. When both are used high degrees have poorer fit.


22. What role does visualization play in Data Science?

    *a) Helps humans understand patterns that exist in large datasets
    b) It eliminates the need for data cleaning
    c) It guarantees conclusions are correct
    d) It replaces statistics entirely
    e) It is only useful for small datasets

23. What does statistics help prevent in analysis?

    *a) False conclusions caused by random patterns
    b) Collecting too much data
    c) Good visualizations
    d) The need for computers
    e) Faster machine learning training


24. In NumPy, what is “broadcasting”?

    *a) Automatically expanding arrays to compatible shapes during arithmetic
    b) Sending arrays to a TV channel
    c) Only used when adding identical shapes
    d) A memory compression method
    e) Copying data into SQL databases

25. Which is a key drawback of hash tables?

    a) They require keys to be sorted
    b) They cannot delete items
    *c) They do not preserve meaningful order
    d) Searching is always slower than a linked list
    e) They can only store fixed-size elements

26. In NumPy, why does adding a 1×3 vector to a 3×3 matrix work?

    *a) The vector is broadcast across rows to match shape
    b) The matrix is flattened automatically
    c) NumPy guesses the user’s intention
    d) The vector overwrites the diagonal
    e) Because 3 is a special broadcast-safe number

27. Which part of the data science workflow primarily focuses on understanding the structure, patterns, and anomalies present in the data?

    a) Data Collection
    *b) Exploratory Data Analysis (EDA)
    c) Confirmatory Data Analysis
    d) Feature Deployment
    e) GPU Optimization


28.  In matplotlib, why is using `fig, ax = plt.subplots()` preferred over calling `plt.plot()` directly?

    a) It uses more memory so it's faster
    *b) It gives explicit references to figure and axes objects for better control
    c) It enables automatic machine learning integration
    d) It prevents adding labels and legends
    e) It is required by NumPy


29.  The lecture suggests that before trusting an outlier, you should:

    a) Remove all outliers automatically
    *b) Trace back to the original data and verify context
    c) Replace with the mean
    d) Convert to categorical encoding
    e) Report it as a major scientific discovery


30.  A matrix of scatter plots helps you:

    *a) Visualize pairwise relationships among many quantitative variables
    b) Render 3D surfaces of a function
    c) Encode hierarchical trees
    d) Compute p-values for regression
    e) Normalize geospatial coordinates


31. In a standard ML workflow, a hold‑out test set is primarily used to…

    a) Select the best model during tuning
    b) Fit the feature scaler and imputer
    *c) Estimate the final generalization performance after all modeling choices are frozen
    d) Balance class labels in the training data
    e) Visualize learning curves

32. Which practice best prevents **data leakage** when scaling features?

    *a) Fit the scaler only on the training data, then apply the fitted transform to validation/test
    b) Use MinMax scaling instead of standardization
    c) Use more features so leakage averages out
    d) Shuffle the rows before scaling
    e) Fit the scaler on all available data, then transform splits


33. In simple linear regression, the **least squares** estimator chooses coefficients that…

    a) Equalize residuals across x
    b) Minimize mean absolute error of residuals
    c) Maximize R² directly
    d) Minimize classification error
    *e) Minimize the sum of squared residuals


34. In supervised classification, what is the primary goal when some rows have known labels?

    a) To delete rows without labels so training is cleaner
    b) To reduce dimensionality for visualization only
    c) To generate synthetic labels for all rows from noise
    *d) To label previously unlabeled rows using a learned model
    e) To cluster the data into groups without labels

35. Which example task is most clearly a multi-class classification problem?

    a) Predicting house prices in dollars
    b) Grouping unlabeled news articles by topic
    c) Estimating the mean of a Gaussian distribution
    d) Finding a low-dimensional embedding of images
    *e) Assigning each handwritten digit image a class from 0–9

36. For k-Nearest Neighbors (kNN), increasing k typically has what effect on the decision boundary?

    a) Has no effect on the boundary; only runtime changes
    b) Converts the classifier into a linear separator
    *c) Smooths the boundary by averaging over more neighbors
    d) Forces the classifier to overfit training data
    e) Makes the boundary more jagged and sensitive to noise


37. Linear Discriminant Analysis (LDA) can be viewed as finding:

    a) A nonlinear kernel mapping to infinite dimensions
    b) A decision tree that partitions space by axis-aligned cuts
    c) A clustering of unlabeled data by k-means
    d) A random forest that averages many trees
    *e) A projection that maximizes between-class separation relative to within-class scatter

38. Why is Naïve Bayes called 'naïve'?

    *a) It assumes features are independent given the class
    b) It assumes k is chosen by cross-validation
    c) It assumes infinite training data
    d) It assumes a linear decision boundary
    e) It assumes labels are uniformly distributed

39. Logistic regression models the log-odds (logit) as:

    a) A sum of kernel functions over support vectors
    *b) A linear function of input features (wᵀx)
    c) A decision tree depth
    d) A constant independent of input features
    e) The reciprocal of a Gaussian density


40. Which of the following statements about the Central Limit Theorem is FALSE?

    a) It applies to the distribution of sample means
    *b) It requires that the population distribution be normal
    c) It becomes more accurate as sample size increases
    d) It implies that the sampling distribution approaches a normal distribution

41. Which of the following statements about hypothesis testing is TRUE?

    a) A small p‑value proves that the null hypothesis is false
    b) Failing to reject the null hypothesis means it is true
    *c) A p‑value is the probability, under the null hypothesis, of obtaining a result as extreme as the one observed
    d) The null hypothesis always states that there is a difference



42. The Maximum A Posteriori (MAP) estimate selects:

    a) Any class with probability above 0.1
    *b) The class C that maximizes P(C|X)
    c) The class that maximizes P(X|C) regardless of priors
    d) The class with the smallest label alphabetically
    e) The parameter that minimizes variance only


43. Observing 27 heads in 40 fair‑coin flips is evaluated in lecture by:

    a) Replacing missing flips with the mean
    b) Assuming the coin is biased without testing
    *c) Comparing the observed statistic to a simulated null distribution
    d) Counting only the last five flips
    e) Using a geospatial plot of flips

44. Permutation tests (label shuffling) assess:

    a) How to order categories alphabetically
    b) Whether variables are exactly deterministic
    c) Which distribution family is true a priori
    *d) Whether the observed group difference could arise by chance under the null
    e) The best color map for plots

45. Bootstrapping, as presented, is primarily used to:

    *a) Approximate the sampling distribution of a statistic by resampling with replacement
    b) Force data to follow a Normal distribution
    c) Guarantee smaller variance than the original sample
    d) Encrypt sensitive variables
    e) Eliminate outliers by deletion

46. A central purpose of EDA is to:

    a) Guarantee future market trends
    *b) Reveal structure, anomalies, and relationships in raw data before modeling
    c) Replace statistics with visuals
    d) Finalize the causal model and deploy
    e) Remove all missing data automatically

47. In Bayes’ theorem, the prior P(C) represents:

    *a) Belief about classes before seeing current data
    b) Noise added to stabilize training
    c) A probability that must always be 0.5
    d) The maximum of the likelihood
    e) A resampling weight in bootstrapping


48. Which statement is TRUE regarding discrete vs. continuous modeling per lecture?

    *a) Discrete probabilities sum to 1; continuous densities integrate to 1
    b) Continuous probabilities sum to 1 over observed bins only
    c) Neither requires normalization
    d) Discrete distributions cannot have expectations
    e) Both integrate to 1 only

49. The slides define the 'best guess' class given X as:

    *a) $argmax_i P(C_i|X)$
    b) Choose the smallest index i
    c)  $argmin_i P(C_i|X)$
    d) Random selection
    e)  $argmax_i P(X)$


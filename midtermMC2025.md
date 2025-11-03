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

16. In scraping web pages it is most common to obtain the HTML via the request library and then parse it with the library

    a) scrapy
    b) regexp 
    *c) Beautifulsoup
    d) parsely

17. What is a difference between *Exploratory* Data Analysis and *Explanatory* Data Visualization?

    a) Exploratory is only statistical analysis, Explanatory is only visual analysis
    *b) Exploratory is to understand data, Explanatory presents the outcome
    c) Explanatory Visualization is the prerequisite for EDA
    d) They are two terms are interchangeable

18. Lag plots are typically used to

    a) Show relationships between different variables in time-independent data
    b) The lag effect of a change between a switch from the control group to treatment group
    c) periodic noise in an image
    *d) relationship between values at a fixed separation within a time series


19. Suppose we are analyzing ER admissions over time during a pandemic and we are trying to separate the typical patients from accidents, heart attacks, strokes, and violence from patients suffering from infectious disease. We would likely consider a time series

    a) multiplicative decomposition
    *b) additive decomposition
    c) moving average
    d) PCA

20. When building models on time series (as opposed to other data) an extra consideration is 

    a) that the validation/testing occurs on different data than was used to fit the model
    b) that the validation/testing occurs on data with earlier timestamps than was used to fit the model
    *c) that the validation/testing occurs on data with later timestamps than was used to fit the model
    d) that sequential data is not used in fitting to avoid overfitting

21. Data storytelling is most important when

    *a) presenting the results of the analysis
    b) brainstorming during exploratory data analysis
    c) identifying outliers
    d) interpreting a model

22. When we fit a line using linear regression we are trying to optimize

    a) the number of points a line passes through
    *b) sum of the square of the difference of the y value of the data points and the y value of the proposed line at each x value of the data points
    c) sum of the square of the distance between the each data point and the closest point proposed line (perpendicular to the line)
    d) The probability of an error

23. Which component(s) of data storytelling is(are) particularly critical (but often overlooked)?

    a) Providing a comprehensive view of the data
    b) Proper modulation of your voice
    *c) evoking emotion and providing story (plot) structure
    d) the quality of the data visualizations

24. Why must random numbers be seeded?

    a) otherwise they become less random and clump
    b) it speeds up the generation of such numbers
    c) it allows you to use different distributions (like the normal distribution)
    *d) it allows you to reproduce a result exactly


25. Which of the following is likely the best strategy (preserving the structure of the data) when you have a large number of rows and a small number of missing values spread across different columns? 

    *a) drop the rows with missing values
    b) drop the columns with missing values
    c) fill in the missing values with the row mean
    d) fill in the missing values with zero


26. In the case of linear regression, solving Xa = y for a, we can use a linear algebra solution based on a "linear algebra" solution a=(X^TX)^{-1}X^Ty and another more general but iterative solution based on

    *a) gradient descent
    b) the normal distribution
    c) dynamic programming
    d) tree search

27. In order to visualize the potential dependency between one variable and another we are most likely to use a

    a) violin plot
    *b) scatter plot
    c) a bar graph
    d) a line plot

28. Suppose we have a statistic from two groups, group A and group B and we want to know if the difference between the two groups is statistically significant. We do not know any thing about the distributions of these two groups and cannot thus use a direct simulation. We would most likely use

    *a) the permutation test
    b) a linear regression
    c) a matrix of scatter plots
    d) the covariance

29. If we perform polynomial regression (one variable). Given a set of data, we can fit the training data better and better by increasing the degree of the polynomial. However, this is not a good idea. Why?

    a) the computation explodes with the degree
    b) high degree polynomials result in underfit of the training data (generalizing to test data poorly)
    *c) high degree polynomials result in overfit of the training data (generalizing to test data poorly)
    d) the fit only takes into account the y values and not the x values. When both are used high degrees have poorer fit.


30. What role does visualization play in Data Science?

    *a) Helps humans understand patterns that exist in large datasets
    b) It eliminates the need for data cleaning
    c) It guarantees conclusions are correct
    d) It replaces statistics entirely
    e) It is only useful for small datasets

31. What does statistics help prevent in analysis?

    *a) False conclusions caused by random patterns
    b) Collecting too much data
    c) Good visualizations
    d) The need for computers
    e) Faster machine learning training


32. In NumPy, what is “broadcasting”?

    *a) Automatically expanding arrays to compatible shapes during arithmetic
    b) Sending arrays to a TV channel
    c) Only used when adding identical shapes
    d) A memory compression method
    e) Copying data into SQL databases

33. Which is a key drawback of hash tables?

    a) They require keys to be sorted
    b) They cannot delete items
    *c) They do not preserve meaningful order
    d) Searching is always slower than a linked list
    e) They can only store fixed-size elements

34. In NumPy, why does adding a 1×3 vector to a 3×3 matrix work?

    *a) The vector is broadcast across rows to match shape
    b) The matrix is flattened automatically
    c) NumPy guesses the user’s intention
    d) The vector overwrites the diagonal
    e) Because 3 is a special broadcast-safe number

35. Which part of the data science workflow primarily focuses on understanding the structure, patterns, and anomalies present in the data?

    a) Data Collection
    *b) Exploratory Data Analysis (EDA)
    c) Confirmatory Data Analysis
    d) Feature Deployment
    e) GPU Optimization

36. A bar chart comparing 'Plant Type' and 'Fruit Variety' represents what type of data?

    a) Ordinal vs Quantitative
    *b) Nominal vs Nominal
    c) Ordinal vs Ordinal
    d) Quantitative vs Quantitative
    e) Geospatial vs Quantitative

37. Scatter plots are primarily used to visualize:

    *a) Relationships between two quantitative variables
    b) Distribution of a single variable only
    c) Hierarchical relationships
    d) Statistical inference and p-values
    e) Survey proportions

38. In matplotlib, why is using `fig, ax = plt.subplots()` preferred over calling `plt.plot()` directly?

    a) It uses more memory so it's faster
    *b) It gives explicit references to figure and axes objects for better control
    c) It enables automatic machine learning integration
    d) It prevents adding labels and legends
    e) It is required by NumPy

39. A KDE (Kernel Density Estimate) is used to:

    a) Visualize category labels
    *b) Smooth the distribution of sampled data
    c) Display geospatial movement
    d) Simulate stock trading
    e) Normalize missing values

40. The lecture suggests that before trusting an outlier, you should:

    a) Remove all outliers automatically
    *b) Trace back to the original data and verify context
    c) Replace with the mean
    d) Convert to categorical encoding
    e) Report it as a major scientific discovery

41. Which chart type allows three variables to be shown simultaneously using two axes and color/size encoding?

    a) Bar chart with sublevels
    *b) Scatter plot with a third encoding
    c) Pie chart slices only
    d) Table layout
    e) Q-Q plot

42. A matrix of scatter plots helps you:

    *a) Visualize pairwise relationships among many quantitative variables
    b) Render 3D surfaces of a function
    c) Encode hierarchical trees
    d) Compute p-values for regression
    e) Normalize geospatial coordinates

43. What does a correlation heat map display?

    *a) The sign and magnitude of linear relationships between variables
    b) Raw counts of categories
    c) Geographic elevation
    d) Financial OHLC patterns
    e) Kernel bandwidths

44. Which step most directly ensures that the problem you’re solving is actually a machine‑learning problem and not a simple rules or query task?

    *a) Check whether a labeled target exists and if patterns must generalize to new data
    b) Visualize predictions with a confusion matrix
    c) Collect more data first
    d) Tune hyperparameters with cross‑validation
    e) Train a baseline linear model

45. In a standard ML workflow, a hold‑out test set is primarily used to…

    a) Select the best model during tuning
    b) Fit the feature scaler and imputer
    *c) Estimate the final generalization performance after all modeling choices are frozen
    d) Balance class labels in the training data
    e) Visualize learning curves

46. Which practice best prevents **data leakage** when scaling features?

    *a) Fit the scaler only on the training data, then apply the fitted transform to validation/test
    b) Use MinMax scaling instead of standardization
    c) Use more features so leakage averages out
    d) Shuffle the rows before scaling
    e) Fit the scaler on all available data, then transform splits

47. A **baseline** model in the ML process is best described as…

    a) A model with zero variance predictions
    b) The final, most complex model
    *c) A simple, often naive model used to set a minimum performance bar
    d) Any linear model
    e) A model trained without regularization

48. A confusion matrix is **not** the right tool to evaluate a model when…

    a) You need class‑wise errors
    b) You want false positive rate
    *c) You must compare ranking quality at varying thresholds
    d) You want recall per class
    e) You are solving classification

49. In simple linear regression, the **least squares** estimator chooses coefficients that…

    a) Equalize residuals across x
    b) Minimize mean absolute error of residuals
    c) Maximize R² directly
    d) Minimize classification error
    *e) Minimize the sum of squared residuals

50. You add a perfectly predictive but noisy feature. Training MSE drops sharply; validation MSE rises. The model most likely…

    a) Underfit
    *b) Overfit due to high variance
    c) Suffers from label leakage
    d) Is unbiased
    e) Has perfect calibration

51. Polynomial regression of degree 10 on small n most likely increases…

    a) Sample size
    b) Linearity
    c) Bias
    *d) Variance
    e) Homoskedasticity

52. In supervised classification, what is the primary goal when some rows have known labels?

    a) To delete rows without labels so training is cleaner
    b) To reduce dimensionality for visualization only
    c) To generate synthetic labels for all rows from noise
    *d) To label previously unlabeled rows using a learned model
    e) To cluster the data into groups without labels

53. Which example task is most clearly a multi-class classification problem?

    a) Predicting house prices in dollars
    b) Grouping unlabeled news articles by topic
    c) Estimating the mean of a Gaussian distribution
    d) Finding a low-dimensional embedding of images
    *e) Assigning each handwritten digit image a class from 0–9

54. For k-Nearest Neighbors (kNN), increasing k typically has what effect on the decision boundary?

    a) Has no effect on the boundary; only runtime changes
    b) Converts the classifier into a linear separator
    *c) Smooths the boundary by averaging over more neighbors
    d) Forces the classifier to overfit training data
    e) Makes the boundary more jagged and sensitive to noise

55. Cross-validation is introduced primarily to combat which issue?

    *a) Overfitting and unreliable estimates from a single split
    b) Class imbalance exclusively
    c) Label noise only
    d) GPU memory limits
    e) Too many features

56. In one-dimensional two-class separation, the 'overlap region' between class distributions most directly corresponds to:

    a) Training time
    b) Regularization strength
    c) Bayesian prior probability
    d) Model bias
    *e) Classification error rate

57. Linear Discriminant Analysis (LDA) can be viewed as finding:

    a) A nonlinear kernel mapping to infinite dimensions
    b) A decision tree that partitions space by axis-aligned cuts
    c) A clustering of unlabeled data by k-means
    d) A random forest that averages many trees
    *e) A projection that maximizes between-class separation relative to within-class scatter

58. Which is listed as a *pro* of LDA in the deck?

    a) Nonlinear boundaries by default
    b) Requires deep networks to perform well
    c) Often overfits small datasets
    *d) Usually doesn’t overfit and works with much less data
    e) Slow classification at inference

59. Why is Naïve Bayes called 'naïve' in these slides?

    *a) It assumes features are independent given the class
    b) It assumes k is chosen by cross-validation
    c) It assumes infinite training data
    d) It assumes a linear decision boundary
    e) It assumes labels are uniformly distributed

60. Logistic regression models the log-odds (logit) as:

    a) A sum of kernel functions over support vectors
    *b) A linear function of input features (wᵀx)
    c) A decision tree depth
    d) A constant independent of input features
    e) The reciprocal of a Gaussian density

61. In the logistic regression derivation provided, which activation function maps z=wᵀx to a probability p?

    *a) σ(z)=e^z/(1+e^z)
    b) Hard threshold at z=0
    c) tanh(z)
    d) Softplus(z)=log(1+e^z)
    e) ReLU(z)=max(0,z)

62. Which of the following is *not* one of the four 'brain-dead' baseline algorithms the slides recommend trying first?

    a) Logistic Regression
    *b) Support Vector Machines with RBF kernel
    c) Naïve Bayes
    d) Linear Discriminant Analysis
    e) k-Nearest Neighbors

63. According to the M07B slides, what is a *critical* step before using logistic regression weights as feature importance?

    a) Apply PCA to all features
    *b) Normalize or standardize features to comparable scales
    c) Remove the intercept term
    d) Use L1 regularization
    e) Convert all features to binary indicators

64. Which of the following best captures the motivation slide 'Why do we need explainable models?'

    a) To increase training speed only
    *b) To support trust, debugging, fairness, and accountability in decisions (e.g., 'Why didn’t I get the loan?')
    c) To reduce the need for labeled data
    d) Because explainability always improves accuracy
    e) So we never need test sets again

65. Which statement about fairness and explainability is consistent with the surrounding course materials?

    *a) Choosing one fairness metric can create trade‑offs with others
    b) Fairness is solved by increasing model capacity
    c) All statistical definitions of fairness are mutually compatible
    d) Only demographic parity matters in practice
    e) Explainability eliminates the need for fairness analysis

66. Which of the following statements about Python dictionaries is TRUE?

    a) Dictionaries preserve the order of key insertion in all Python versions
    *b) Keys in a dictionary must be immutable objects
    c) Duplicate keys are allowed and the values are stored in a list
    d) Dictionary keys and values must be of the same type

67. Which of the following statements about the Central Limit Theorem is FALSE?

    a) It applies to the distribution of sample means
    *b) It requires that the population distribution be normal
    c) It becomes more accurate as sample size increases
    d) It implies that the sampling distribution approaches a normal distribution

68. Which of the following statements about hypothesis testing is TRUE?

    a) A small p‑value proves that the null hypothesis is false
    b) Failing to reject the null hypothesis means it is true
    *c) A p‑value is the probability, under the null hypothesis, of obtaining a result as extreme as the one observed
    d) The null hypothesis always states that there is a difference

69. Which of the following statements about cross‑validation is TRUE?

    a) In k‑fold cross‑validation, the value of k must equal the number of observations
    *b) Cross‑validation provides a way to estimate model performance on unseen data
    c) Cross‑validation is only applicable to classification problems
    d) Cross‑validation always reduces overfitting

70. In this course, a 'model' primarily serves to...

    a) Guarantee that data will fit a normal distribution
    b) Tell a compelling narrative that motivates the audience
    c) Eliminate randomness from the world entirely
    d) Automatically generate high‑quality plots without code
    *e) Provide a mathematical abstraction that summarizes patterns and supports prediction

71. For a continuous distribution with density p(x), a core property is that:

    a) ∑ p(x) over the data equals 1
    b) p(x) must always be less than 1
    c) The derivative of p(x) is constant
    d) p(x) must be symmetric around the mean
    *e) ∫ p(x) dx over the support equals 1

72. In the slides, which notation pairing is used (abuse of notation aside)?

    a) Discrete variables must be converted to z‑scores
    b) Only continuous variables can be modeled
    c) Both must be written as integrals only
    *d) P(X) for discrete distributions, p(X) for continuous densities
    e) p(X) for discrete, P(X) for continuous

73. Which expression corresponds to the conditional probability as defined in the slides?

    a) P(C|X) = P(C) · P(X)
    b) P(X|C) = P(C,X) / P(C)
    *c) P(C|X) = P(C,X) / P(X)
    d) P(C|X) = P(C) + P(X)
    e) P(C|X) = 1 − P(C,X)

74. The Maximum A Posteriori (MAP) estimate selects:

    a) Any class with probability above 0.1
    *b) The class C that maximizes P(C|X)
    c) The class that maximizes P(X|C) regardless of priors
    d) The class with the smallest label alphabetically
    e) The parameter that minimizes variance only

75. For a Normal distribution fitted by Maximum Likelihood to i.i.d. data, the parameter estimates are:

    a) Any pair that minimizes the max error
    b) Both parameters are always zero
    c) Sample median for μ and IQR for σ
    *d) Sample mean for μ and sample standard deviation for σ
    e) Skewness for μ and kurtosis for σ

76. Observing 27 heads in 40 fair‑coin flips is evaluated in lecture by:

    a) Replacing missing flips with the mean
    b) Assuming the coin is biased without testing
    *c) Comparing the observed statistic to a simulated null distribution
    d) Counting only the last five flips
    e) Using a geospatial plot of flips

77. Permutation tests (label shuffling) assess:

    a) How to order categories alphabetically
    b) Whether variables are exactly deterministic
    c) Which distribution family is true a priori
    *d) Whether the observed group difference could arise by chance under the null
    e) The best color map for plots

78. Bootstrapping, as presented, is primarily used to:

    *a) Approximate the sampling distribution of a statistic by resampling with replacement
    b) Force data to follow a Normal distribution
    c) Guarantee smaller variance than the original sample
    d) Encrypt sensitive variables
    e) Eliminate outliers by deletion

79. A central purpose of EDA is to:

    a) Guarantee future market trends
    *b) Reveal structure, anomalies, and relationships in raw data before modeling
    c) Replace statistics with visuals
    d) Finalize the causal model and deploy
    e) Remove all missing data automatically

80. Which is one of the narrative components highlighted for data stories?

    a) Kernel bandwidth
    b) Hash seed
    c) ASCII table index
    *d) Conflict
    e) Recursion depth

81. In Bayes’ theorem, the prior P(C) represents:

    *a) Belief about classes before seeing current data
    b) Noise added to stabilize training
    c) A probability that must always be 0.5
    d) The maximum of the likelihood
    e) A resampling weight in bootstrapping

82. In the factorization P(C|X) = P(X|C)P(C)/P(X), P(X) (the 'evidence') mainly serves to:

    a) Set the sampling rate for bootstrapping
    b) Choose color bars for heatmaps
    c) Encode class labels as integers
    d) Maximize the likelihood for each class
    *e) Normalize the posterior over classes so probabilities sum to 1

83. Which is an example of a discrete distribution family discussed in the slides?

    a) Fourier
    b) Cauchy (continuous heavy‑tailed)
    *c) Binomial
    d) Beta‑prime (advanced)
    e) Gaussian mixture with infinite components

84. Diagnostic analytics asks primarily:

    *a) Why did this happen?
    b) What should we do next?
    c) Who is to blame regardless of data?
    d) How to export to PDF?
    e) What color should bars be?

85. Predictive analytics, per the slide taxonomy, addresses:

    a) What happened, historically?
    *b) What may happen in the future?
    c) Where to place legends
    d) Which category is funniest?
    e) How to set DPI for figures

86. Repeating simulations many times primarily helps to:

    a) Guarantee significance
    b) Avoid computing summaries
    *c) Quantify variability of estimates (e.g., Monte Carlo error)
    d) Reduce the true variance in the population
    e) Change the historical data

87. Which Python package was explicitly recommended to visualize missingness patterns?

    a) pytorch.missviz
    b) matplotlib.auto_na
    *c) missingno
    d) seaborn.naheat
    e) cv2.missing

88. Which statement is TRUE regarding discrete vs. continuous modeling per lecture?

    *a) Discrete probabilities sum to 1; continuous densities integrate to 1
    b) Continuous probabilities sum to 1 over observed bins only
    c) Neither requires normalization
    d) Discrete distributions cannot have expectations
    e) Both integrate to 1 only

89. The slides define the 'best guess' class given X as:

    *a) argmaxᵢ P(Cᵢ|X)
    b) Choose the smallest index i
    c) argminᵢ P(Cᵢ|X)
    d) Random selection
    e) argmaxᵢ P(X)

90. A finite‑state machine (FSM) controlling an elevator is used to illustrate:

    a) A continuous‑time Markov chain only
    b) A visualization library
    c) An image compression algorithm
    d) A stochastic bootstrap procedure
    *e) A deterministic system with defined transitions

91. Which trio forms the core 'puzzle pieces' of data storytelling emphasized in the lecture?

    *a) Data, Narrative, Visualizations
    b) Tables, Dashboards, Animation
    c) Python, SQL, Excel
    d) Fonts, Colors, Icons
    e) Neural Nets, GPUs, TPUs

92. Which statement best captures why data is called 'structured' in this context?

    a) It lives in a single file rather than multiple tables.
    b) It is stored as images and audio files.
    c) It contains only numeric values with no missing entries.
    d) It comes from sensors in time order only.
    *e) It has a predefined schema with labeled columns and consistent record shape.

93. Which step most directly ensures that the problem you’re solving is actually a machine‐learning problem and not a simple rules or query task?

    *a) Check whether a labeled target exists and if patterns must generalize to new data
    b) Visualize predictions with a confusion matrix
    c) Collect more data first
    d) Tune hyperparameters with cross‐validation
    e) Train a baseline linear model

94. Which of the following statements about Python dictionaries is TRUE?

    a) Dictionaries preserve the order of key insertion in all Python versions
    *b) Keys in a dictionary must be immutable objects
    c) Duplicate keys are allowed and the values are stored in a list
    d) Dictionary keys and values must be of the same type
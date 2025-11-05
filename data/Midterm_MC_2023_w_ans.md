## ENGR 10200 Fall 2022 Midterm Exam, Part 1, Multiple Choice

First Name: ________________________ 
Last Name: ________________________
ID Number: ________________________

I submit exam as my own original work. I understand that any material copied by or from me constitutes plagiarism and **will** result in failure of the exam, the course and potentially
academic discipline.


Signature _____________________________________


Written Part Closed Book. No references Allowed.
In these questions you must supply short answers.

[//]: # (python language/compilers/interpreters)

[//]: # (type)

1. Which of these expression causes an **error**

 a) `str(0) + 5` <--
 b) `int("25")/5`
 c) `type(9.0/3) == 2.0`
 d) `type(9/3) == type(3)`

[//]: # (variables/assignment)

[//]: # (booleans)

[//]: # (conditionals)

[//]: # (if-elif-else)

2. What does this code print?

```python {.numberLines}
    x = 6
    if x % 3 == 2:
        if x == 6:
            print("x is equal to 6")
        else:
            print("x/3 has remainder 2")
    elif x % 3 == 1:
        print("x cannot be a prime")
    else:
        print("This is absurd!")
```

a) x is equal to 6
b) x/3 has remainder 2
c) x cannot be a prime
d) This is absurd! <--

[//]: # (while)

3. When would you more likely use a **while** loop rather than a for loop?

a) When you are running some code 15 times
b) When you have a list of strings to process.
c) When you don't know how many times you will need to run the code but you have a condition that will stop the loop <--
d) When you think you need to use a continue statement.

[//]: # (for)

4.   What output does this code give?

```python {.numberLines}
    for i in range(9):
        if i%2 == 0:
            continue
        print(2*i)
```

a)  <--
```
2
6
10
14
```
b) 
```
2
6
10
18
```

c) 
```
0
4
8
12
16
```

d)

```
1
3
5
7
```

5. In the expression `y = math.cos(x)`, 

a) `y` is called the function argument, and `x` is the called the function return value
b) `x` is called the function argument, and `y` is the called the function return value <--
c) `x` is called the input, and `y` is the called the output
d) `y` is called the input, and `x` is the called the output


6.  What does the following print?

```python {.numberLines}
x = 90
msg = "fish"
def f(x):
    x = 99
    print(msg)
    return x
msg = "dog"
print(msg, f(x), x)
```

a) <--
```python {.numberLines}
    dog
    dog 99 90
```

b)
```python {.numberLines}
    fish
    dog 99 99
```

c)
```python {.numberLines}
    dog
    dog 99 99
```

d)
```python {.numberLines}
    fish
    dog 99 90
```

[//]: # (lists)

7. For the following code

```python {.numberLines}
thingOne = ('hat',9)
thingTwo = [8, 9]
thingThree = "What is going on here?"
```

which would **not** cause an error?

a) `thingOne[1] = 8`
b) `thingTwo[1] = "hat"` <--
c) `thingTwo[2] = 10`
d) `thingThree[21]="!"`

[//]: # (import libraries)

1. To get access to a fictional library "braineaters" in python you would say

a) `include braineaters`
b) `<- braineaters`
c) `import braineaters` <--
d) `access braineaters`

[//]: # (math library)

[//]: # (random library)

[//]: # (list comprehensions)

9. Which of these is **not** the squares of even numbers less than 100?

a) `np.array([i for i in range(0,100) if i % 2])` <--
b) `np.array([i*i for i in range(0,100) if i % 2 == 0])`
c) `np.array([i**2 for i in range(0, 100, 2)]`
d) `np.array([int(math.pow(i,2)) for i in range(0,100) if not i % 2])`

[//]: # (2d lists)

10. Suppose we have a 2D python array

```python {.numberLines}
    A = [[10 , 12, 16], [12, 8, 3]]
```

which is true?

a) `A[1][1] == 10`
b) `A[1,1] == 8`
c) `A(1,1) == 10`
d) `A[1][1] == 8` <--

[//]: # (set)

[//]: # (dictionary)

11. The method for getting key value tuples from a dictionary bar is:

a) `bar.elements()`
b) `bar.items()` <--
c) `bar.values()`
d) `bar.keys()`

12. If we have a dictionary `favorite_ices = {'stewart': 'bannana', 'kevin': 'lemon'}'` and we execute the code `print("popular flavors are {kevin} and {stewart}".format(**favorite_ices))`, what is the output?

a) popular flavors are bannana and lemon
b) popular flavors are {kevin} and {stewart}
c) popular flavors are lemon and bannana <--
d) the code does not run because of a syntax error

[//]: # (numpy: creating)

1.  A NumPy array cannot have

a) integer data, it can only hold floats
b) float data, it can only hold integers
c) multiple different types of data <--
d) float32 data

[//]: # (numpy: fancing indexing)

[//]: # (pandas: Series and DataFrame)

14.   The difference between a pandas DataFrame and a pandas Series is that

a) The DataFrame can have two "index" columns
b) The Series can only contain a single column of data <--
c) Only the series can have dates
d) The Series is made up of a sequence of DataFrames

15. In a pandas series the index is always

a) integers starting at 0 up to one minus the number of rows, indexing the row just like a python list
d) a set of column names
c) a set of labels (could be ints) referencing each row <--
d) the integer starting at 0 up to one minus the number of columns indexing the column


[//]: # (pandas: head)

[//]: # (pandas:iloc and loc)

1.   Pandas DataFrame has methods iloc and loc. Which is true?

a) iloc is for addressing by index while loc indexes by name <--
b) iloc is for by name while loc by index
c) iloc is for columns but loc is only for rows
d) With loc you can get rows and columns but iloc only rows

[//]: # (fstring)

[//]: # (string formating)

17.  If `phrase = 'snap crackle pop'` and we want the variable
    `message == 'snap, crackle, pop'` which will **not** work?

a)
```python
    message = phrase.replace(" ",", ")
```

b) <--
```python
    message = phrase.sub(" ",", ")
```

c)
```python 
    message = ', '.join("snap crackle pop".split())
```

d) 
```python
    one, two, three = "snap crackle pop".split()
    message = f"{one}, {two}, {three}"
```

[//]: # (compute basic statisics)

18.  Which data structure is less well adapted to computing basic statistics directly on the data, for example it doesn't have a "mean" method?

a) pandas Series
b) pandas DataFrame
c) numpy.array
d) List <--

[//]: # (visualiztion: plot)

[//]: # (visualization: histogram)

[//]: # (visualization: scatter plot)

19.   Which chart is best for showing the relationship of two variables for a collection of measurements like weight and height?

a) Bar Graphs
b) Line Graphs
c) Scatter Plots <--
d) Pie Charts

[//]: # (simulation)

[//]: # (statistic of sample)

[//]: # (parameter of population)

20. What is the difference between a parameter and a statistic?


a) A statistic is a number that we usually can't know which describes a population, a parameter is function of a sample.
b) A parameter is a number that we usually can't know which describes a population, a statistic is function of a sample. <--
c) A parameter is a central tendency of a sample, a statistic is the spread of a population.
d) A parameter is the spread of a sample, a statistic is the central tendency of a population.


[//]: # (sampling/emperical distribution)

[//]: # (probabilities)

21.  In the Monty Hall problem we have three doors. Behind one door is a car, behind the other two doors are junks, eg. a goat and a pile of junk. The contestant chooses a door, let's say door 1. The host, who knows what is behind the doors, opens one of the other doors, let's say door 3, which has a goat behind it. The host then gives the contestant the option to stick with their original choice or switch to the last unopened door, let's say door 2. If the contestant sticks with their original choice the probability of getting the car

a) is 1/2 because it is either behind door 1 or door 2.
b) is 2/3 because the probability of the door they picked has changed from 1/3 to 2/3.
c) is 1/3 since there were three doors and one was chosen. <--
d) can only be computed with a computer simulation 


[//]: # (comparing two samples -Permutation test-)

22.    Suppose we have a collection of weight measurements from two group of birds. We want to show that there is a statistically significance different in mean from the two groups. In this case we could shuffle the labels of data, which is called

a) the hypothesis test
b) the permutation test <--
c) the hypothesis test
d) the simulation test

[//]: # (bootstarap)

23.  Suppose we have a sample of 50 height measurments. We want to estimate the probability distribution of possible mean heights. As a result we re-sample from our original sample **with replacement**, and compute the mean. This is called

a) the standard deviation
b) p-value
c) the permutation test
d) the bootstrap <--

[//]: # (central tendency)

[//]: # (spread)

[//]: # (Exeptions)

24.   When will we see the output "The answer you seek is 42" and "Heat death of the universe"?

```python {.numberLines}
try:
    with open("file.txt") as fid:
        pass
except:
    print("Houston, we have a problem")
else:
    print("The answer you seek is 42")
finally:
    print("Heat death of the universe")
```

a) Pass is not a valid python statement so this is an error and crashes the program.
b) When the "file.txt" does not exists or cannot be read.
c) When the "file.txt" exists and can be read. <--
d) You will never see both the output "The answer you seek is 42" and "Heat death of the universe" at the same time.


25. Which of the following is **not** a measure of spread

a) p-value <--
b) standard deviation
c) max-min
d) variance

[//]: # (I/O file)

26.  Which of the following can be used to open a file called csvFile.csv in read-only mode?

a) `infile = open("csvFile.csv", “w”)`
b) `infile = open("csvFile.csv", r)`
c) `infile = open("csvFile.csv", “read”)`
d) `infile = open("csvFile.csv", "r")` <--


[//]: # (pandas: creating)

27.  Which of the following is **not** a valid way to create a pandas DataFrame?

a) `df = pd.DataFrame(); df['primes']=[2,3,5,7,11];df.index=[1,2,3,4,5]`
b) `df = pd.DataFrame(np.array([2,3,5,7,11]), columns = ["primes"], index = [1, 2, 3, 4, 5])`
c) `df2 = pd.DataFrame();df2.index[:,:] = [[1,2,3,4,5],[2,3,5,7,11]];df2.columns = ["primes"]` <--
d) `df = pd.DataFrame({"numbers": [2,3,5,7,11]}, columns = ["primes"])`


[//]: # (hypothesis testing)

28.  You are asked to run a hypothesis test to test whether two sample means are different from each other or not. Your null hypothesis is that there is no difference in the sample means. Your alternative hypothesis is that the sample means are different from each other. You run the test and find a p-value of 0.001. If we believe our conclusion should have a probability of greater than 95%, what does this mean?

a) We reject the null hypothesis the p-value is less than 0.05. <--
b) The p-value is too small to reject the null hypothesis, it must be greater than .95.
c) We do not have enough information to assess whether we have enough evidence to reject or fail to reject the null hypothesis.
d) We have proven that there is a 95% probability that the sample means are different from each other.

29. Which of the following is an advantage of encapsulation?

a) It makes code easier to reuse
b) It allows data hiding <--
c) It enables the same method name to be used by different classes
d) It reduces coupling

30.  Which attribute is designated a private attribute?

a) `self._x` <--
b) `private x`
c) `private(self.x)`
d) `self_private.x`

31. If we are building a confidence interval for the mean based on sample, then a 95% confidence interval we are trying to find

a) the range that contains 95% of the data
b) the range of values that with 95% probability contains the population mean <--
c) the range of values that contain 95% of population values
d) the interquartile range of the sample

32. What is the difference between a function and a method in Python?

a) A function is global, a method is local
b) A method does not have arguments, a function does
c) A method is associated with a class, a function is standalone <--
d) A function returns a value, a method modifies state


33. What does the `__init__()` method do?

a) Initializes a new instance of a class <--
b) It defines class attributes
c) It starts a process
d) Calls the parent constructor

34. What is the main difference between a class and an object in Python?


a) An object is a blueprint, a class is an instance created from the object
b) There is no difference between a class and an object in Python
c) A class contains methods, an object contains attributes
d) A class is a blueprint, an object is an instance created from the class <--

35.  Which is **not** true when using permutation test

a) our null hypothesis is that the data is drawn from the same population
b) we need to assume that the data is drawn from a population with a normal distribution <--
c) we shuffle the labels of the groups associated with the data via random permutations
d) we can reject the null hypothesis if the observed difference is unlikely compared to those obtained from the "groups" with the labels shuffled

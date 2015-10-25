# HH School 2015

## Tasks:
---
### 1. Median
Given two sorted numeric array of the same length N. Find the median of the numerical array of length 2N, containing all the numbers of the two data sets. 

```
Sample input: 
1 2 3 4 
1 4 5 6 

Example output: 
3.5 
```

### 2. Conversion
We call the transformation of an integer n the use of one of the following: 

* n -> n + 1 
* n -> n + 2 
* n -> 2n 

Write a program that, given the numbers n and m defines the length of the shortest sequence of transformations, which translates into a number n integer m.

Where n and m: (0 <= n <= m <= 10 ^ 15). 

```
Example: 
n = 5, m = 13 

Answer: 3
```

## Usage:
---
### Requirements
Python 3.5

### Run median program
```
python median.py
```

Median program read imput from file: *median_input.txt*.

Format in *median_input.txt*:

```
1,2,3,4
1,4,5,6
```

Output:

```
[1, 2, 3, 4]
[1, 4, 5, 6]
The median is: 3.5
Done
```


### Run conversion program
```
python conversion.py
```

Conversion program read imput from file: *conversion_input.txt*.

Format in *conversion_input.txt*:
```
5,13
```

Output:
```
n = 5
m = 13
The length of the shortest sequence of transformations: 3
Done
```

## Unit tests
* test_median.py
* test_conversion.py

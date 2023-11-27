Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*


---
## Bioinformatics 1
##### Exercise sheet 4: Sequence Alignment - affine gap costs
---

### _Exercise 4 - Programming assignment: Implementation of Gotoh algorithm_

The programming assignment will use a scoring function as parameters which is a dictionary with 4 entries.
This will look as follows:

<p align="center">
scoring = {"match": -1,
               "mismatch": 1,
               "gap_introduction": 4,
               "gap_extension: 1}
</p>

You do not need to write the scoring function by yourself. However, make sure you use the correct keys in your implementation.
An example will be provided in the skeleton of part *a)*.

Despite most implementations of Gotoh will use a maximization at the optimization step, we will stick to the lecture and use minimization (score(match) < score(gap)). Also, have a look at return typehints in the skeleton functions and read carefully how the results should be returned.


**a)** Implement the function zero_init() which takes two sequences S1 and S2 and creates the Needleman-Wunsch matrix and initiates all the matrix values with zeroes. Hereby S1 should be represented by the rows and S2 by the columns.


**b)** Implement the function d_matrix_init() which takes two sequences S1 and S2 as well as the scoring function and fills in the values for the first row and first column of the D matrix with the correct values. Utilize *a)* in your implementation.

**c)** Implement the function p_matrix_init() which takes two sequences S1 and S2 and fills in the values for the first row and first column of the P matrix with the correct values. Utilize *a)* in your implementation.

**d)** Implement the function q_matrix_init() which takes two sequences S1 and S2 and fills in the values for the first row and first column of the Q matrix with the correct values. Utilize *a)* in your implementation.

**e)** Implement the function gotoh_init() which initializes all three matrices. Utilize *b)*, *c)*, *d)* in your implementation.

**f)** Implement the function gothoh_forward() which takes the two sequences S1 and S2 and the scoring function and output the complete matrices D, P and Q filled in with the Gotoh approach.

The following steps will help you with implementing the traceback.

**g)** Implement the function previous_cells() which takes two sequences S1 and S2, scoring function, the filled in recursion matrices from the step *f)* and the cell coordinates as a tuple with the matrix name and the coordinates pair (matrix, (row, column)). I.e. ("D", (2, 3))
The function should output a list of tuples of all possible previous cells. The tuples should be again structured like (matrix, (row, column)). Use capital D, P and Q to refer to the corresponding matrix

**h)** Implement the function build_all_traceback_paths() which builds all possible traceback paths. This function should return a list of possible paths which themselves are a list of tuples (matrix, (row, column)). The ordering must be decreasing. Meaning paths should start in the lower right corner of the matrix D.

**i)** Implement the function build_alignment() which takes two sequences and a path as a list of tuples. This function should return an alignment tuple. Meaning two strings of same length with introduced gaps.

---

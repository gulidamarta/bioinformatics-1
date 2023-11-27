Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 1
###### WS 2021/2022
##### Exercise sheet 3: Sequence Alignment
---


### _Exercise 4 - Programming assignment: Implementation of Needleman-Wunsch algorithm_

The programming assignment will use a scoring function as parameters which is a dictionary with 3 entries. 
This will look as follows:

<p align="center">
scoring = {"match": -1,
               "mismatch": 1,
               "gap_introduction": 0}
</p>

You do not need to write the scoring function by yourself. However, make sure you use the correct keys in your implementation.
An example will be provided in the skeleton of part *a)*. 

Despite most implementations of Needleman Wunsch will use a maximization at the optimization step, we will stick to the lecture and use minimization (score(match) < score(gap)). Also, have a look at return typehints in the skeleton functions and read carefully how the results should be returned.


**a)** Implement the function zero_init() which takes two sequences S1 and S2 and creates the Needleman-Wunsch matrix and initiates all the matrix values with zeroes. Hereby S1 should be represented by the rows and S2 by the columns.


**b)** Implement the function nw_init() which takes two sequences S1 and S2 as well as the scoring function and fills in the values for the first row and first column of the matrix with the correct values. Utilize *a)* in your implementation.

**c)** Implement the function nw_forward() which takes the two sequences S1 and S2 and the scoring function and output the complete matrix filled with the Needleman-Wunsch approach.

The following steps will help you with implementing the traceback.

**d)** Implement the function previous_cells() which takes two sequences S1 and S2, scoring function, the filled in recursion matrix from the step *c)* and the cell coordinates as a tuple (row, column).
The function should output a list of tuples of all possible previous cells. The tuples should be again structured like (row, column).

**e)** Implement the function which builds all possible traceback paths. This function should return a list of possible paths which themselves are a list of tuples (row, column). The ordering must be decreasing. Meaning paths should start in the lower right corner of the matrix.

**f)** Implement the function build_alignment() which takes two sequences and a path as a list of tuples. This function should return an alignment tuple. Meaning two strings of same length with introduced gaps. 

---

### _Preparing for the Exam_

The [exam_practice_nw.py](./exam_practice_nw.py) file provides the possibility to create training examples for the exam. 
You can use it as a command line tool e.g. like:

```shell
python exam_practice_nw.py --first AAATGT --second AATTAAAA --match -1 --mismatch 0 --gap_introduction 1 --file_name matrix.csv
```

This will produce a csv file that you can import into Excel, Libre Office Calc, etc., where you can fill in the forward values by yourself. 

To check if you provided the correct result,
you can use the `--check True` flag and run it similarily.

```shell
python exam_practice_nw.py --check True --first AAATGT --second AATTAAAA --match -1 --mismatch 0 --gap_introduction 1 --file_name matrix_correct.csv
```

---

#### _Recommended good practices_

Here we have included some best practices helping you solve the exercises as efficiently as possible. First, clone the assignment repository.
    

```
$ git clone git@github.com:Bioinformatics-teaching/exercise-sheet-3-sequence-alignment-userID.git
```

Do not forget to use your own user ID. Now, answers the questions.


```
$ cd exercise-sheet-3-sequence-alignment-userID
$ emacs -nw exercise_sheet3.py
```

Include the changes and make a commit describing the modifications.


```
$ git add exercise_sheet3.py
$ git commit -m "Description of your modifications"
```

 
Send your results.       


```
$ git push
```

Done! But, it would be nice to know something about the score, wouldn't it? Let's check the autograding results. This PR will also be used by the teachers to include specific comments.


<img src="./figures/sheet2_classroom.gif" alt="Autograding" width=100%/>


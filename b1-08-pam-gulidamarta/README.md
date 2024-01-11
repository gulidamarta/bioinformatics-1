Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 1
##### Exercise sheet 8: Substitution Scoring
---

### _Exercise 2 - Programming assignmnet: Substitution Scoring Models_

After manually calculating the PAM matrices in the exercise 1, you are now tasked to implement each of the steps.
Make use of the formulae introduced before. All the functions should take an argument called sym_align which represents the symmetric alignment as a tuple of strings 

**a)** Implement the calculation of the nucleotide frequencies for a symmetric alignment. Make sure that the indexing works the following way:

- [0] = A
- [1] = C
- [2] = T
- [3] = G

**b)** Implement the calculation of the mutation matrix. Remember indexing as in the previous exercise.

**c)** Implement the calculation of the unnormalized PAM scores. Remember indexing as in the previous exercise.

**d)** Implement the calculation of the normalization factor gamma.

**e)** Implement the calculation of the probability matrix.

**f)** Implement the calculation of the normalized probability matrix.

**g)** Implement the calculation of the PAM matrix. Make sure to round values to integers.

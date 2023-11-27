Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*

---
## Bioinformatics 1
##### Exercise sheet 2: Edit operations and alignments
---




### _Programming assignment: Levenshtein Distance_

**a)** Implement the function **levenshtein_substitution()** which takes two sequences of the same length and 
computes the minimum number of substitutions to transform one into another.

**b)** Implement the function **levenshtein_deletion()** which takes two sequences and returns the positions of characters from the longest sequences which should be deleted to 
transform the sequence into the other one.This should be returned as a list of indices (int).
If such deletion can not be done the function should return *None*. Also, if there are no editing operations needed the function should return an empty list.

Albert-Ludwigs-Universität Freiburg

Lehrstuhl für Bioinformatik - Institut für Informatik - *http://www.bioinf.uni-freiburg.de*


---
## Bioinformatics 1
##### Exercise sheet 10: UPGMA
---

### _Exercise 4 - Programming assignment_
In this programming assignment we want you to implement functions that will allow you to generate a phylogenetic tree in Newick's format using an input distance matrix.

To this end, we provide helper classes `Node`, `Tree` and a function `compute_distance` to aid you in your task. Detail on how to use these helpers can be found in the `exercise_sheet10.py` file.

a) Implement the function `convert_to_nodes` which takes the distance matrix information and converts it to a list of nodes.

b) Implement the function `merge_best_pair` which takes a list of elements which can be both nodes and trees. It finds the best pair to merge based on the distance. Then it merges the two closest objects and returns a list with the merged object as well as the remaining unmerged ones.
Use the `compute_distance` function to determine the distance between two elements.

c) Implement the function `build_the_tree` which takes the distance information and outputs the final tree in Newick's representation.
Use your implementations of `convert_to_nodes` and `merge_best_pair` to create this function.
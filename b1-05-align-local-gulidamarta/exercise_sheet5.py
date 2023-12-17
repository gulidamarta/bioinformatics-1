from typing import List, Tuple, Dict


########################################################
############## Programming tasks #######################
########################################################


def sw_init(seq1, seq2):
    """
    Exercise 3 a
    Implement the function sw_init() which takes two sequences S1 and S2 and
    creates the Smith-Waterman matrix and initiates all the matrix values
    with zeroes. Hereby S1 should be represented by the rows and S2 by
    the columns.
    """
    return [[0]*(len(seq2) + 1) for _ in range(len(seq1) + 1)]


def sw_forward(seq1, seq2, scoring: Dict[str, int]):
    """
    Exercise 3 b
    Implement the function sw_forward() which takes the two sequences S1 and
    S2 and the scoring function and output the complete matrix filled with
    the Smith-Waterman approach.
    """
    match, mismatch, gap = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
    )
    return None


def previous_cells(
    seq1, seq2, scoring, sw_matrix, cell: Tuple[int, int]
) -> List[Tuple[int, int]]:
    """
    Exercise 3 c
    Implement the function previous_cells() which takes two sequences S1 and
    S2, scoring function, the filled in recursion matrix from the step c) and
    the cell coordinates (row, column). The function should output the list
    of all possible previous cells.
    """
    return None


def build_all_traceback_paths(
    seq1, seq2, scoring, sw_matrix
) -> List[List[Tuple[int, int]]]:
    """
    Exercise 3 d
    Implement the function which builds all possible traceback paths.
    """
    return None


def build_alignment(seq1, seq2, traceback_path) -> Tuple[str, str]:
    """
    Exercise 3 e
    Implement the function build_alignment() which takes two sequences and
    outputs the alignment.
    """
    return None

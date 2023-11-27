from helpers.matrix_helpers import nw_init_csv_maker
from typing import Dict, List, Tuple

########################################################
############## Programming tasks #######################
########################################################


def zero_init(seq1, seq2):
    """
    Exercise 4 a
    Implement the function zero_init() which takes two sequences S1 and S2 and
    creates the Needleman-Wunsch matrix and initiates all the matrix values
    with zeroes. Hereby S1 should be represented by the rows and S2 by
    the columns.
    """
    return [[0]*(len(seq2) + 1) for _ in range(len(seq1) + 1)]


def nw_init(seq1, seq2, scoring: Dict[str, int]):
    """
    Exercise 4 b
    Implement the function nw_init() which takes two sequences S1 and S2 as
    well as the scoring function and fills in the values for the first row and
    first column of the matrix with the correct values. Utilize a) in your
    implementation.
    """
    match, mismatch, gap = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
    )
    matrix = zero_init(seq1, seq2)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0:
                matrix[i][j] = j * gap

            if j == 0:
                matrix[i][j] = i * gap

    return matrix


def nw_forward(seq1, seq2, scoring: Dict[str, int]):
    """
    Exercise 4 c
    Implement the function nw_forward() which takes the two sequences S1 and
    S2 and the scoring function and output the complete matrix filled with
    the Needleman-Wunsch approach.
    """
    match, mismatch, gap = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
    )

    initialized_matrix = nw_init(seq1, seq2, scoring)
    for i in range(1, len(initialized_matrix)):
        for j in range(1, len(initialized_matrix[i])):
            diagonal_element_score = match if seq1[i - 1] == seq2[j - 1] else mismatch
            initialized_matrix[i][j] = min(
                initialized_matrix[i - 1][j] + gap,
                initialized_matrix[i][j-1] + gap,
                initialized_matrix[i-1][j-1] + diagonal_element_score,
            )

    return initialized_matrix


def previous_cells(
    seq1, seq2, scoring, nw_matrix, cell: Tuple[int, int]
) -> List[Tuple[int, int]]:
    """
    Exercise 4 d
    Implement the function previous_cells() which takes two sequences S1 and
    S2, scoring function, the filled in recursion matrix from the step c) and
    the cell coordinates (row, column). The function should output the list
    of all possible previous cells.
    """
    match, mismatch, gap = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
    )
    nw_matrix = nw_forward(seq1, seq2, scoring)

    requested_row, requested_column = cell
    requested_element = nw_matrix[requested_row][requested_column]

    diagonal_penalty = match if seq1[requested_row - 1] == seq2[requested_column - 1] else mismatch
    diagonal = nw_matrix[requested_row - 1][requested_column - 1] + diagonal_penalty
    left = nw_matrix[requested_row][requested_column - 1] + gap
    up = nw_matrix[requested_row - 1][requested_column] + gap

    result_list = []
    if requested_element == up:
        result_list.append((requested_row - 1, requested_column))

    if requested_element == left:
        result_list.append((requested_row, requested_column - 1))

    if requested_element == diagonal:
        result_list.append((requested_row - 1, requested_column - 1))

    return result_list


def build_all_traceback_paths(
    seq1, seq2, scoring, nw_matrix
) -> List[List[Tuple[int, int]]]:
    """
    Exercise 4 e
    Implement the function which builds all possible traceback paths.
    """
    traceback_paths_list = []

    cell = len(nw_matrix) - 1, len(nw_matrix[0]) - 1
    bottom_bound = [[cell]]
    while bottom_bound:
        path = bottom_bound.pop()
        last_cell = path[-1]

        next_steps = previous_cells(seq1, seq2, scoring, nw_matrix, last_cell)
        for next_step in next_steps:
            traceback_path = path + [next_step]
            if next_step == (0, 0):
                traceback_paths_list.append(traceback_path)
            else:
                bottom_bound.append(traceback_path)

    return traceback_paths_list


def build_alignment(seq1, seq2, traceback_path) -> Tuple[str, str]:
    """
    Exercise 4 f
    Implement the function build_alignment() which takes two sequences and
    outputs the alignment.
    """
    alignment_first_string = ''
    alignment_second_string = ''

    # Revert traceback paths
    alignment = traceback_path[::-1]

    # And start from the upper left corner (0, 0)
    previous_row, previous_column = 0, 0

    # Iterate over the pairs (row, column)
    for cell in alignment[1:]:
        row, column = cell

        if (row > previous_row) and (column > previous_column):
            alignment_first_string += seq1[row - 1]
            alignment_second_string += seq2[column - 1]
        elif row > previous_row:
            alignment_first_string += seq1[row - 1]
            alignment_second_string += '-'
        else:
            alignment_first_string += '-'
            alignment_second_string += seq2[column - 1]

        previous_row, previous_column = row, column

    return alignment_first_string, alignment_second_string


if __name__ == "__main__":
    """
    You can run this to create csv files from two sequences. Further you can 
    import this file in excel or some similar program, where you can fill in
    the forward values yourself.    
    """
    seq1 = "AT"
    seq2 = "CTAT"
    scoring = {"match": -1, "mismatch": 0, "gap_introduction": 1}

    nw_init_csv_maker(seq1, seq2, scoring)

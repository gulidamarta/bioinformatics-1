from typing import Dict, List, Tuple


def sw_init_correct(seq1, seq2):
    return [[0] * (len(seq2) + 1) for _ in range(len(seq1) + 1)]


def sw_forward_correct(seq1, seq2, scoring):
    matrix = sw_init_correct(seq1, seq2)
    match_score, mismatch_score, gap_score = (
        scoring["match"],
        scoring["mismatch"],
        scoring["gap_introduction"],
    )

    for row_index, row in enumerate(matrix[1:], 1):
        for column_index, column in enumerate(row[1:], 1):
            char_seq_1, char_seq_2 = (
                seq1[row_index - 1],
                seq2[column_index - 1],
            )
            no_gap_score = (
                match_score if char_seq_1 == char_seq_2 else mismatch_score
            )

            diagonal = matrix[row_index - 1][column_index - 1] + no_gap_score
            left = matrix[row_index][column_index - 1] + gap_score
            top = matrix[row_index - 1][column_index] + gap_score
            min_val = max(top, left, diagonal, 0)
            matrix[row_index][column_index] = min_val
    return matrix


def previous_cells_correct(seq1, seq2, scoring, sw_matrix, cell):
    prev_cells = []
    row, column = cell

    top = (row - 1, column) if row > 0 else None
    left = (row, column - 1) if column > 0 else None
    diagonal = (row - 1, column - 1) if (row > 0 and column > 0) else None

    cur_val = sw_matrix[row][column]
    char_first, char_second = seq1[row - 1], seq2[column - 1]
    match_score = (
        scoring["match"] if char_first == char_second else scoring["mismatch"]
    )
    gap_score = scoring["gap_introduction"]

    if diagonal:
        diagonal_val = sw_matrix[diagonal[0]][diagonal[1]]
        if (diagonal_val + match_score) == cur_val:
            prev_cells.append(diagonal)

    if top:
        top_val = sw_matrix[top[0]][top[1]]
        if (top_val + gap_score) == cur_val:
            prev_cells.append(top)

    if left:
        left_val = sw_matrix[left[0]][left[1]]
        if (left_val + gap_score) == cur_val:
            prev_cells.append(left)

    return prev_cells


def build_all_traceback_paths_correct(seq1, seq2, scoring, sw_matrix):
    list_traceback_paths = []

    flat = [x for row in sw_matrix for x in row]
    max_val = max(flat)

    if max_val == 0:
        return [[]]

    frontier = []

    for row_index, row in enumerate(sw_matrix):
        for column_index, column in enumerate(row):
            if sw_matrix[row_index][column_index] == max_val:
                frontier.append([(row_index, column_index)])

    while frontier:
        partial_path = frontier.pop()
        last_cell_partial = partial_path[-1]
        next_steps = previous_cells_correct(
            seq1, seq2, scoring, sw_matrix, last_cell_partial
        )
        for next_step in next_steps:
            new_traceback_path = partial_path + [next_step]
            row, column = next_step
            matrix_value = sw_matrix[row][column]
            if matrix_value == 0:
                list_traceback_paths.append(new_traceback_path)
            else:
                frontier.append(new_traceback_path)

    return list_traceback_paths


def build_alignment_correct(seq1, seq2, alignment_path):
    align_seq1 = ""
    align_seq2 = ""

    if not alignment_path:
        return "", ""

    alignment_path = alignment_path[::-1]

    prev_cell = alignment_path[0]

    for cell in alignment_path[1:]:
        prev_row, prev_column = prev_cell
        row, column = cell

        if (row > prev_row) and (column > prev_column):
            align_seq1 += seq1[row - 1]
            align_seq2 += seq2[column - 1]

        elif row > prev_row:
            align_seq1 += seq1[row - 1]
            align_seq2 += "-"

        elif column > prev_column:
            align_seq1 += "-"
            align_seq2 += seq2[column - 1]

        prev_cell = cell

    return align_seq1, align_seq2


def main():
    scoring = {"match": 2, "mismatch": -1, "gap_introduction": -1}
    s1 = "ATTGC"
    s2 = "TTT"

    h = sw_forward_correct(s1, s2, scoring)

    print("_____")
    for row in h:
        print(row)
    print("_____")

    paths = build_all_traceback_paths_correct(s1, s2, scoring, h)
    for p in paths:
        print(p)
        al = build_alignment_correct(s1, s2, p)
        al_seq1, al_seq2 = al
        print(al_seq1)
        print(al_seq2)
        print("_____")


if __name__ == "__main__":
    main()

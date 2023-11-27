import pprint
import random

import pytest

from exercise_sheet4 import *
from gotoh_implementation.gotoh import *

HELPER = {
    0: "d",
    1: "p",
    2: "q"
}

SCORING = [
    {"match": -1, "mismatch": 0, "gap_introduction": 4, "gap_extension": 1},
    {"match": -1, "mismatch": 0, "gap_introduction": 2, "gap_extension": 1},
    {"match": -1, "mismatch": 1, "gap_introduction": 2, "gap_extension": 1},
    {"match": -2, "mismatch": 1, "gap_introduction": 2, "gap_extension": 1},
]


def random_seq_generator(length, random_seed):
    random.seed(random_seed)
    return "".join(
        [random.choice(["A", "T", "C", "G"]) for _ in range(length)]
    )


def check_none(*args):
    if None in args:
        print("you have not filled in all the fields")
        raise ValueError


def check_zero_in_dict(d):
    val = d.values()
    if 0 in val:
        print("you have not filled in all the fields")
        raise ValueError


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
def test_exercise_4a(seq1, seq2):
    matrix_expected = zero_init_correct(seq1, seq2)
    matrix = zero_init(seq1, seq2)
    if matrix != matrix_expected:
        print(
            f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\n")
        print(f"Your init matrix is:")
        pprint.pprint(matrix)
        print("It is supposed to look like:")
        pprint.pprint(matrix_expected)
    assert matrix == matrix_expected


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4b(seq1, seq2, scoring):
    matrix_expected = init_d_matrix_correct(seq1, seq2, scoring)
    matrix = d_matrix_init(seq1, seq2, scoring)
    if matrix != matrix_expected:
        print(
            f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\n")
        print(f"Your d-matrix is:")
        pprint.pprint(matrix)
        print("It is supposed to look like:")
        pprint.pprint(matrix_expected)
    assert matrix == matrix_expected


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
def test_exercise_4c(seq1, seq2):
    matrix_expected = init_p_matrix_correct(seq1, seq2)
    matrix = p_matrix_init(seq1, seq2)
    if matrix != matrix_expected:
        print(
            f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\n")
        print(f"Your p-matrix is:")
        pprint.pprint(matrix)
        print("It is supposed to look like:")
        pprint.pprint(matrix_expected)
    assert matrix == matrix_expected


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
def test_exercise_4d(seq1, seq2):
    matrix_expected = init_q_matrix_correct(seq1, seq2)
    matrix = q_matrix_init(seq1, seq2)
    if matrix != matrix_expected:
        print(
            f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\n")
        print(f"Your q-matrix is:")
        pprint.pprint(matrix)
        print("It is supposed to look like:")
        pprint.pprint(matrix_expected)
    assert matrix == matrix_expected


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4e(seq1, seq2, scoring):
    expected_matrices = gotoh_init_correct(seq1, seq2, scoring)
    matrices = gotoh_init(seq1, seq2, scoring)
    for x, matrix in enumerate(matrices):
        if matrix != expected_matrices[x]:
            print(
                f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}")
            print(f"Your {HELPER[x]}-matrix is:")
            pprint.pprint(matrix)
            print("It is supposed to look like:")
            pprint.pprint(expected_matrices[x])
    assert matrices == expected_matrices


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4f(seq1, seq2, scoring):
    expected_matrices = gotoh_forward_correct(seq1, seq2, scoring)
    matrices = gotoh_forward(seq1, seq2, scoring)
    for x, matrix in enumerate(matrices):
        if matrix != expected_matrices[x]:
            print(
                f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}")
            print(f"Your {HELPER[x]}-matrix is:")
            pprint.pprint(matrix)
            print("It is supposed to look like:")
            pprint.pprint(expected_matrices[x])
    assert matrices == expected_matrices


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
@pytest.mark.parametrize(
    "cell",
    [
        ("D", (3, 2)),
        ("D", (3, 3)),
        ("D", (2, 2)),
        ("D", (3, 1)),
        ("P", (3, 2)),
        ("Q", (3, 2)),
        ("Q", (3, 3)),
     ]
)
def test_exercise_4g(seq1, seq2, scoring, cell):
    d, p, q = gotoh_forward_correct(seq1, seq2, scoring)
    expected_prev = previous_cells_correct(seq1, seq2, scoring, d, p, q, cell)
    prev = previous_cells(seq1, seq2, scoring, d, p, q, cell)
    expected_cells = set(expected_prev)
    actual_cells = set(prev)
    if actual_cells != expected_cells:
        print(f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\ncell: {cell}\n"
              f"scoring: {scoring}")
        print(f"Your previous cells are:\n{actual_cells}")
        print(f"It should be:\n{expected_cells}")
    assert actual_cells == expected_cells


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4h(seq1, seq2, scoring):
    d, p, q = gotoh_forward_correct(seq1, seq2, scoring)
    expected_paths = build_all_traceback_paths_correct(seq1, seq2, scoring, d, p, q)
    expected_paths = [tuple(x) for x in expected_paths]
    expected_paths = set(expected_paths)
    actual_paths = build_all_traceback_paths(seq1, seq2, scoring, d, p, q)
    actual_paths = [tuple(x) for x in actual_paths]
    actual_paths = set(actual_paths)
    if actual_paths != expected_paths:
        print(
            f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}")
        print(f"Your paths are:")
        pprint.pprint(actual_paths)
        print(f"It should be:")
        pprint.pprint(expected_paths)
    assert expected_paths == actual_paths


@pytest.mark.parametrize(
    "seq1,seq2",
    [
        ("TCCGA", "TACGCGC", ),
        ("TCCCGG", "TCAAA",),
        ("TCCGA", "TACGCGC", ),
        ("AAA", "TTT", ),
        ("TACGCAGA", "TCCGA", ),

    ] + [
        (random_seq_generator(10, 1), random_seq_generator(10, 2)),
        (random_seq_generator(15, 1), random_seq_generator(20, 2)),
        (random_seq_generator(30, 1), random_seq_generator(13, 2)),
        (random_seq_generator(19, 1), random_seq_generator(13, 2)),
    ]
)
@pytest.mark.parametrize(
    "scoring",
    [scoring for scoring in SCORING]
)
def test_exercise_4i(seq1, seq2, scoring):
    d, p, q = gotoh_forward_correct(seq1, seq2, scoring)
    expected_paths = build_all_traceback_paths_correct(
        seq1, seq2, scoring, d, p, q)
    for traceback_path in expected_paths:
        expected_alignment = build_alignment_correct(seq1, seq2,
                                                     traceback_path)
        actual_alignment = build_alignment(seq1, seq2, traceback_path)
        if actual_alignment != expected_alignment:
            print(
                f"\nFor the Test case:\nS1: {seq1}\nS2: {seq2}\nscoring: {scoring}\npath: {traceback_path}")
            print("Your alignment is:")
            print(f"S1: {actual_alignment[0]}\nS2: {actual_alignment[1]}")
            print("It should be:")
            print(f"S1: {expected_alignment[0]}\nS2: {expected_alignment[1]}")
        assert expected_alignment == actual_alignment





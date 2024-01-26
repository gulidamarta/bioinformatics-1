import pytest

import copy
from exercise_sheet10 import *
from helpers import *


@pytest.fixture
def distance_info1():
    matrix_dist_1 = [
        [0, 3, 12, 12, 9],
        [3, 0, 13, 13, 10],
        [12, 13, 0, 6, 7],
        [12, 13, 6, 0, 7],
        [9, 10, 7, 7, 0]
    ]
    nodes_ = ["a", "b", "c", "d", "e"]
    weight_1 = "wpgma"
    distance_info1 = matrix_dist_1, nodes_, weight_1
    return distance_info1


@pytest.fixture
def distance_info2():
    matrix_dist_2 = [
        [0, 17, 21, 31, 23],
        [17, 0, 30, 34, 21],
        [21, 30, 0, 28, 39],
        [31, 34, 28, 0, 43],
        [23, 21, 39, 43, 0]
    ]
    nodes_ = ["a", "b", "c", "d", "e"]
    weight_1 = "wpgma"
    return matrix_dist_2, nodes_, weight_1


@pytest.fixture
def distance_info3(distance_info1):
    return distance_info1[0], distance_info1[1], "upgma"


@pytest.fixture
def distance_info4(distance_info2):
    return distance_info2[0], distance_info2[1], "upgma"


@pytest.fixture
def distance_info5():
    matrix_dist_2 = [
        [0, 2, 4, 6, 6, 8],
        [2, 0, 4, 6, 6, 8],
        [4, 4, 0, 6, 6, 8],
        [6, 6, 6, 0, 4, 8],
        [6, 6, 6, 4, 0, 8],
        [8, 8, 8, 8, 8, 0],

    ]
    nodes_ = ["a", "b", "c", "d", "e", "f"]
    weight_1 = "upgma"
    return matrix_dist_2, nodes_, weight_1


@pytest.mark.parametrize(
    "distance_info",
    [
        "distance_info1",
        "distance_info2",
        "distance_info3",
        "distance_info4",
    ]
)
def test_exercise_4a(distance_info, request):
    distance_info = request.getfixturevalue(distance_info)
    expected = convert_to_nodes_correct(distance_info)
    actual = convert_to_nodes(distance_info)
    for node in expected:
        assert node in actual


@pytest.mark.parametrize(
    "distance_info",
    [
        "distance_info1",
        "distance_info2",
        "distance_info3",
        "distance_info4",
    ]
)
def test_exercise_4b(distance_info, request):
    distance_info = request.getfixturevalue(distance_info)
    nodes_list = convert_to_nodes_correct(distance_info)
    actual = []
    while len(nodes_list) > 1:
        actual = merge_best_pair(copy.deepcopy(nodes_list))
        nodes_list = merge_best_pair_correct(nodes_list)
        for node in nodes_list:
            assert node in actual
    for node in nodes_list:
        assert node in actual


@pytest.mark.parametrize(
    "distance_info",
    [
        "distance_info1",
        "distance_info2",
        "distance_info3",
        "distance_info4",
        "distance_info5"
    ]
)
def test_exercise_4c(distance_info, request):
    distance_info = request.getfixturevalue(distance_info)
    expected = build_the_tree_correct(distance_info)
    actual = build_the_tree(distance_info)
    assert actual == expected

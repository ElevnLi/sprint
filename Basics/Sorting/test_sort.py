from heap_sort import sort as sort_to_test


def test_in_place_sort():
    l = [2, 1, 3, 5, 4, 7, 6, 8]
    sort_to_test(l)
    assert l == [1, 2, 3, 4, 5, 6, 7, 8]

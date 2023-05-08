from intervals import overlapping_intervals


def test_overlapping_intervals1():
    assert overlapping_intervals((1, 5), (3, 6))

    assert not overlapping_intervals((2, 5), (7, 10))
def test_overlapping_intervals2():
    assert not overlapping_intervals((0,0), (1,4))
def test_overlapping_intervals3():
    assert overlapping_intervals ((0,0), (0,0))
def test_overlapping_intervals4():
    assert overlapping_intervals ((0,1), (0,0))
def test_overlapping_intervals():
    assert overlapping_intervals ((3,3), (0,5))
from src.generators import intersection_generator


def test_intersection_generator():
    generator = intersection_generator([1, 2, 3, 4, 5, 6], [1, 2, 3, 7, 8, 9])
    assert next(generator) == 1
    assert  next(generator) == 2
    assert next(generator) == 3
    assert next(generator) == 4


import pytest
from ..source.LCD import LCD

@pytest.mark.parametrize("num1, num2, expected", [
    (54, 24, 6),
    (48, 18, 6),
    (101, 10, 1),
    (7, 3, 1),
    (20, 8, 4)
])
def test_LCD(num1, num2, expected):
    assert LCD(num1, num2) == expected
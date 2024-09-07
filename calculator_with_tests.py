# calc functions that are going to be tested

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# unit testing the above calc functions
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0
    assert subtract(0, 0) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 10) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, -3) == 2
    assert divide(0, 1) == 0

    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(1, 0)

# To run the tests, add this block
if __name__ == "__main__":
    pytest.main()

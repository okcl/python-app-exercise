import pytest
from app import add, subtract

def test_add():
    assert add(3, 7) == 10
    assert add(-1, 1) == 0
    
def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(1, 1) == 0

if __name__ == '__main__':
    pytest.main()

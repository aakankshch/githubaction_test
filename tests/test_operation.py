from src.math_operations import add,sub


#unit test cases
def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    
def test_sub():
    assert sub(7,3)==4
    assert sub(4,2)==2
    assert sub(3,3)==0
    assert sub(2,3)==-1
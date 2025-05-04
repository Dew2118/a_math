from main import a_math
from pytest_unordered import unordered
def test_a_math():
    assert a_math([],1) == [[(7,7)]]
    assert a_math([],2) == unordered([unordered([(7,6),(7,7)]),unordered([(7,7),(7,8)]),unordered([(6,7),(7,7)]),unordered([(7,7),(8,7)])])
    assert a_math([],3) == unordered([unordered([(7,5),(7,6),(7,7)]),unordered([(7,6),(7,7),(7,8)]),unordered([(7,7),(7,8),(7,9)]),unordered([(5,7),(6,7),(7,7)]),unordered([(6,7),(7,7),(8,7)]),unordered([(7,7),(8,7),(9,7)])])
    
    assert a_math([[(7,5),(7,6),(7,7)]],2) == unordered([unordered([(7,3),(7,4)]),unordered([(5,5),(6,5)]),unordered([(6,5),(8,5)]),unordered([(8,5),(9,5)]),unordered([(5,6),(6,6)]),unordered([(6,6),(8,6)]),unordered([(8,6),(9,6)]),unordered([(5,7),(6,7)]),unordered([(6,7),(8,7)]),unordered([(8,7),(9,7)]),unordered([(7,8),(7,9)])])
    assert a_math([[(5,7),(6,7),(7,7),(8,7),(9,7)]],3) == unordered([unordered([(2,7),(3,7),(4,7)]),unordered([(10,7),(11,7),(12,7)]),unordered([(5,4),(5,5),(5,6)]),unordered([(5,5),(5,6),(5,8)]),unordered([(5,6),(5,8),(5,9)]),unordered([(5,8),(5,9),(5,10)]),unordered([(6,4),(6,5),(6,6)]),unordered([(6,5),(6,6),(6,8)]),unordered([(6,6),(6,8),(6,9)]),unordered([(6,8),(6,9),(6,10)]),unordered([(7,4),(7,5),(7,6)]),unordered([(7,5),(7,6),(7,8)]),unordered([(7,6),(7,8),(7,9)]),unordered([(7,8),(7,9),(7,10)]),unordered([(8,4),(8,5),(8,6)]),unordered([(8,5),(8,6),(8,8)]),unordered([(8,6),(8,8),(8,9)]),unordered([(8,8),(8,9),(8,10)]),unordered([(9,4),(9,5),(9,6)]),unordered([(9,5),(9,6),(9,8)]),unordered([(9,6),(9,8),(9,9)]),unordered([(9,8),(9,9),(9,10)])])
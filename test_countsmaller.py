import countsmaller

def test_1():
    nums = [5,2,6,1]
    output=[2,1,1,0]
    r=countsmaller.count_smaller_numbers(nums)
    assert r==output

def test_2():
    nums = [-1]
    output=[0]
    r=countsmaller.count_smaller_numbers(nums)
    assert r==output

def test_3():
    nums = [-1,-1]
    output=[0,0]
    r=countsmaller.count_smaller_numbers(nums)
    assert r==output

def test_4():
    nums = [9,6,3,0,9]
    output=[3,2,1,0,0]
    r=countsmaller.count_smaller_numbers(nums)
    assert r==output

def test_5():
    nums = [15,18,3,98,63,27,0,0,2,3]
    output=[5, 5, 3, 6, 5, 4, 0, 0, 0, 0]
    r=countsmaller.count_smaller_numbers(nums)
    assert r==output

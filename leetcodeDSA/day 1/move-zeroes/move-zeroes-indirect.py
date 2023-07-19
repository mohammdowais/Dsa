def moveZeroes(nums):
    """
    https://leetcode.com/problems/move-zeroes/
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    

    Example 1:

    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    Example 2:

    Input: nums = [0]
    Output: [0]
    ___________________________________________
     0 1 2 3 4 
    [0,1,0,3,12]    | [2,1,0,3,12]
    [1,0,0,3,12]    ->[1,3,0,0,12]
                                   0 1 2 3 4            
     iteration 1 i = 0 j = 1 ->   [1,0,0,3,12] 
     iteration 2 i = 1 j = 2 ->   [1,0,0,3,12] i = 1
     iteration 3 i = 1 j = 3 ->   [1,3,0,0,12]
     iteration 4 i = 2 j = 4 ->   [1,3,12,0,0]
    loop through the array with i = 0
    compare ith element jth initial value j = 1
    if(ith == 0 & jth !=0 ) swap ith and jth increment ith
    if(ith == 0 and jth == 0) decrement i and continue



    """
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
    iterate through list
    if zero pop it
    append append zero to list

        """
    for n in nums:
        if n == 0:
            nums.remove(n)
            nums.append(0)
        

    print(nums)

moveZeroes([0,1,0,3,12])


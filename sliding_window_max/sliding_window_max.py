'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    max_nums = []

    # create a loop the length of array - the window size; + 1 for range
    for i in range( len( nums ) - k + 1 ):
        # append the max of the nums window slice
        max_nums.append( max( nums[ i : i + k ] ) )
    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

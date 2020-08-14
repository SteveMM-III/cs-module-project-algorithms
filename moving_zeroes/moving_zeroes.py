'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    nums   = []
    zeroes = 0

    for num in arr:
        if num != 0:
            nums.append( num )
        else:
            zeroes += 1

    for i in range( 0, zeroes ):
        nums.append( 0 )
    
    return nums

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
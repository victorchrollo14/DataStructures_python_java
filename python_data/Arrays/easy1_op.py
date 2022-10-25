from array import array


# Implementation 1 passes 96 test cases but its complexity is still O(n**2) - Quadratic 
# so it takes too much time.
def implement1(arr, n, s):
    for i in range(n):
        currentsum = arr[i]

        j = i + 1
        while (j <= n):
            if (currentsum == s):
                print("subarray found:")
                print(f"position of subarray: {i + 1} {j}")
                return i+1, j

            if (currentsum > s or j == n):
                break

            currentsum += arr[j]
            j += 1
        
    return -1,



def subArraySum(arr, n, sum_):

        # Initialize currentSum as
        # value of first element
        # and starting point as 0
        currentSum = arr[0]
        start = 0

        # Add elements one by
        # one to currentSum and
        # if the currentSum exceeds
        # the sum, then remove
        # starting element
        i = 1
        while i <= n:

            # If currentSum exceeds
            # the sum, then remove
            # the starting elements
            while currentSum > sum_ and start < i-1:

                currentSum = currentSum - arr[start]
                start += 1

            # If currentSum becomes
            # equal to sum, then
            # return true
            if currentSum == sum_:
                print("Sum found between indexes")
                print("% d and % d" % (start, i-1))
                return 1

            # Add this element
            # to currentSum
            if i < n:
                currentSum = currentSum + arr[i]
            i += 1

        # If we reach here,
        # then no subarray
        print("No subarray found")
        return 0


# Driver program
if __name__ == '__main__':
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    sum_ = 23

    subArraySum(arr, n, sum_)
    

# def main():
#     pass


# N = 5; S = 10
# arr = array('i', [1, 2, 3, 7, 5])
# ans = implement2(arr, N, S)

# for i in ans:
#     print(i, end=" ")

from array import array
import math

# time complexity of the given code would be (O(n**2) - Quadratic 
# The following algorithm passed only 16 test cases
# It fails when there are repeated elements as a result it does not give the accurate index.

# Function to find a continuous sub-array which adds up to a given number.

# Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
# Output: Sum found between indexes 2 and 4
# Explanation: Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33

class Solution:
    def subArraySum(self,arr, n, s): 
        self.arr = arr
        self.n = n
        self.s = s
        sum = sum1 = 0
        k = 0
        subarray = []
        subarray1 = []
        for i in range(n):
            sum = sum + arr[i]
            subarray.append(arr[i])
            print(f'sum:{sum}')
            if (sum == s):
                print(subarray)
                return arr.index(subarray[0]) + 1, arr.index(subarray[len(subarray) - 1]) + 1

        for i in range(n):
            for j in range(i+1, n):
                sum1 += arr[j]
                subarray1.append(arr[j])
                print(f'sum1: {sum1}')
                if(sum1 == s):
                    print(subarray1)
                    k = 1
                    return arr.index(subarray1[0]) + 1, arr.index(subarray1[len(subarray1) - 1]) + 1
            print()
            sum1 = 0
            subarray1.clear()
            if(k == 1):
                break
        return -1, 


# driver code               
def main():
    T = int(input())
    while(T > 0):

        NS = input().strip().split()
        N = int(NS[0])
        S = int(NS[1])

        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.subArraySum(A, N, S)
        print(ans)
        for i in ans:
            print(i, end=" ")
        
        print()

        T -= 1

if __name__ == "__main__":
    main()



# A = list(map(int, input().split()))
# ob = Solution()
# ans = ob.subArraySum(A, 42, 468)
# for i in ans:
#     print(i, end=" ")




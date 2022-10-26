

class Solution:
    def KthSmallest(self, arr, k):
        temp = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if (arr[i] > arr[j]):
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    
        return arr[k - 1]
    
    def KthSmallest_optimized(self, arr, k):
        i = 0
        temp = 0
        while (i < len(arr) - 1):
            if (arr[i] > arr[i+1]):
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                i = -1
            i+=1
        return arr[k - 1]

        

                
                    



# if __name__ == "__main__":
#     import random
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         arr = list(map(int, input().split()))
#         k = int(input())
#         ob = Solution()
#         print(ob.KthSmallest(arr, 0, n-1, k))

N = 6
arr = [7, 10, 4, 3, 20, 15]
K = 3
ob = Solution()
ans = ob.KthSmallest_optimized(arr, K)
print(ans)

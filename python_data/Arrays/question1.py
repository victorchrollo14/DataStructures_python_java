import array


# sum of subarray
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
            if (sum == s):
                print(subarray)
                return arr.index(subarray[0]) + 1, arr.index(subarray[len(subarray) - 1]) + 1
            for j in range(i+1, n):
                sum1 += arr[j]
                subarray1.append(arr[j])
                if(sum1 == s):
                    print(subarray1)
                    k = 1
                    return arr.index(subarray1[0]) + 1, arr.index(subarray1[len(subarray1) - 1]) + 1
        
            subarray1.clear()
            if(k == 1):
                break
                

               

n = 5
s = 12
arr = array.array('i', [1,2,3,7,5])

obj = Solution()
obj.subArraySum(arr, n, s)
ans = obj.subArraySum(arr, n, s)
for i in ans:
    print(i, end=" ")
print('\n')

n1 = 10
s1 = 15
arr1 = array.array('i', [1,2,3,4,5,6,7,8,9,10])

ob2 = Solution()
ans2 = ob2.subArraySum(arr1, n1, s1)
for i in ans2:
    print(i, end=" ")


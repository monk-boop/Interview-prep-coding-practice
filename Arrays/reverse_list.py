#Problem Statement:
#Given an array, rotate the array to the right by k steps, where k is non-negative.
#Example 1:
#Input: [1,2,3,4,5,6,7] and k = 3
#Output: [5,6,7,1,2,3,4]
#Explanation:
#rotate 1 steps to the right: [7,1,2,3,4,5,6]
#rotate 2 steps to the right: [6,7,1,2,3,4,5]
#rotate 3 steps to the right: [5,6,7,1,2,3,4]
#Example 2:
#Input: [-1,-100,3,99] and k = 2
#Output: [3,99,-1,-100]
#Explanation: 
#rotate 1 steps to the right: [99,-1,-100,3]
#rotate 2 steps to the right: [3,99,-1,-100]
#Note:
#Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
#Could you do it in-place with O(1) extra space? Level: Easy
#Problem Practice Link: https://leetcode.com/problems/rotate-array/
#Companies Asked in: Amazon, Microsoft, Paypal, Goldman sachs, Facebook, Uber, Cisco, Adobe
#Similar Problems:
#1. Rotate List: https://leetcode.com/problems/rotate-list/
#2. Reverse Words in a String II: https://leetcode.com/problems/reverse-words-in-a-string-ii/
####### Naive solution (Approach 1) Time Complexity : O[n*k]
arr = [1,2,3,4,5,6,7]
k = 3

for iteration in range(k):
    temp = arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = temp
    
    print(arr)
        
####### (Approach 2) Time Complexity : O[N]+O(K)    Space Complexity : O(1)
arr = [1,2,3,4,5,6,7]
k = 3
def reverse(arr,start_index,end_index):
    temp = 0
    
    while start_index < end_index:
        temp = arr[start_index]
        arr[start_index] = arr[end_index]
        arr[end_index] = temp
        start_index+=1
        end_index-=1
    
    return arr
    
print(reverse(arr,len(arr)-k,len(arr)-1))
print(reverse(arr,0,len(arr)-k-1))
print(reverse(arr,0,len(arr)-1))

    
    
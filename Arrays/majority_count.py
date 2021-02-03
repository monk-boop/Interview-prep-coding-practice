#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#You may assume that the array is non-empty and the majority element always exist in the array.
#Example 1:
#Input: [3,2,3]
#Output: 3
#Example 2:
#Input: [2,2,1,1,1,2,2]
#Output: 2
#Level: Easy
#Companies Asked in: Amazon, Microsoft, Visa
#Similar Problems:
#1. Majority Element II: https://leetcode.com/problems/majority-element-ii/
#2. Check if a number is majority  Element in a sorted array: https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/
# 1) Brute force method
import math
arr = [2,2,1,1,1,2,2]
num_count = {}
for i in arr:
    if i not in num_count:
        num_count[i] = 1
        
    else:
        num_count[i] += 1
        
        
for i,j in zip(num_count.keys(),num_count.values()):
    if j >= math.ceil(len(arr)/2):
        print(i)
        #Time complexity : O(n); Space Complexity: O(n)
# 2) Optimized method : Boyer-Moore Algorithm [ #Time complexity : O(n)+O(n); Space Complexity: 1]
# Since I want O(n), time complexity, I can iterate through the list only once!
import math
#arr = [2,2,1,1,1,2,2]

def BM_algo(arr):
    count = 1
    m = arr[0]
    for i in arr[1:]:
        if i == m:
            count+=1
        elif i!= m:
            if count == 0:
                m = i
                count = 1
            else:
                count -=1
                
    return m
    
def validate(m,arr):
    count = 0
    for i in arr:
        if i==m:
            count+=1
            
    if count >= len(arr)/2:
        return True
    else:
        return False
        
if __name__=='__main__':
    arr=[3, 3, 4, 2, 4, 4, 2, 4]
    value=BM_algo(arr)
    if(validate(value,arr)):
        print(value)
    else:
        print("majority element not found")
            




    
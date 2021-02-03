'''Problem Statement:

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]

Output: [2,4,3,1]

The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:

1 <= A.length <= 5000

0 <= A[i] <= 5000

Level: Easy

Problem Practice Link: https://leetcode.com/problems/sort-array-by-parity/

Companies Asked in: Cisco, Amazon, VMWare, Oracle, Microsoft'''


arr = [3,1,2,4]
odd = []
even = []
for i in arr:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
    
print(even+odd)

### Solution 2: Swap odd numbers to the end
arr = [3,1,2,4]
j = len(arr)-1
i = 0
while i< j:
    if arr[i] % 2 == 0 or arr[j]%2 ==0:
        arr[i] = arr[i]+arr[j]
        arr[j] = arr[i]-arr[j]
        arr[i] = arr[i]-arr[j]
    j-=1 
    i+=1
    
    
print(arr)
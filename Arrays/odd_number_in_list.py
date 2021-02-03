#Problem Statement:
#Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#Example 1:
#Input: [2,2,1]
#Output: 1
#Example 2:
#Input: [4,1,2,1,2]
#Output: 4
#Level: Easy
#Problem Practice link: https://leetcode.com/problems/single-number/
#Python Executable code: https://onlinegdb.com/SJ1p4B2W8
#Companies Asked in: Amazon, Google, Microsoft, Facebook, Oracle, Adobe, Airbnb
#Similar Problems:
#1. Single Number II: https://leetcode.com/problems/single-number-ii/
#2. Single Number III: https://leetcode.com/problems/single-number-iii/
#3. Missing Number: https://leetcode.com/problems/missing-number/
#4. Find the Duplicate Number: https://leetcode.com/problems/find-the-duplicate-number/

### Again, we will make use of the fact that XOR of a number with itself is 0

arr = [4,1,2,1,2,4,3]

def odd(arr):
    num = 0
    for i in arr:
        num ^= i
        
    return num
    
print(odd(arr))
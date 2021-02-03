# Find the missing number(type : easy; Asked in global analytics for optimized solution(XOR))
#For a given list with numbers from 1 to n(in this case n=10), find the missing number in the list
#Fast solution
a=[1,2,4,3,6,7,9,8,10]
n = len(a)
#Sum of n numbers is N*N+1/2
print((((n+1)/2)*(2+n))-sum(a))
#Space complexity : O(n)
#Drawback: If n is very large, the sum of n numbers (n*(n+1)/2) can give an overflow error, since n+1 could be larger than the largest value
# allowed to be stored in memory
#Faster Solution
a=[1,2,4,3,6,7,9,8,10]

#USing XOR operation, the XOR of the XOR of all numbers upto n and XOR of all numbers in a list will be the missing number
X1 = a[0]
X2 = 1
for i in range(1,len(a)):
    X1^=a[i]
    
for i in range(2,len(a)+2):
    X2^=i
    
print(X1^X2)
'''Find leaders in an array:-

given arr = [8,4,2,3,1,5,4,2]
leaders are 8,5,4,2. This is because the elements on the right of the elements 8 and 5 are smaller than them.
arr2 = [10,6,3,1,7,9]
leaders are 10,9
level: easy
Comapnies asked: leetcode, Barclays, paypal (data science)'''
#Time complexity = O(n) ------> We go from right to left
arr = [8,4,2,3,1,5,4,2]
leaders = []
max_num = 0

for i in range(len(arr)-1,-1,-1):
    if not leaders:
        leaders.append(arr[i])
        max_num = arr[i]
    elif arr[i] > leaders[-1]:
        leaders.append(arr[i])
        max_num = arr[i]
        
print(leaders)
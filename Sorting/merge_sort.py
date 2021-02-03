"""
1. Worst case Time: O(n*lg(n))
   Worst case Space: O(n) for out of space & 
   extra lg(n) stack space for Recursions
2. Perfect for large arrays which can not fit into RAM need to acces from HDD/SSD
3. Introduces Divide & Conquer method(concept used in all Recursive programmes).
Out of place, Stable and Off-line Algorithm
"""

def mergeSort(arr):
    if len(arr)>1: #arrays of length 1 will be accepted
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]
        mergeSort(l)
        mergeSort(r)
        
        i=j=k=0
        
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i+=1
            else:
                arr[k] = r[j]
                j+=1
            k+=1
            
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1
                
 
# Driver program
if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]
 
    mergeSort(array)
 
    print("Sorted array is: ")
    print(array)
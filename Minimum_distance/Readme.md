## Challenge
The distance between two array values is the number
of indices between them. Given a list, find the
minimum distance between any pair of equal elements
in the array. If no such value exists, print no same 
elements are present in the list.\
For Example:

$a=[3,2,1,2,3]$

There are two matching pairs of values: 3 and 2. The indices of 
the 3's are i=0, j=4, so their distance is $d[i,j]=|i-j|=4$.
The indices of the 2's are i=1, j=3, so their distance is $d[i,j]=|i-j|=2$.

## Input format

The input line contains n space-separated integers *a[i]*.
Example:
```
7 1 3 4 1 7
```
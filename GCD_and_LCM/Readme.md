## Challenge
There will be two arrays of integers. Determine all
integers that satisfy the following two conditions:

1. The elements of the first array are all factors of
the integer being considered.
2. The integer being considered is a factor of all
elements of the second array.

These numbers are referred to as being *between 
the two sets*. Determine how many such numbers exist and
print them.

For example:

$a=[2, 4]$

$h2=[16, 32]$

Here, there are three integers that can be called *between
the two sets*: 4, 8, 16.
All the integers in list *a* = [2, 4] are factors of 4, 8, 16.
And all the integers in list *b* = [16, 32] are divisible by 
4, 8, 16. 

Another example:

$a=[2, 6]$

$h2=[24, 36, 48]$

Here, there are two integers that can be called *between
the two sets*: 6, 12.


## Input format

The first line contains n distinct space-separated integers *a[i]* where $0\leq i< n$.
The third line contains m distinct space-separated integers *b[i]* where $0\leq i< m$.


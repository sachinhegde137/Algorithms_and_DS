## Challenge
You have three stacks of cylinders where each cylinder
has the same diameter, but they may vary in height. 
You can change the height of a stack by removing and
discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such 
that all of the stacks are exactly the same height. 
This means you must remove zero or more cylinders from
the top of zero or more of the three stacks until 
they are all the same height, then return the height.\
For Example:

$h1=[3, 2, 1, 1, 1]$

$h2=[4, 3, 2]$

$h3=[1, 1, 4, 1]$

There are *5,3,4* cylinders in the three stacks, with
their heights in the three arrays. Remove the top 1 
cylinder from *h1* (heights = [3])  and *h2* 
(heights = [4]), and top 2 cylinders from *h3* 
(heights = [1, 1]), so that the three stacks all are
5 units tall. Display 5 as the answer.

## Input format
- The first line contains *n1* space-separated 
integers, the cylinder heights in stack 1. The 
first element is the top cylinder of the stack.
- The second line contains *n2* space-separated 
integers, the cylinder heights in stack 2. The first
element is the top cylinder of the stack.
- The third line contains *n3* space-separated 
integers, the cylinder heights in stack 3. The 
first element is the top cylinder of the stack.


## Sample Input
```
STDIN       Function
-----       --------
3 2 1 1 1   h1 = [3, 2, 1, 1, 1]
4 3 2       h2 = [4, 3, 2]
1 1 4 1     h3 = [1, 1, 4, 1]
```

## Sample output
```
5
```


### Additional example:

$h1=[1, 2, 1, 1]$

$h2=[1, 1, 2]$

$h3=[1, 1]$

There are *4,3,2* cylinders in the three stacks, 
with their heights in the three arrays. Remove the 
top 2 cylinders from *h1* (heights = [1, 2]) and 
from *h2* (heights = [1, 1]) so that the three 
stacks all are 2 units tall. Return 2 as the answer.

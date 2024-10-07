## Challenge

Given an array of strings of digits, try to find the
occurrence of a given pattern of digits. In the grid 
and pattern arrays, each string represents a row in the
grid. For example, consider the following grid:
```
1234567890  
0987654321  
1111111111  
1111111111  
2222222222 
```
The pattern array is:
```
876543  
111111  
111111
```
The pattern begins at the second row and the third 
column of the grid and continues in the following
two rows. The pattern is said to be present in the
grid. The program must print if the pattern exists 
or not in the grid. 

## Input format

The first line contains two space-separated integers *R*
and *C*, the number of rows in the search grid *G* and the
length of each row string.

This is followed by *R* lines, each with a string of
*C* digits that represent the grid *G*.

The following line contains two space-separated 
integers, *r* and *c*, the number of rows in the 
pattern grid *P* and the length of each pattern 
row string. This is followed by *r* lines, each with a
string of *c* digits that represent the pattern grid *P*.

## Sample Input
```
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
```
## Sample Output
```
The pattern exists in the grid
```

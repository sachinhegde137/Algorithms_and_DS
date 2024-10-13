## Binary Search Tree
A Binary Search Tree (BST) is a data structure used in
computer science for organizing and storing data in 
a sorted manner. Each node in a BST has at most two 
children, a left child and a right child.The values
of the left sub-tree are less than the root node and
the values of the right sub-tree are greater than the
value of the root node. 

#### Properties of BST
- The left side of a node only has smaller values.
- The right side of a node only has bigger values.
- Both the left and right sides follow the same
rule, forming a smaller binary search tree.

An example of a binary search tree is shown below.
![BST](bst.png)

In this binary tree

- Root node: 8
- Left subtree (3): values < 8
- Right subtree (10): values > 8
- Each subtree maintains the same rule, with values
relative to their respective roots.

## Task
You are given a list of integers, with the first element pointing 
the rooot of the binary search tree. 
Insert the values into their appropriate position 
in the binary search tree and return the root of the 
updated binary tree. 
https://leetcode.com/problems/increasing-order-search-tree

## 897. Increasing Order Search Tree

<div><p>Given a binary search tree, rearrange the tree in <strong>in-order</strong> so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.</p>
<pre><strong>Example 1:</strong>
<strong>Input:</strong> [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

<strong>Output:</strong> [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  </pre>
<p><strong>Note:</strong></p>
<ol>
<li>The number of nodes in the given tree will be between 1 and 100.</li>
<li>Each node will have a unique integer value from 0 to 1000.</li>
</ol>
</div>

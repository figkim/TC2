https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

## 235. Lowest Common Ancestor of a Binary Search Tree

<div><p>Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.</p>
<p>According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow <b>a node to be a descendant of itself</b>).”</p>
<p>Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]</p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 200px; height: 190px;"/>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
<strong>Output:</strong> 6
<strong>Explanation: </strong>The LCA of nodes <code>2</code> and <code>8</code> is <code>6</code>.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
<strong>Output:</strong> 2
<strong>Explanation: </strong>The LCA of nodes <code>2</code> and <code>4</code> is <code>2</code>, since a node can be a descendant of itself according to the LCA definition.
</pre>
<p> </p>
<p><strong>Note:</strong></p>
<ul>
<li>All of the nodes' values will be unique.</li>
<li>p and q are different and both values will exist in the BST.</li>
</ul>
</div>

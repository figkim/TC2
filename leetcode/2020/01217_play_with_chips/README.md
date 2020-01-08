https://leetcode.com/problems/play-with-chips

## 1217. Play with Chips

<div><p>There are some chips, and the i-th chip is at position <code>chips[i]</code>.</p>
<p>You can perform any of the two following types of moves <strong>any number of times</strong> (possibly zero) <strong>on any chip</strong>:</p>
<ul>
<li>Move the <code>i</code>-th chip by 2 units to the left or to the right with a cost of <strong>0</strong>.</li>
<li>Move the <code>i</code>-th chip by 1 unit to the left or to the right with a cost of <strong>1</strong>.</li>
</ul>
<p>There can be two or more chips at the same position initially.</p>
<p>Return the minimum cost needed to move all the chips to the same position (any position).</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> chips = [1,2,3]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Second chip will be moved to positon 3 with cost 1. First chip will be moved to position 3 with cost 0. Total cost is 1.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> chips = [2,2,2,3,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Both fourth and fifth chip will be moved to position two with cost 1. Total minimum cost will be 2.
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= chips.length &lt;= 100</code></li>
<li><code>1 &lt;= chips[i] &lt;= 10^9</code></li>
</ul>
</div>

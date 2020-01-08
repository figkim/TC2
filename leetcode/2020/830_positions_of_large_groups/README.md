https://leetcode.com/problems/positions-of-large-groups

## 830. Positions of Large Groups

<div><p>In a string <code>S</code> of lowercase letters, these letters form consecutive groups of the same character.</p>
<p>For example, a string like <code>S = "abbxxxxzyy"</code> has the groups <code>"a"</code>, <code>"bb"</code>, <code>"xxxx"</code>, <code>"z"</code> and <code>"yy"</code>.</p>
<p>Call a group <em>large</em> if it has 3 or more characters.  We would like the starting and ending positions of every large group.</p>
<p>The final answer should be in lexicographic order.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>"abbxxxxzzy"
<strong>Output: </strong>[[3,6]]
<strong>Explanation</strong>: <code>"xxxx" is the single </code>large group with starting  3 and ending positions 6.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>"abc"
<strong>Output: </strong>[]
<strong>Explanation</strong>: We have "a","b" and "c" but no large group.
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input: </strong>"abcdddeeeeaabbbcd"
<strong>Output: </strong>[[3,5],[6,9],[12,14]]</pre>
<p> </p>
<p><strong>Note: </strong> <code>1 &lt;= S.length &lt;= 1000</code></p>
</div>

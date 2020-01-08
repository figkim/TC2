https://leetcode.com/problems/string-compression

## 443. String Compression

<div><p>Given an array of characters, compress it <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank"><b>in-place</b></a>.</p>
<p>The length after compression must always be smaller than or equal to the original array.</p>
<p>Every element of the array should be a <b>character</b> (not int) of length 1.</p>
<p>After you are done <b>modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a></b>, return the new length of the array.</p>
 

<p><b>Follow up:</b><br/>
Could you solve it using only O(1) extra space?</p>
 

<p><b>Example 1:</b></p>
<pre><b>Input:</b>
["a","a","b","b","c","c","c"]

<b>Output:</b>
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

<b>Explanation:</b>
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
</pre>
<p> </p>
<p><b>Example 2:</b></p>
<pre><b>Input:</b>
["a"]

<b>Output:</b>
Return 1, and the first 1 characters of the input array should be: ["a"]

<b>Explanation:</b>
Nothing is replaced.
</pre>
<p> </p>
<p><b>Example 3:</b></p>
<pre><b>Input:</b>
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

<b>Output:</b>
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

<b>Explanation:</b>
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
</pre>
<p> </p>
<p><b>Note:</b></p>
<ol>
<li>All characters have an ASCII value in <code>[35, 126]</code>.</li>
<li><code>1 &lt;= len(chars) &lt;= 1000</code>.</li>
</ol>
</div>

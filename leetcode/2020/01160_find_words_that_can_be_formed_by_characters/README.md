https://leetcode.com/problems/find-words-that-can-be-formed-by-characters

## 1160. Find Words That Can Be Formed by Characters

<div><p>You are given an array of strings <code>words</code> and a string <code>chars</code>.</p>
<p>A string is <em>good</em> if it can be formed by characters from <code>chars</code> (each character can only be used once).</p>
<p>Return the sum of lengths of all good strings in <code>words</code>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>words = <span id="example-input-1-1">["cat","bt","hat","tree"]</span>, chars = <span id="example-input-1-2">"atach"</span>
<strong>Output: </strong><span id="example-output-1">6</span>
<strong>Explanation: </strong>
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>words = <span id="example-input-2-1">["hello","world","leetcode"]</span>, chars = <span id="example-input-2-2">"welldonehoneyr"</span>
<strong>Output: </strong><span id="example-output-2">10</span>
<strong>Explanation: </strong>
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
</pre>
<p> </p>
<p><span><strong>Note:</strong></span></p>
<ol>
<li><code>1 &lt;= words.length &lt;= 1000</code></li>
<li><code>1 &lt;= words[i].length, chars.length &lt;= 100</code></li>
<li>All strings contain lowercase English letters only.</li>
</ol></div>

https://leetcode.com/problems/greatest-common-divisor-of-strings

## 1071. Greatest Common Divisor of Strings

<div><p>For strings <code>S</code> and <code>T</code>, we say "<code>T</code> divides <code>S</code>" if and only if <code>S = T + ... + T</code>  (<code>T</code> concatenated with itself 1 or more times)</p>
<p>Return the largest string <code>X</code> such that <code>X</code> divides <font face="monospace">str1</font> and <code>X</code> divides <font face="monospace">str2</font>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>str1 = <span id="example-input-1-1">"ABCABC"</span>, str2 = <span id="example-input-1-2">"ABC"</span>
<strong>Output: </strong><span id="example-output-1">"ABC"</span>
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>str1 = <span id="example-input-2-1">"ABABAB"</span>, str2 = <span id="example-input-2-2">"ABAB"</span>
<strong>Output: </strong><span id="example-output-2">"AB"</span>
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input: </strong>str1 = <span id="example-input-3-1">"LEET"</span>, str2 = <span id="example-input-3-2">"CODE"</span>
<strong>Output: </strong><span id="example-output-3">""</span>
</pre>
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= str1.length &lt;= 1000</code></li>
<li><code>1 &lt;= str2.length &lt;= 1000</code></li>
<li><code>str1[i]</code> and <code>str2[i]</code> are English uppercase letters.</li>
</ol>
</div>

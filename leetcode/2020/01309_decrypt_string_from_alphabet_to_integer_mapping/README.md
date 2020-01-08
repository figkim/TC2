https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping

## 1309. Decrypt String from Alphabet to Integer Mapping

<div><p>Given a string <code>s</code> formed by digits (<code>'0'</code> - <code>'9'</code>) and <code>'#'</code> . We want to map <code>s</code> to English lowercase characters as follows:</p>
<ul>
<li>Characters (<code>'a'</code> to <code>'i')</code> are represented by (<code>'1'</code> to <code>'9'</code>) respectively.</li>
<li>Characters (<code>'j'</code> to <code>'z')</code> are represented by (<code>'10#'</code> to <code>'26#'</code>) respectively. </li>
</ul>
<p>Return the string formed after mapping.</p>
<p>It's guaranteed that a unique mapping will always exist.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "10#11#12"
<strong>Output:</strong> "jkab"
<strong>Explanation:</strong> "j" -&gt; "10#" , "k" -&gt; "11#" , "a" -&gt; "1" , "b" -&gt; "2".
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "1326#"
<strong>Output:</strong> "acz"
</pre>
<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "25#"
<strong>Output:</strong> "y"
</pre>
<p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
<strong>Output:</strong> "abcdefghijklmnopqrstuvwxyz"
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 &lt;= s.length &lt;= 1000</code></li>
<li><code>s[i]</code> only contains digits letters (<code>'0'</code>-<code>'9'</code>) and <code>'#'</code> letter.</li>
<li><code>s</code> will be valid string such that mapping is always possible.</li>
</ul></div>

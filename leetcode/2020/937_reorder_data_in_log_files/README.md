https://leetcode.com/problems/reorder-data-in-log-files

## 937. Reorder Data in Log Files

<div><p>You have an array of <code>logs</code>.  Each log is a space delimited string of words.</p>
<p>For each log, the first word in each log is an alphanumeric <em>identifier</em>.  Then, either:</p>
<ul>
<li>Each word after the identifier will consist only of lowercase letters, or;</li>
<li>Each word after the identifier will consist only of digits.</li>
</ul>
<p>We will call these two varieties of logs <em>letter-logs</em> and <em>digit-logs</em>.  It is guaranteed that each log has at least one word after its identifier.</p>
<p>Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.</p>
<p>Return the final order of the logs.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
<strong>Output:</strong> ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
</pre>
<p> </p>
<p><strong>Constraints:</strong></p>
<ol>
<li><code>0 &lt;= logs.length &lt;= 100</code></li>
<li><code>3 &lt;= logs[i].length &lt;= 100</code></li>
<li><code>logs[i]</code> is guaranteed to have an identifier, and a word after the identifier.</li>
</ol>
</div>

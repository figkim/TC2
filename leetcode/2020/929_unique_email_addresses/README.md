https://leetcode.com/problems/unique-email-addresses

## 929. Unique Email Addresses

<div><p>Every email consists of a local name and a domain name, separated by the @ sign.</p>
<p>For example, in <code>alice@leetcode.com</code>, <code>alice</code> is the local name, and <code>leetcode.com</code> is the domain name.</p>
<p>Besides lowercase letters, these emails may contain <code>'.'</code>s or <code>'+'</code>s.</p>
<p>If you add periods (<code>'.'</code>) between some characters in the <strong>local name</strong> part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, <code>"alice.z@leetcode.com"</code> and <code>"alicez@leetcode.com"</code> forward to the same email address.  (Note that this rule does not apply for domain names.)</p>
<p>If you add a plus (<code>'+'</code>) in the <strong>local name</strong>, everything after the first plus sign will be <strong>ignored</strong>. This allows certain emails to be filtered, for example <code>m.y+name@email.com</code> will be forwarded to <code>my@email.com</code>.  (Again, this rule does not apply for domain names.)</p>
<p>It is possible to use both of these rules at the same time.</p>
<p>Given a list of <code>emails</code>, we send one email to each address in the list.  How many different addresses actually receive mails? </p>
<p> </p>
<div>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong><span id="example-input-1-1">["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong><span>Explanation:</span></strong><span> "</span><span id="example-input-1-1">testemail@leetcode.com" and "testemail@lee.tcode.com" </span>actually receive mails
</pre>
<p> </p>
<p><strong>Note:</strong></p>
<ul>
<li><code>1 &lt;= emails[i].length &lt;= 100</code></li>
<li><code>1 &lt;= emails.length &lt;= 100</code></li>
<li>Each <code>emails[i]</code> contains exactly one <code>'@'</code> character.</li>
<li>All local and domain names are non-empty.</li>
<li>Local names do not start with a <code>'+'</code> character.</li>
</ul>
</div>
</div>

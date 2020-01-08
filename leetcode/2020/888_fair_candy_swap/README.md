https://leetcode.com/problems/fair-candy-swap

## 888. Fair Candy Swap

<div><p>Alice and Bob have candy bars of different sizes: <code>A[i]</code> is the size of the <code>i</code>-th bar of candy that Alice has, and <code>B[j]</code> is the size of the <code>j</code>-th bar of candy that Bob has.</p>
<p>Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (<em>The total amount of candy a person has is the sum of the sizes of candy bars they have.</em>)</p>
<p>Return an integer array <code>ans</code> where <code>ans[0]</code> is the size of the candy bar that Alice must exchange, and <code>ans[1]</code> is the size of the candy bar that Bob must exchange.</p>
<p>If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.</p>
<p> </p>
<div>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>A = <span id="example-input-1-1">[1,1]</span>, B = <span id="example-input-1-2">[2,2]</span>
<strong>Output: </strong><span id="example-output-1">[1,2]</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>A = <span id="example-input-2-1">[1,2]</span>, B = <span id="example-input-2-2">[2,3]</span>
<strong>Output: </strong><span id="example-output-2">[1,2]</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre><strong>Input: </strong>A = <span id="example-input-3-1">[2]</span>, B = <span id="example-input-3-2">[1,3]</span>
<strong>Output: </strong><span id="example-output-3">[2,3]</span>
</pre>
<div>
<p><strong>Example 4:</strong></p>
<pre><strong>Input: </strong>A = <span id="example-input-4-1">[1,2,5]</span>, B = <span id="example-input-4-2">[2,4]</span>
<strong>Output: </strong><span id="example-output-4">[5,4]</span>
</pre>
<p> </p>
<p><strong><span>Note:</span></strong></p>
<ul>
<li><span><code>1 &lt;= A.length &lt;= 10000</code></span></li>
<li><span><code>1 &lt;= B.length &lt;= 10000</code></span></li>
<li><code><span>1 &lt;= A[i] &lt;= 100000</span></code></li>
<li><code><span>1 &lt;= B[i] &lt;= 100000</span></code></li>
<li>It is guaranteed that Alice and Bob have different total amounts of candy.</li>
<li>It is guaranteed there exists an answer.</li>
</ul>
</div>
</div>
</div>
</div>
</div>

https://leetcode.com/problems/flower-planting-with-no-adjacent

## 1042. Flower Planting With No Adjacent

<div><p>You have <code>N</code> gardens, labelled <code>1</code> to <code>N</code>.  In each garden, you want to plant one of 4 types of flowers.</p>
<p><code>paths[i] = [x, y]</code> describes the existence of a bidirectional path from garden <code>x</code> to garden <code>y</code>.</p>
<p>Also, there is no garden that has more than 3 paths coming into or leaving it.</p>
<p>Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.</p>
<p>Return <strong>any</strong> such a choice as an array <code>answer</code>, where <code>answer[i]</code> is the type of flower planted in the <code>(i+1)</code>-th garden.  The flower types are denoted <font face="monospace">1</font>, <font face="monospace">2</font>, <font face="monospace">3</font>, or <font face="monospace">4</font>.  It is guaranteed an answer exists.</p>
<p> </p>
<div>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>N = <span id="example-input-1-1">3</span>, paths = <span id="example-input-1-2">[[1,2],[2,3],[3,1]]</span>
<strong>Output: </strong><span id="example-output-1">[1,2,3]</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>N = <span id="example-input-2-1">4</span>, paths = <span id="example-input-2-2">[[1,2],[3,4]]</span>
<strong>Output: </strong><span id="example-output-2">[1,2,1,2]</span>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre><strong>Input: </strong>N = <span id="example-input-3-1">4</span>, paths = <span id="example-input-3-2">[[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]</span>
<strong>Output: </strong><span id="example-output-3">[1,2,3,4]</span>
</pre>
<p> </p>
<p><strong><span>Note:</span></strong></p>
<ul>
<li><code><span>1 &lt;= N &lt;= 10000</span></code></li>
<li><code><span>0 &lt;= paths.size &lt;= 20000</span></code></li>
<li>No garden has 4 or more paths coming into or leaving it.</li>
<li>It is guaranteed an answer exists.</li>
</ul>
</div>
</div>
</div></div>

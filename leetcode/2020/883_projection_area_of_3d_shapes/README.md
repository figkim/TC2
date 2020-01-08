https://leetcode.com/problems/projection-area-of-3d-shapes

## 883. Projection Area of 3D Shapes

<div><p>On a <code>N * N</code> grid, we place some <code>1 * 1 * 1 </code>cubes that are axis-aligned with the x, y, and z axes.</p>
<p>Each value <code>v = grid[i][j]</code> represents a tower of <code>v</code> cubes placed on top of grid cell <code>(i, j)</code>.</p>
<p>Now we view the <em>projection</em> of these cubes onto the xy, yz, and zx planes.</p>
<p>A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane. </p>
<p>Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.</p>
<p>Return the total area of all three projections.</p>
<p> </p>
<div>
<ul>
</ul>
</div>
<div>
<div>
<ul>
</ul>
</div>
</div>
<div>
<div>
<div>
<div>
<ul>
</ul>
</div>
</div>
</div>
</div>
<div>
<div>
<div>
<div>
<div>
<div>
<div>
<div>
<ul>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong><span id="example-input-1-1">[[2]]</span>
<strong>Output: </strong><span id="example-output-1">5</span>
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong><span id="example-input-2-1">[[1,2],[3,4]]</span>
<strong>Output: </strong><span id="example-output-2">17</span>
<strong>Explanation: </strong>
Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/02/shadow.png" style="width: 749px; height: 200px;"/>
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre><strong>Input: </strong><span id="example-input-3-1">[[1,0],[0,2]]</span>
<strong>Output: </strong><span id="example-output-3">8</span>
</pre>
<div>
<p><strong>Example 4:</strong></p>
<pre><strong>Input: </strong><span id="example-input-4-1">[[1,1,1],[1,0,1],[1,1,1]]</span>
<strong>Output: </strong><span id="example-output-4">14</span>
</pre>
<div>
<p><strong>Example 5:</strong></p>
<pre><strong>Input: </strong><span id="example-input-5-1">[[2,2,2],[2,1,2],[2,2,2]]</span>
<strong>Output: </strong><span id="example-output-5">21</span>
</pre>
<p> </p>
<div>
<div>
<div>
<p><span><strong>Note:</strong></span></p>
<ul>
<li><code>1 &lt;= grid.length = grid[0].length &lt;= 50</code></li>
<li><code>0 &lt;= grid[i][j] &lt;= 50</code></li>
</ul>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>

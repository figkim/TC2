https://leetcode.com/problems/long-pressed-name

## 925. Long Pressed Name

<div><p>Your friend is typing his <code>name</code> into a keyboard.  Sometimes, when typing a character <code>c</code>, the key might get <em>long pressed</em>, and the character will be typed 1 or more times.</p>
<p>You examine the <code>typed</code> characters of the keyboard.  Return <code>True</code> if it is possible that it was your friends name, with some characters (possibly none) being long pressed.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>name = <span id="example-input-1-1">"alex"</span>, typed = <span id="example-input-1-2">"aaleex"</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation: </strong>'a' and 'e' in 'alex' were long pressed.
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>name = <span id="example-input-2-1">"saeed"</span>, typed = <span id="example-input-2-2">"ssaaedd"</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation: </strong>'e' must have been pressed twice, but it wasn't in the typed output.
</pre>
<div>
<p><strong>Example 3:</strong></p>
<pre><strong>Input: </strong>name = <span id="example-input-3-1">"leelee"</span>, typed = <span id="example-input-3-2">"lleeelee"</span>
<strong>Output: </strong><span id="example-output-3">true</span>
</pre>
<div>
<p><strong>Example 4:</strong></p>
<pre><strong>Input: </strong>name = <span id="example-input-4-1">"laiden"</span>, typed = <span id="example-input-4-2">"laiden"</span>
<strong>Output: </strong><span id="example-output-4">true</span>
<strong>Explanation: </strong>It's not necessary to long press any character.
</pre>
<p> </p>
</div>
</div>
</div>
<p><strong>Note:</strong></p>
<ol>
<li><code>name.length &lt;= 1000</code></li>
<li><code>typed.length &lt;= 1000</code></li>
<li>The characters of <code>name</code> and <code>typed</code> are lowercase letters.</li>
</ol>
<div>
<p> </p>
<div>
<div>
<div> </div>
</div>
</div>
</div></div>

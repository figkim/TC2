https://leetcode.com/problems/divisor-game

## 1025. Divisor Game

<div><p>Alice and Bob take turns playing a game, with Alice starting first.</p>
<p>Initially, there is a number <code>N</code> on the chalkboard.  On each player's turn, that player makes a <em>move</em> consisting of:</p>
<ul>
<li>Choosing any <code>x</code> with <code>0 &lt; x &lt; N</code> and <code>N % x == 0</code>.</li>
<li>Replacing the number <code>N</code> on the chalkboard with <code>N - x</code>.</li>
</ul>
<p>Also, if a player cannot make a move, they lose the game.</p>
<p>Return <code>True</code> if and only if Alice wins the game, assuming both players play optimally.</p>
<p> </p>
<ol>
</ol>
<div>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong><span id="example-input-1-1">2</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation:</strong> Alice chooses 1, and Bob has no more moves.
</pre>
<div>
<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong><span id="example-input-2-1">3</span>
<strong>Output: </strong><span id="example-output-2">false</span>
<strong>Explanation:</strong> Alice chooses 1, Bob chooses 1, and Alice has no more moves.
</pre>
<p> </p>
<p><strong>Note:</strong></p>
<ol>
<li><code>1 &lt;= N &lt;= 1000</code></li>
</ol>
</div>
</div></div>

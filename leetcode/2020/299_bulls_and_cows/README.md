https://leetcode.com/problems/bulls-and-cows

## 299. Bulls and Cows

<div><p>You are playing the following <a href="https://en.wikipedia.org/wiki/Bulls_and_Cows" target="_blank">Bulls and Cows</a> game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.</p>
<p>Write a function to return a hint according to the secret number and friend's guess, use <code>A</code> to indicate the bulls and <code>B</code> to indicate the cows. </p>
<p>Please note that both secret number and friend's guess may contain duplicate digits.</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> secret = "1807", guess = "7810"

<strong>Output:</strong> "1A3B"

<strong>Explanation:</strong> <code>1</code><span style='font-family: sans-serif, Arial, Verdana, "Trebuchet MS";'> bull and </span><code>3</code><span style='font-family: sans-serif, Arial, Verdana, "Trebuchet MS";'> cows. The bull is </span><code>8</code><span style='font-family: sans-serif, Arial, Verdana, "Trebuchet MS";'>, the cows are </span><code>0</code><span style='font-family: sans-serif, Arial, Verdana, "Trebuchet MS";'>, </span><code>1</code><span style='font-family: sans-serif, Arial, Verdana, "Trebuchet MS";'> and </span><code>7<font face="sans-serif, Arial, Verdana, Trebuchet MS">.</font></code></pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> secret = "1123", guess = "0111"

<strong>Output:</strong> "1A1B"

<strong>Explanation: </strong>The 1st <code>1 </code><span style='font-family: sans-serif, Arial, Verdana, "Trebuchet MS";'>in friend's guess is a bull, the 2nd or 3rd </span><code>1</code><span style='font-family: sans-serif, Arial, Verdana, "Trebuchet MS";'> is a cow</span><span style='font-family: sans-serif, Arial, Verdana, "Trebuchet MS";'>.</span></pre>
<p><strong>Note: </strong>You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.</p></div>

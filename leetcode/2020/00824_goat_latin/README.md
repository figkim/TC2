https://leetcode.com/problems/goat-latin

## 824. Goat Latin

<div><p>A sentence <code>S</code> is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.</p>
<p>We would like to convert the sentence to "<em>Goat Latin"</em> (a made-up language similar to Pig Latin.)</p>
<p>The rules of Goat Latin are as follows:</p>
<ul>
<li>If a word begins with a vowel (a, e, i, o, or u), append <code>"ma"</code> to the end of the word.<br/>
	For example, the word 'apple' becomes 'applema'.<br/>
	 </li>
<li>If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add <code>"ma"</code>.<br/>
	For example, the word <code>"goat"</code> becomes <code>"oatgma"</code>.<br/>
	 </li>
<li>Add one letter <code>'a'</code> to the end of each word per its word index in the sentence, starting with 1.<br/>
	For example, the first word gets <code>"a"</code> added to the end, the second word gets <code>"aa"</code> added to the end and so on.</li>
</ul>
<p>Return the final sentence representing the conversion from <code>S</code> to Goat Latin. </p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input: </strong>"I speak Goat Latin"
<strong>Output: </strong>"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
</pre>
<p><strong>Example 2:</strong></p>
<pre><strong>Input: </strong>"The quick brown fox jumped over the lazy dog"
<strong>Output: </strong>"heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
</pre>
<p> </p>
<p>Notes:</p>
<ul>
<li><code>S</code> contains only uppercase, lowercase and spaces. Exactly one space between each word.</li>
<li><code>1 &lt;= S.length &lt;= 150</code>.</li>
</ul>
</div>

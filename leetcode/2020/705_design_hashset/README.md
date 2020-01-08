https://leetcode.com/problems/design-hashset

## 705. Design HashSet

<div><p>Design a HashSet without using any built-in hash table libraries.</p>
<p>To be specific, your design should include these functions:</p>
<ul>
<li><code>add(value)</code>: Insert a value into the HashSet. </li>
<li><code>contains(value)</code> : Return whether the value exists in the HashSet or not.</li>
<li><code>remove(value)</code>: Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.</li>
</ul>
<p><br/>
<strong>Example:</strong></p>
<pre>MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)
</pre>
<p><br/>
<strong>Note:</strong></p>
<ul>
<li>All values will be in the range of <code>[0, 1000000]</code>.</li>
<li>The number of operations will be in the range of <code>[1, 10000]</code>.</li>
<li>Please do not use the built-in HashSet library.</li>
</ul>
</div>

https://leetcode.com/problems/kth-largest-element-in-a-stream

## 703. Kth Largest Element in a Stream

<div><p>Design a class to find the <strong>k</strong>th largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.</p>
<p>Your <code>KthLargest</code> class will have a constructor which accepts an integer <code>k</code> and an integer array <code>nums</code>, which contains initial elements from the stream. For each call to the method <code>KthLargest.add</code>, return the element representing the kth largest element in the stream.</p>
<p><strong>Example:</strong></p>
<pre>int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
</pre>
<p><strong>Note: </strong><br/>
You may assume that <code>nums</code>' length ≥ <code>k-1</code> and <code>k</code> ≥ 1.</p>
</div>

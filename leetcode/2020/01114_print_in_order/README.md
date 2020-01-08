https://leetcode.com/problems/print-in-order

## 1114. Print in Order

<div><p>Suppose we have a class:</p>
<pre>public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
</pre>
<p>The same instance of <code>Foo</code> will be passed to three different threads. Thread A will call <code>first()</code>, thread B will call <code>second()</code>, and thread C will call <code>third()</code>. Design a mechanism and modify the program to ensure that <code>second()</code> is executed after <code>first()</code>, and <code>third()</code> is executed after <code>second()</code>.</p>
<p> </p>
<p><strong>Example 1:</strong></p>
<pre><b>Input:</b> [1,2,3]
<b>Output:</b> "firstsecondthird"
<strong>Explanation:</strong> There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
</pre>
<p><strong>Example 2:</strong></p>
<pre><b>Input:</b> [1,3,2]
<b>Output:</b> "firstsecondthird"
<strong>Explanation:</strong> The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.</pre>
<p> </p>
<p><strong>Note:</strong></p>
<p>We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seems to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.</p>
</div>

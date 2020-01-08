https://leetcode.com/problems/customers-who-never-order

## 183. Customers Who Never Order

<div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg class="icon__3Su4" height="1em" viewbox="0 0 24 24" width="1em"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z" fill-rule="evenodd"></path></svg></a></div>
<div><p>Suppose that a website contains two tables, the <code>Customers</code> table and the <code>Orders</code> table. Write a SQL query to find all customers who never order anything.</p>
<p>Table: <code>Customers</code>.</p>
<pre>+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
</pre>
<p>Table: <code>Orders</code>.</p>
<pre>+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
</pre>
<p>Using the above tables as example, return the following:</p>
<pre>+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
</pre>
</div>

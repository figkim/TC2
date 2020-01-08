https://leetcode.com/problems/reformat-department-table

## 1179. Reformat Department Table

<div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg class="icon__3Su4" height="1em" viewbox="0 0 24 24" width="1em"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z" fill-rule="evenodd"></path></svg></a></div>
<div><p>Table: <code>Department</code></p>
<pre>+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| revenue       | int     |
| month         | varchar |
+---------------+---------+
(id, month) is the primary key of this table.
The table has information about the revenue of each department per month.
The month has values in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"].
</pre>
<p> </p>
<p>Write an SQL query to reformat the table such that there is a department id column and a revenue column <strong>for each month</strong>.</p>
<p>The query result format is in the following example:</p>
<pre>Department table:
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+

Result table:
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+

Note that the result table has 13 columns (1 for the department id + 12 for the months).
</pre>
</div>

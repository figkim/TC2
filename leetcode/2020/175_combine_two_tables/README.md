https://leetcode.com/problems/combine-two-tables

## 175. Combine Two Tables

<div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg class="icon__3Su4" height="1em" viewbox="0 0 24 24" width="1em"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z" fill-rule="evenodd"></path></svg></a></div>
<div><p>Table: <code>Person</code></p>
<pre>+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
</pre>
<p>Table: <code>Address</code></p>
<pre>+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.
</pre>
<p> </p>
<p>Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:</p>
<pre>FirstName, LastName, City, State
</pre>
</div>

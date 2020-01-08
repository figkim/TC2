https://leetcode.com/problems/rising-temperature

## 197. Rising Temperature

<div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg class="icon__3Su4" height="1em" viewbox="0 0 24 24" width="1em"><path d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z" fill-rule="evenodd"></path></svg></a></div>
<div><p>Given a <code>Weather</code> table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.</p>
<pre>+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
</pre>
<p>For example, return the following Ids for the above <code>Weather</code> table:</p>
<pre>+----+
| Id |
+----+
|  2 |
|  4 |
+----+
</pre>
</div>

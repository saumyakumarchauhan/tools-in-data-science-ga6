import duckdb

# Step 1: Connect to DuckDB (no need to create database file)
con = duckdb.connect()

# Step 2: Run the query on the Parquet files
query = '''
SELECT
    corr(c.budget, r.total_revenue) AS correlation
FROM 'campaigns.parquet' c
JOIN (
    SELECT
        campaign_id,
        SUM(revenue) AS total_revenue
    FROM 'performance_metrics.parquet'
    WHERE TRY_CAST(metric_date AS DATE) >= DATE '2025-04-26'
    GROUP BY campaign_id
) r
ON c.campaign_id = r.campaign_id
WHERE c.channel = 'Email' AND c.budget >= 25000;
'''

# Step 3: Execute and show result
result = con.sql(query).fetchall()
print("Correlation between budget and total revenue:", round(result[0][0], 3))

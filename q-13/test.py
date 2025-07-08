import duckdb

con = duckdb.connect()

# Preview the first few rows to understand structure
df = con.sql("SELECT * FROM '2015_flights.parquet' LIMIT 5").df()
print(df.columns)
print(df.head())

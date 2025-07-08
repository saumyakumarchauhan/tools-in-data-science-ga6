
# 📊 DuckDB Linear Regression Assignment — Retail Store Sales

## 🎯 Objective

Write a DuckDB SQL query to calculate linear regression between **store square footage** (independent variable) and **total sales** (dependent variable) for a specific city, square footage condition, and from a given month onward.

Each student is assigned different:
- 📍 City name (`location`)
- 📏 Minimum square footage
- 📅 Start month (e.g., from month 6 onward)

---

## ✅ Use This SQL Template (Only Change 3 Values)

```sql
WITH store_totals AS (
  SELECT 
    s.store_id,
    s.square_footage,
    SUM(sd.monthly_sales) as total_sales
  FROM stores s
  JOIN sales_data sd ON s.store_id = sd.store_id
  WHERE s.location = 'REPLACE_CITY_HERE'
    AND s.square_footage >= REPLACE_SQUARE_FOOTAGE
    AND EXTRACT(MONTH FROM sd.sale_date) >= REPLACE_MONTH
  GROUP BY s.store_id, s.square_footage
)
SELECT 
  REGR_SLOPE(total_sales, square_footage) as slope,
  REGR_INTERCEPT(total_sales, square_footage) as intercept,
  REGR_R2(total_sales, square_footage) as r_squared
FROM store_totals;
```

---

## 🛠️ What to Replace

| Placeholder                   | Replace with |
|-------------------------------|--------------|
| `'REPLACE_CITY_HERE'`         | Your given city name (e.g., `'Winifredchester'`) |
| `REPLACE_SQUARE_FOOTAGE`      | Minimum sq ft value given in your question (e.g., `2500`) |
| `REPLACE_MONTH`               | Starting month number (e.g., `6` for June onward) |

> ⚠️ **Only change these 3 values. Do not edit the rest of the code.**

---

## 🧪 Example

If your question says:

- Location = `Winifredchester`
- Square footage ≥ `2500`
- From month = `6` (June)

Then use:

```sql
WHERE s.location = 'Winifredchester'
  AND s.square_footage >= 2500
  AND EXTRACT(MONTH FROM sd.sale_date) >= 6
```

---

## ✅ Output

Your final output will return **one row** with:

- `slope` (regression coefficient)
- `intercept` (y-axis intercept)
- `r_squared` (goodness of fit)

---

## 📤 Submission Steps

1. Copy the above SQL query template
2. Replace the 3 values with your assigned ones
3. Run it in DuckDB
4. Submit the query (don’t change structure)


# 📝 Q-13 Submission Guide: DuckDB SQL Query for Correlation Analysis

## 🎯 Objective

Calculate the **Pearson correlation coefficient** between `budget` and `total revenue` for selected campaigns, based on the filters **provided to you**.

---

## 📂 Tables Overview

You are given two tables:

- `campaigns`
  - `campaign_id`
  - `channel`
  - `budget`

- `performance_metrics`
  - `campaign_id`
  - `metric_date` (may have mixed formats)
  - `revenue`

---

## 🧠 Your Custom Inputs

Replace the below placeholders with your specific assignment values:

| Placeholder         | Description                          |
|---------------------|--------------------------------------|
| `'Email'`           | Replace with your given `channel`    |
| `25000`             | Replace with your minimum `budget`   |
| `'2025-04-26'`      | Replace with your specific `start date` |

---

## ✅ Final SQL Template

Use this DuckDB SQL query and **modify values accordingly**:

```sql
SELECT
    corr(c.budget, r.total_revenue) AS correlation
FROM campaigns c
JOIN (
    SELECT
        campaign_id,
        SUM(revenue) AS total_revenue
    FROM performance_metrics
    WHERE 
        TRY_CAST(metric_date AS DATE) >= DATE '2025-04-26'  -- 🔁 Replace with your own start date
    GROUP BY campaign_id
) r
ON c.campaign_id = r.campaign_id
WHERE c.channel = 'Email'  -- 🔁 Replace with your own channel
  AND c.budget >= 25000;   -- 🔁 Replace with your own budget threshold
```

---

## 🧪 Output Example

```
correlation
-----------
0.000
```

---

## 📌 Notes

- `TRY_CAST(metric_date AS DATE)` safely converts various date formats
- The subquery aggregates revenue **per campaign** after the given date
- Outer query joins on `campaign_id` and filters by `channel` and `budget`
- Round your final correlation to **3 decimal places**

---

## ✅ Final Submission

Submit your correlation value like this:

```
0.000
```

Replace all placeholders with the actual values provided to you in your assignment before running the query.

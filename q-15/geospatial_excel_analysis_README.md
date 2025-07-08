
# 📍 Geospatial Analysis in Excel: Store Location Optimization

## 🧠 Objective
Identify which existing store is closest to a proposed distribution center using **latitude and longitude** data with the **Haversine distance formula** in **Microsoft Excel**.

---

## 🗂 Dataset Details

### 🧾 Sheet: `Store_Locations`

| Column | Header           | Description                     |
|--------|------------------|---------------------------------|
| A      | Store_ID         | Unique store identifier         |
| D      | Latitude         | Latitude of the store           |
| E      | Longitude        | Longitude of the store          |

### 🧾 Sheet: `Target_Location`

| Cell    | Value            |
|---------|------------------|
| `B2`    | Target Latitude   |
| `C2`    | Target Longitude  |

---

## 📌 Task

Use Excel functions to:

1. Calculate the **distance** from each store to the target location.
2. Identify the **Store_ID** with the **minimum distance**.

---

## 🔢 Haversine Formula (for Excel)

Paste the following formula in a new column `H2` of `Store_Locations`:

```
=2 * 3959 * ASIN(SQRT(
    POWER(SIN(RADIANS((target_latitude - D2)/2)), 2) +
    COS(RADIANS(D2)) * COS(RADIANS(target_latitude)) *
    POWER(SIN(RADIANS((target_longitude - E2)/2)), 2)
))
```

✅ Replace `target_latitude` and `target_longitude` with actual values, e.g., `29.745644` and `-95.368483`.

✅ Drag the formula down to all rows (H2 to H30).

---

## 🧮 Final Steps

### ➤ Find Minimum Distance

In any empty cell (e.g., `I1`):

```
=MIN(H2:H30)
```

### ➤ Find Closest Store ID

In `I2`:

```
=INDEX(A2:A30, MATCH(MIN(H2:H30), H2:H30, 0))
```

This returns the **`Store_ID`** of the store **closest to the target**.

---

## ✅ Output

- `H` column → Distance to target (miles)
- `I1` → Minimum distance
- `I2` → Closest `Store_ID` (Final answer to submit)

---

## 🎓 Notes for All Students

- Your dataset values may differ, but the **format and structure is the same**, so follow these steps exactly.
- Only change the **target lat/lon** in the formula if needed.
- Ensure all distances are calculated before using `MIN()` and `MATCH()`.

---

## 💬 Example Result

If calculated correctly, the final output will be a `Store_ID` like:

```
ST034
```

Which is the closest store to the proposed site.

---

### 👏 Good Luck!

Use this guide to complete and verify your Excel geospatial assignment with full confidence!

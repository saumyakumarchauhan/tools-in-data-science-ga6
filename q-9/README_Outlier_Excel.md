# Outlier Detection with Excel (Pharmaceutical Batch Analysis)

This guide helps you perform **Outlier Detection using the 1.5 × IQR rule** in Excel. It is designed for students working with datasets of batch purity values (in different values but same format).

## 📁 Dataset Format

- Column A: `Batch_Id`
- Column B: `Purity_Percentage`
- Data starts from **row 2** to **row 94** (93 data points)

---

## ✅ Steps to Identify Outliers

### 1. **Calculate Q1 (25th Percentile)**
In any empty cell (e.g., D2), enter:
```
=QUARTILE(B2:B94, 1)
```

### 2. **Calculate Q3 (75th Percentile)**
In cell D3, enter:
```
=QUARTILE(B2:B94, 3)
```

### 3. **Calculate IQR (Interquartile Range)**
IQR = Q3 − Q1  
In D4, enter:
```
=D3 - D2
```

### 4. **Calculate Outlier Bounds**
- **Lower Bound** = Q1 − 1.5 × IQR
- **Upper Bound** = Q3 + 1.5 × IQR

In D5 and D6 respectively, enter:
```
=D2 - 1.5 * D4
=D3 + 1.5 * D4
```

### 5. **Count the Outliers**
- Values < Lower Bound → Low Outliers
- Values > Upper Bound → High Outliers

In D7 (low outliers) and D8 (high outliers):
```
=COUNTIF(B2:B94, "<" & D5)
=COUNTIF(B2:B94, ">" & D6)
```

### 6. **Get Total Outliers**
Add D7 and D8:
```
=D7 + D8
```

---

## 📌 Final Answer

The value in D9 is the **total number of outliers**.

Use this result to answer the question in your assignment portal.

---

## 📈 Optional: Create a Box Plot
- Select Column B (`Purity_Percentage`)
- Go to **Insert > Chart > Box and Whisker**
- Excel will visually mark outliers as dots

---

### 👩‍🔬 Use this method for any dataset in the same format.
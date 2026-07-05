# Customer Shopping Behavior Analysis

This project digs into how customers shop — what they buy, when they buy it, and what influences their decisions. The analysis is built in Python and visualized through a Power BI dashboard and a presentation deck.

---

## Repository Structure

```
Customer_Behaviour_Analysis/
│
├── data/
│   ├── customer_shopping_behavior.csv           # Original raw dataset
│   └── customer_shopping_behavior_cleaned.csv   # Cleaned version, ready for analysis
│
├── src/
│   ├── clean_data.py     # Cleans the raw data and adds derived columns
│   └── analysis.py       # Runs the analysis and generates charts
│
├── reports/
│   ├── CB_Report.docx                       # Written project report
│   ├── customer_behavior_analysis.pptx      # 9-slide presentation of findings
│   └── Customer_Behavior_dashboard.pbix     # Interactive Power BI dashboard
│
├── .gitignore
└── README.md
```

---

## The Dataset

The dataset has **3,900 customer records** across **18 columns**, covering things like age, gender, location, what they bought, how much they spent, shipping preferences, discounts, and review ratings. There were 37 missing values in the `Review Rating` column, which were filled in during cleaning.

---

## Getting Started

**Install dependencies:**

```bash
pip install pandas matplotlib
```

**Step 1 — Clean the data:**

```bash
cd src
python clean_data.py
```

This reads the raw CSV from `data/`, fills in missing ratings, renames columns consistently, adds a few useful new columns, and saves the cleaned file back to `data/`.

**Step 2 — Run the analysis:**

```bash
python analysis.py
```

The script is organized into functions — one per analysis. Uncomment the function calls at the bottom of the file for the analyses you want to run.

---

## What the Cleaning Script Does

`src/clean_data.py` takes the raw data and makes it analysis-ready:

- **Fills missing ratings** with the average rating for that product category
- **Standardizes column names** to `snake_case` (e.g. `purchase_amount_(usd)` becomes `purchase_amount`)
- **Adds an `age_group` column** that bins customers into four groups: Young Adults, Adults, Middle-aged, and Senior
- **Adds a `frequency_purchases_days` column** that converts purchase frequency labels (like "Weekly" or "Monthly") into actual number of days
- **Drops a redundant column** — `promo_code_used` turns out to be identical to `discount_applied`, so it's removed

---

## What the Analysis Covers

Each function in `src/analysis.py` can be run independently:

- **`revenue_by_gender()`** — pie chart showing how spending breaks down between male and female customers
- **`top_rated_products()`** — prints the highest-rated items
- **`shipping_type_comparison()`** — bar chart showing that Express shipping customers tend to spend more per transaction than Standard
- **`discount_dependent_products()`** — which items rely most heavily on discounts to drive purchases
- **`revenue_by_age_group()`** — pie chart of spending by age bracket
- **`customer_segmentation()`** — classifies customers as New, Returning, or Loyal based on purchase history

### Key Findings

- **Highest-rated products:** Gloves, Sandals, Boots, Hat, and Skirt (all rated between 3.78–3.86)
- **Shipping:** Express shipping customers spend more per order than Standard ones
- **Discounts:** Hats (50%), Sneakers (49.7%), and Coats (49.1%) are most frequently purchased with a discount
- **Segments:** Most customers fall into the Loyal segment
- **Age:** Middle-aged customers (35–54) generate the most revenue; spending drops off after 55

---

## Power BI Dashboard

Open `reports/Customer_Behavior_dashboard.pbix` in **Power BI Desktop**. The dashboard lets you explore revenue by category and age group, see subscription status breakdowns, and filter by gender, category, shipping type, and subscription status interactively.

---

## Presentation Slides

`reports/customer_behavior_analysis.pptx` is a 9-slide deck that walks through the entire project:

1. Title
2. Dataset overview
3. Data preparation
4. Revenue by gender
5. Product ratings
6. Shipping method comparison
7. Discount analysis
8. Customer segmentation
9. Revenue by age group

---

## Tools Used

- **Python** (pandas, matplotlib) — data cleaning and analysis
- **Power BI** — interactive dashboard
- **PowerPoint** — presentation slides
---

##👤 About Me  
---
I'm Guhan, a Computer Science student specializing in Data Science. This project is part of my ongoing effort to build practical, portfolio-ready experience in data analytics and visualization.

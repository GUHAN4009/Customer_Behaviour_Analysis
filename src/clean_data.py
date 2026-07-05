import pandas as pd


def load_raw_data(path="../data/customer_shopping_behavior.csv"):
    return pd.read_csv(path)


def clean_data(df):
    # Fill missing review ratings with the average rating for that category
    df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(
        lambda x: x.fillna(x.mean())
    )

    # Standardize column names to snake_case
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})

    # Bin customers into age groups
    labels = ["Young_Adults", "Adults", "Middleaged", "Senior"]
    df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)

    # Convert purchase frequency labels into number of days
    freq_map = {
        "Bi-Weekly": 14,
        "Every 3 Months": 90,
        "Fortnightly": 14,
        "Monthly": 30,
        "Annually": 365,
        "Quarterly": 90,
        "Weekly": 7,
    }
    df['frequency_purchases_days'] = df['frequency_of_purchases'].map(freq_map)

    # promo_code_used is identical to discount_applied — drop the redundant column
    df = df.drop('promo_code_used', axis=1)

    return df


def save_cleaned_data(df, path="../data/customer_shopping_behavior_cleaned.csv"):
    df.to_csv(path, index=False)


if __name__ == "__main__":
    raw_df = load_raw_data()
    cleaned_df = clean_data(raw_df)
    save_cleaned_data(cleaned_df)
    print("done")

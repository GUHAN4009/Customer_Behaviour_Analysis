import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/customer_shopping_behavior_cleaned.csv")


def revenue_by_gender():
    d1 = df.groupby('gender')['purchase_amount'].sum()
    plt.pie(d1, labels=d1.index, autopct=lambda p: f'{p * sum(d1) / 100:.0f}')
    plt.title("Purchase amount by gender")
    plt.legend(title='Gender')
    plt.tight_layout()
    plt.show()


def top_rated_products(n=5):
    gp = df.groupby('item_purchased')['review_rating'].mean()
    top = gp.sort_values(ascending=False).head(n)
    print(top)
    return top


def shipping_type_comparison():
    filtered = df[df['shipping_type'].isin(['Express', 'Standard'])]
    avg_by_shipping = filtered.groupby('shipping_type')['purchase_amount'].mean()
    plt.bar(avg_by_shipping.index, avg_by_shipping)
    plt.title("Average purchase amount by shipping type")
    plt.xlabel("Shipping Type")
    plt.ylabel("Average Purchase Amount")
    plt.grid(True)
    plt.show()


def discount_dependent_products(n=5):
    total = df.groupby('item_purchased').size()
    discounted = df[df['discount_applied'] == 'Yes'].groupby('item_purchased').size()
    discount_percentage = (discounted / total) * 100
    top = discount_percentage.sort_values(ascending=False).head(n)
    print(top)
    return top


def revenue_by_age_group():
    d1 = df.groupby('age_group')['purchase_amount'].sum()
    plt.pie(d1, labels=d1.index, autopct=lambda p: f'{p * sum(d1) / 100:.0f}')
    plt.title("Purchase amount by age group")
    plt.legend(title='Age Group')
    plt.tight_layout()
    plt.show()


def segment_customer(x):
    if x == 1:
        return "New"
    elif x >= 2 and x <= 10:
        return "Returning"
    else:
        return "Loyal"


def customer_segmentation():
    df['customer_segment'] = df['previous_purchases'].apply(segment_customer)
    segment_counts = df['customer_segment'].value_counts()
    plt.bar(segment_counts.index, segment_counts, color='green')
    plt.title("Customer Segments")
    plt.xlabel("Customer Segment")
    plt.ylabel("Count")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    # Uncomment the analyses you want to run
    # revenue_by_gender()
    top_rated_products()
    # shipping_type_comparison()
    # discount_dependent_products()
    # revenue_by_age_group()
    # customer_segmentation()

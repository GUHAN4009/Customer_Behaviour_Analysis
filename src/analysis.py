import pandas as pd

import matplotlib.pyplot as plt


df = pd.read_csv("customer_shopping_behavior_cleaned.csv")
#re checking the cleaned data set
# print(df.head())
# # print(df.info())
# # print(df.describe())
# # print(df.isnull().sum())

# #analytics using matplot lib

# d1 = df.groupby('gender')['purchase_amount'].sum()
# plt.pie(d1,labels=d1.index,autopct=lambda p: f'{p * sum(d1) / 100:.0f}')
# plt.title("Purchase amount by gender")
# plt.legend(title='Gender')
# plt.tight_layout()
# plt.edgewidth=2 
# plt.show()
# _______________________________________________________________
gp = df.groupby('item_purchased')['review_rating'].mean()
gps = gp.sort_values(ascending=False)
gps1 = gps.head(5)
print(gps1)   
# ________________________________________________________________________
# filtered = df[df['shipping_type'].isin(['Express', 'Standard'])]
# a1 = filtered.groupby('shipping_type')['purchase_amount'].mean()
# plt.bar(a1.index,a1)
# plt.title("Average purchase amount by shipping type")
# plt.xlabel("Shipping Type")
# plt.ylabel("Average Purchase Amount")
# plt.grid(True)
# plt.show()
#_____________________________________________________________
# total = df.groupby('item_purchased').size()
# discount = df[df['discount_applied'] == 'Yes'].groupby('item_purchased').size()
# discount_percentage = (discount / total) * 100
# top5 = discount_percentage.sort_values(ascending=False).head(5)
# print(top5)
#_______________________________________________________________ 

# d1 = df.groupby('age_group')['purchase_amount'].sum()

# plt.pie(d1,labels=d1.index,autopct=lambda p: f'{p * sum(d1) / 100:.0f}')
# plt.title("Purchase amount by age group")
# plt.legend(title='Age Group')
# plt.tight_layout()
# plt.edgewidth=2
# plt.show()

# _________________________________________________________
# def segment_customer(x):
#     if x == 1:
#         return "New"
#     elif x >2 and x <= 10:
#         return "Returning"
#     else:
#         return "Loyal"

# df['customer_segment'] = df['previous_purchases'].apply(segment_customer)

# g1 = df["customer_segment"].value_counts()

# plt.bar(g1.index,g1,color='green')
# plt.title("Customer Segments")
# plt.xlabel("Customer Segment")
# plt.ylabel("Count")
# plt.grid(True)
# plt.show()
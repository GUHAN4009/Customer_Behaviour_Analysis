import pandas as pd


df = pd.read_csv("customer_shopping_behavior.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.mean()))
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})
print(df.groupby('frequency_of_purchases')['review_rating'].mean()) 

labels = ["Young_Adults", "Adults", "Middleaged", "Senior"]

df['age_group']= pd.qcut(df['age'], q=4, labels=labels)
print(df[['age', 'age_group']].head(10))

freq_map= {"Bi-Weekly":14,"Every 3 Months":90,"Fortnightly":14,       
"Monthly":30,           
"Annually":365,          
"Quarterly":90,         
"Weekly":7}
df['frequency_purchases_days'] = df['frequency_of_purchases'].map(freq_map)
# print((df['discount_applied']==df['promo_code_used']).all())
df.drop('promo_code_used', axis=1, inplace=True)


df.to_csv("customer_shopping_behavior_cleaned.csv", index=False)
print("done")
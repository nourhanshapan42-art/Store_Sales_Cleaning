import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# إنشاء DataFrame بالبيانات المطلوبة
data = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 101],
    'Category': ['clothing', '   CLOTHING   ', 'Electronics', 'electronics', 'Home', 'home', 'clothing', 'clothing'],
    'Sales': [500.5, 300.0, 1200.0, None, 2500.0, 1800.5, 200.0, 500.5],
    'Customer': ['Ali', 'Mona', 'Ahmed', 'Sara', 'Mohamed', 'Ali', None, 'Ali']
}

df_store = pd.DataFrame(data)

# عرض البيانات للتأكد منها
print(df_store)
df_store = df_store.drop_duplicates()
df_store['Category'] = df_store['Category'].str.strip().str.title()
df_store['Sales'] = df_store['Sales'].fillna(0)
df_store['Customer'] = df_store['Customer'].fillna('Unknown')
print(df_store)

df_store.to_excel('New_store_data.xlsx', index=False)

Mean = df_store.groupby("Category")['Sales'].mean()
Mean.plot(kind='bar', color="skyblue")
print(Mean)

plt.title('New Bar')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()
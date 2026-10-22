import pandas as pd
import matplotlib.pyplot as plt

# 1. إنشاء بيانات شبيهة بداتا عملاء حقيقيين (E-Commerce)
data = {
    'Transaction_ID': [201, 202, 203, 204, 205, 206, 201],
    'Region': [' Cairo ', 'Alex', ' CAIRO ', 'Giza', 'Alex', None, ' Cairo '],
    'Product': ['Laptop', ' Phone ', 'Laptop', ' Tablet ', 'Phone', 'Tablet', 'Laptop'],
    'Price': [15000, 8000, None, 5000, 8000, 5000, 15000],
    'Quantity': [1, 2, 1, 3, None, 1, 1],
    'Date': ['2026-01-10', '2026/01/11', '2026-01-10', '2026-01-12', '2026-01-13', '2026-01-14', '2026-01-10']
}

df = pd.DataFrame(data)

# 2. خطوة التنظيف والمعالجة الاحترافية
# أ. حذف التكرار
df = df.drop_duplicates()

# ب. تنظيف النصوص والمسافات وتوحيد الحروف (Capitalization)
df['Region'] = df['Region'].str.strip().str.title()
df['Product'] = df['Product'].str.strip().str.title()

# ج. التعامل مع القيم المفقودة (Fill Missing Values)
df['Region'] = df['Region'].fillna('Unknown')
df['Price'] = df['Price'].fillna(df['Price'].mean()) # استبدال السعر الناقص بمتوسط الأسعار
df['Quantity'] = df['Quantity'].fillna(1) # استبدال الكمية الناقصة بـ 1

# د. توحيد صيغة التواريخ (Date Formatting)
df['Date'] = pd.to_datetime(df['Date'], format='mixed').dt.strftime('%Y-%m-%d')

# 3. حساب إجمالي المبيعات (Feature Engineering)
df['Total_Sales'] = df['Price'] * df['Quantity']

print("--- البيانات بعد التنظيف والمعالجة ---")
print(df)

# 4. استخراج التقرير المطلوب للعميل (Aggregation Report)
region_report = df.groupby('Region')['Total_Sales'].sum()
print("\n--- تقرير إجمالي المبيعات حسب المنطقة ---")
print(region_report)

# 5. تصدير الشغل للعميل
df.to_csv('Cleaned_Ecommerce_Data.csv', index=False)
region_report.to_excel('Region_Sales_Report.xlsx')

# 6. الرسم البياني للتقرير
region_report.plot(kind='bar', color='teal', figsize=(8, 5))
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales (EGP)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
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
# 1. استخدام ستايل احترافي ونظيف
plt.style.use('seaborn-v0_8-whitegrid')

# 2. إنشاء الشكل بحجم مناسب ودقة عالية (DPI)
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=150)

# 3. رسم الأعمدة مع ألوان جذابة وشكل مودرن
bars = region_report.plot(
    kind='bar', 
    ax=ax, 
    color='#1f77b4',       # لون أزرق إلكتروني احترافي
    edgecolor='#0f4c81',   # تحديد خفيف للأعمدة
    linewidth=1.2,
    width=0.55             # عرض الأعمدة
)

# 4. إضافة القيم فوق كل بار (Data Labels)
for bar in ax.patches:
    yval = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2.0, 
        yval + 400, 
        f'{int(yval):,}',    # إضافة فاصلة الألوافات 25,000
        ha='center', 
        va='bottom', 
        fontsize=10, 
        fontweight='bold', 
        color='#333339'
    )

# 5. تحسين العناوين والمحاور
plt.title('Total Sales by Region (EGP)', fontsize=14, fontweight='bold', pad=15, color='#111111')
plt.xlabel('Region', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('Total Sales (EGP)', fontsize=11, fontweight='bold', labelpad=10)

# 6. ضبط زاوية الأسماء وضبط الحدود
plt.xticks(rotation=0, fontsize=10, fontweight='bold')
ax.set_ylim(0, max(region_report) * 1.15)  # إعطاء مساحة علوية للأرقام

# 7. إزالة الحدود الخارجية الزائدة لشكل أنظف
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()

# 8. حفظ الصورة بجودة عالية لمعرض الأعمال
plt.savefig('sales_by_region_clean.png', dpi=300, bbox_inches='tight')
plt.show()

# --- 7. رسم بياني إضافي: تحليل اتجاهات المبيعات عبر الأشهر (Line Chart) ---

# بيانات تجريبية لاتجاه المبيعات الشهرية
monthly_data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [12000, 19000, 15000, 24000, 22000, 30000],
}
monthly_df = pd.DataFrame(monthly_data)

# إنشاء الشكل بدقة عالية
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=150)

# رسم الخط البياني مع النقاط
ax.plot(
    monthly_df['Month'],
    monthly_df['Sales'],
    marker='o',
    color='#2b5c8f',
    linewidth=3,
    markersize=8,
    markerfacecolor='#e74c3c',
    markeredgecolor='#ffffff',
)

# إضافة القيم فوق كل نقطة (Data Labels)
for i, txt in enumerate(monthly_df['Sales']):
  ax.text(
      monthly_df['Month'][i],
      txt + 1000,
      f'{txt:,}',
      ha='center',
      va='bottom',
      fontsize=10,
      fontweight='bold',
      color='#333339',
  )

# تحسين العناوين والمحاور
plt.title(
    'Monthly Sales Trend (EGP)',
    fontsize=14,
    fontweight='bold',
    pad=15,
    color='#111111',
)
plt.xlabel('Month', fontsize=11, fontweight='bold', labelpad=10)
plt.ylabel('Sales (EGP)', fontsize=11, fontweight='bold', labelpad=10)

# تنسيق المحاور والحدود
plt.xticks(fontsize=10, fontweight='bold')
ax.set_ylim(0, max(monthly_df['Sales']) * 1.15)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()

# حفظ الصورة الثالثة بجودة عالية لمعرض الأعمال
plt.savefig('monthly_sales_trend_clean.png', dpi=300, bbox_inches='tight')
plt.show()

# --- 8. رسم بياني إضافي: نسبة مبيعات المناطق (Pie Chart) ---

# حساب إجمالي المبيعات لكل منطقة
region_sales = df.groupby('Region')['Total_Sales'].sum()

# إنشاء الشكل بدقة عالية
fig, ax = plt.subplots(figsize=(8, 6), dpi=150)

# ألوان مخصصة احترافية
colors_list = ['#1f77b4', '#aec7e8', '#ff7f0e', '#2ca02c']

# رسم البي دي إيه (Pie Chart)
wedges, texts, autotexts = ax.pie(
    region_sales, 
    labels=region_sales.index, 
    autopct='%1.1f%%', 
    startangle=140,
    colors=colors_list,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

# تنسيق النصوص والأرقام داخل الرسمة الدائرية
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(11)

for text in texts:
    text.set_fontweight('bold')
    text.set_fontsize(11)

plt.title('Sales Distribution by Region (%)', fontsize=14, fontweight='bold', pad=20, color='#111111')

plt.tight_layout()

# حفظ الصورة الرابعة للمعرض
plt.savefig('sales_pie_chart.png', dpi=300, bbox_inches='tight')
plt.show()

# حفظ الصورتين مباشرة في المجلد بدون إظهار نوافذ مزعجة
plt.savefig('sales_by_region_clean.png', dpi=300, bbox_inches='tight')
plt.close()

plt.savefig('sales_pie_chart.png', dpi=300, bbox_inches='tight')
plt.close()

print('✨ تم حفظ جميع رسوم معرض الأعمال بنجاح وجاهزة للرفع!')
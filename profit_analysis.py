import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. CREATE DATA MANUALLY (To avoid loading errors) ---
data = {
    'Category': ['Technology', 'Technology', 'Furniture', 'Furniture', 'Office Supplies', 'Office Supplies'],
    'Sub-Category': ['Phones', 'Accessories', 'Tables', 'Chairs', 'Paper', 'Binders'],
    'Sales': [5000, 3000, 4500, 4000, 1500, 1200],
    'Profit': [1200, 800, -1500, 400, 300, -200]
}

df = pd.DataFrame(data)
print("✅ Data Created Successfully!")

# --- 2. THE ANALYSIS ---
# Calculate total profit and sales
total_s = df['Sales'].sum()
total_p = df['Profit'].sum()

print(f"Total Sales: ${total_s}")
print(f"Total Profit: ${total_p}")

# --- 3. THE VISUALIZATION ---
# This creates a bar chart showing Profit and Loss
plt.figure(figsize=(10, 6))

# Use a list to color Profit green and Loss red
colors = ['red' if x < 0 else 'green' for x in df['Profit']]

plt.bar(df['Sub-Category'], df['Profit'], color=colors)

# Adding labels so it looks professional
plt.title('Profit/Loss Analysis by Sub-Category', fontsize=15)
plt.xlabel('Product Sub-Category', fontsize=12)
plt.ylabel('Profit in USD ($)', fontsize=12)
plt.axhline(0, color='black', linewidth=1) # The "Zero" line
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
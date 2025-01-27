import pandas as pd
data = pd.read_csv(r"C:\Users\Vailla Bhargav\Downloads\Day_8_sales_data.csv")
print("First few rows of the dataset:")
print(data.head())
print("\nSummary Statistics:")
print(data.describe())
print("\nTotal Sales by Region:")
region_group = data.groupby("Region")["Sales"].sum()
print(region_group)
print("\nProduct with highest quantity sold:")
most_sold_product = data.groupby("Product")["Quantity"].sum().idxmax()
print(most_sold_product)
data['Profit_Margin'] = (data['Profit'] / data['Sales']) * 100
print("\nAverage Profit Margin by Product:")
average_profit_margin = data.groupby("Product")["Profit_Margin"].mean()
print(average_profit_margin)
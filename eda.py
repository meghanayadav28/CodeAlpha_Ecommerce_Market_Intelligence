import pandas as pd

print("📊 Initializing Exploratory Data Analysis (EDA) Pipeline...")

# 1. Load the dataset we scraped in Task 1
df = pd.read_csv("raw_market_intelligence.csv")

print(f"\n✨ Dataset loaded successfully! Total records to analyze: {len(df)}")

# 2. Clean the Price Column
df['Price_Clean'] = df['Price_Raw'].str.replace('$', '', regex=False)
df['Price_Clean'] = pd.to_numeric(df['Price_Clean'])

# 3. Feature Engineering (Extracting the Brand Name)
df['Brand'] = df['Product_Name'].str.split().str[0]

# 4. Run Statistical Calculations
print("\n🧮 Calculating Descriptive Statistics for Prices:")
mean_price = df['Price_Clean'].mean()
max_price = df['Price_Clean'].max()
min_price = df['Price_Clean'].min()

print(f"🔹 Average Laptop Price: ${mean_price:.2f}")
print(f"🔹 Most Expensive Laptop: ${max_price:.2f}")
print(f"🔹 Cheapest Laptop: ${min_price:.2f}")

# 5. Market Share Grouping
print("\n🏢 Number of Unique Laptops Available by Brand:")
brand_counts = df['Brand'].value_counts()
print(brand_counts)

# Save our newly cleaned dataset into a separate file for Task 3
df.to_csv("cleaned_market_intelligence.csv", index=False)
print("\n💾 Cleaned dataset successfully exported to 'cleaned_market_intelligence.csv'!")
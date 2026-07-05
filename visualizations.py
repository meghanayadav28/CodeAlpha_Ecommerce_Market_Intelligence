import pandas as pd
import matplotlib.pyplot as plt

print("🎨 Initializing Data Visualization Pipeline...")

# 1. Load the cleaned data from Task 2
df = pd.read_csv("cleaned_market_intelligence.csv")

# 2. Prepare Data for the Chart (Count laptops by brand)
brand_counts = df['Brand'].value_counts()

# 3. Create the Bar Chart
plt.figure(figsize=(10, 6)) # Sets the window size
brand_counts.plot(kind='bar', color='skyblue', edgecolor='black')

# 4. Add Titles and Labels so it's easy to read
plt.title('Laptop Market Volume by Brand (E-Commerce Sandbox)', fontsize=14, fontweight='bold')
plt.xlabel('Laptop Brand', fontsize=12)
plt.ylabel('Number of Models Available', fontsize=12)
plt.xticks(rotation=45) # Tilts the brand names so they don't overlap
plt.tight_layout() # Ensures everything fits perfectly inside the image frame

# 5. Save the graph as an image file on your laptop
plt.savefig('brand_market_volume.png', dpi=300)
print("💾 Graph successfully created and saved as 'brand_market_volume.png'!")

# 6. Display the graph on your screen
print("👁️ Displaying the visualization window...")
plt.show()
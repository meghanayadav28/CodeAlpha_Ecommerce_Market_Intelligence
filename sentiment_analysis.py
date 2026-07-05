import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

print("🧠 Initializing Natural Language Processing (NLP) Pipeline...")

# Download the required VADER lexicon data file from NLTK
nltk.download('vader_lexicon', quiet=True)

# 1. Load our cleaned dataset from Task 2
df = pd.read_csv("cleaned_market_intelligence.csv")

# Initialize the VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

print("\n🔍 Analyzing text sentiment on product specifications...")

# 2. Run Sentiment Scoring
# VADER calculates a 'compound' score between -1 (very negative) and +1 (very positive)
df['Sentiment_Score'] = df['Specifications'].apply(lambda text: sia.polarity_scores(str(text))['compound'])

# 3. Categorize the scores into clean labels
def categorize_sentiment(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment_Label'] = df['Sentiment_Score'].apply(categorize_sentiment)

# 4. Print Summary Analytics to the terminal
print("\n📋 Text Sentiment Distribution:")
sentiment_counts = df['Sentiment_Label'].value_counts()
print(sentiment_counts)

# Let's take a look at a few examples of how they matched up
print("\n👀 Sneak Peek of Text Classifications:")
print(df[['Product_Name', 'Sentiment_Label', 'Sentiment_Score']].head(5))

# 5. Export the final data file containing ALL tasks' information
df.to_csv("final_market_intelligence.csv", index=False)
print("\n💾 Ultimate data bundle saved to 'final_market_intelligence.csv'!")
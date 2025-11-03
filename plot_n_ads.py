import pandas as pd
import matplotlib.pyplot as plt

# Load the collaboratively filled CSV file
df = pd.read_csv("corpus_sources.csv")

# Optional: ensure correct ordering by date
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.sort_values("date")

# Create the bar plot
plt.figure(figsize=(10, 5))
plt.bar(df["date"].dt.strftime("%Y-%m-%d"), df["n_ads"])

# Formatting
plt.xticks(rotation=45, ha="right")
plt.xlabel("Date of Issue")
plt.ylabel("Number of Advertisements (n_ads)")
plt.title("Number of Ads per Newspaper Issue")
plt.tight_layout()

# Show or save
plt.show()
# plt.savefig("n_ads_barplot.png", dpi=300)

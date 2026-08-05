import pandas as pd

# Load dataset
file_path = "customer_shopping_behavior.csv"
df = pd.read_csv(file_path)

# Preview data
df.head()

# Dataset information
df.info()

# Summary statistics
df.describe(include="all")

# Check missing values
df.isna().sum()

# Fill missing Review Rating values using category-wise median
median_rating = df.groupby("Category")["Review Rating"].transform("median")
df["Review Rating"] = df["Review Rating"].fillna(median_rating)

# Verify missing values
df.isna().sum()

# Rename columns to snake_case
df.columns = (
    df.columns
      .str.lower()
      .str.replace(" ", "_")
)

df.rename(
    columns={"purchase_amount_(usd)": "purchase_amount"},
    inplace=True
)

# Check updated column names
df.columns

# Create Age Group column
age_labels = ["Young Adult", "Adult", "Middle-aged", "Senior"]

df["age_group"] = pd.qcut(
    df["age"],
    q=4,
    labels=age_labels
)

df[["age", "age_group"]].head(10)

# Create Purchase Frequency (Days) column
frequency_mapping = {
    "Fortnightly": 14,
    "Weekly": 7,
    "Monthly": 30,
    "Quarterly": 90,
    "Bi-Weekly": 14,
    "Annually": 365,
    "Every 3 Months": 90
}

df["purchase_frequency_days"] = (
    df["frequency_of_purchases"]
      .map(frequency_mapping)
)

df[["purchase_frequency_days", "frequency_of_purchases"]].head(10)

# Check whether Discount Applied and Promo Code Used columns are identical
matching = df["discount_applied"].eq(df["promo_code_used"]).all()
print(matching)

# Remove Promo Code Used column
df.drop(columns=["promo_code_used"], inplace=True)

# Verify updated columns
df.columns

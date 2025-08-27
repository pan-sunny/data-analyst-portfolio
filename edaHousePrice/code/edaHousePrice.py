# code/edaHousePrice.py

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Set up paths
# DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/train.csv')

# Set styles
sns.set(style="whitegrid")
plt.style.use("ggplot")


def load_data():
    print("Loading dataset...")
    df = pd.read_csv('../data/train.csv')
    print(f"Shape: {df.shape}")
    return df


def inspect_data(df):
    print("\nDataset Info:")
    print(df.info())
    print("\nDescriptive Stats:")
    print(df.describe().T)

    print("\nMissing Values:")
    missing = df.isnull().sum()
    print(missing[missing > 0].sort_values(ascending=False))


def plot_sale_price(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['SalePrice'], kde=True)
    plt.title("Distribution of SalePrice")
    plt.savefig('../images/saleprice_distribution.png')
    plt.show()

    df['LogSalePrice'] = np.log1p(df['SalePrice'])

    plt.figure(figsize=(8, 5))
    sns.histplot(df['LogSalePrice'], kde=True, color='orange')
    plt.title("Log-Transformed SalePrice")
    plt.savefig('../images/log_saleprice_distribution.png')
    plt.show()


def correlation_analysis(df):
    print("\nCorrelation with SalePrice:")
    num_df = df.select_dtypes(include='number')
    corr = num_df.corr()['SalePrice'].sort_values(ascending=False)
    print(corr.head(10))

    top_features = corr.index[1:11]
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[top_features].corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Top Correlated Features")
    plt.savefig('../images/top_correlated_heatmap.png')
    plt.show()


def feature_visuals(df):
    # Scatter: GrLivArea vs SalePrice
    plt.figure(figsize=(6, 5))
    sns.scatterplot(x='GrLivArea', y='SalePrice', data=df)
    plt.title("GrLivArea vs SalePrice")
    plt.savefig('../images/grlivarea_vs_saleprice.png')
    plt.show()

    # Boxplot: OverallQual vs SalePrice
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='OverallQual', y='SalePrice', data=df)
    plt.title("OverallQual vs SalePrice")
    plt.savefig('../images/overallqual_vs_saleprice.png')
    plt.show()

    # Categorical: SaleCondition vs SalePrice
    plt.figure(figsize=(10, 5))
    sns.boxplot(x='SaleCondition', y='SalePrice', data=df)
    plt.xticks(rotation=45)
    plt.title("SaleCondition vs SalePrice")
    plt.savefig('../images/salecondition_vs_saleprice.png')
    plt.show()


def main():
    df = load_data()
    inspect_data(df)
    plot_sale_price(df)
    correlation_analysis(df)
    feature_visuals(df)


if __name__ == "__main__":
    main()

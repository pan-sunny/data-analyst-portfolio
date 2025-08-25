# edaTitanic.py

"""
Titanic Survival Exploratory Data Analysis (EDA)

This script performs data cleaning, exploration, and visualization on the Titanic dataset
to uncover patterns in passenger survival.

"""

# 1. Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set plot style
sns.set_style("whitegrid")

# 2. Load Dataset
# Combine train data with test data
data_train = pd.read_csv ('../data/train.csv')
data_test = pd.read_csv ('../data/test.csv')
print('TrainData:',data_train.shape, 'TestData', data_test.shape)
df = data_train.append(data_test, ignore_index=True)

# 3. Data Cleaning
# Fill missing Age values with median
df['Age'].fillna(df['Age'].median(), inplace=True)

# Drop 'Cabin' due to many missing values
df.drop(columns=['Cabin'], inplace=True)

# Fill Embarked missing values with mode
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

# 4. Exploratory Data Analysis
print("Dataset shape:", df.shape)
print("\nSurvival counts:\n", df['Survived'].value_counts())
print("\nSurvival rate by Gender:\n", df.groupby('Sex')['Survived'].mean())
print("\nSurvival rate by Passenger Class:\n", df.groupby('Pclass')['Survived'].mean())

# 5. Create images directory if not exists
img_dir = '../images'
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

# 6. Visualizations

# Survival count by Gender
plt.figure(figsize=(8,6))
sns.countplot(x='Survived', hue='Sex', data=df, palette='pastel')
plt.title('Survival Count by Gender')
plt.xlabel('Survived (0 = No, 1 = Yes)')
plt.ylabel('Count')
plt.savefig(os.path.join(img_dir, 'survival_by_gender.png'))
plt.show()

# Survival rate by Passenger Class
plt.figure(figsize=(8,6))
sns.barplot(x='Pclass', y='Survived', data=df, hue='Pclass', palette='muted', errorbar=None)
plt.title('Survival Rate by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Survival Rate')
plt.savefig(os.path.join(img_dir, 'survival_by_class.png'))
plt.show()

# Age distribution by Survival status
plt.figure(figsize=(10,6))
sns.kdeplot(df.loc[df['Survived'] == 1, 'Age'], label='Survived', fill=True)
sns.kdeplot(df.loc[df['Survived'] == 0, 'Age'], label='Die', fill=True)
plt.title('Age Distribution by Survival Status')
plt.xlabel('Age')
plt.ylabel('Density')
plt.legend()
plt.savefig(os.path.join(img_dir, 'age_distribution.png'))
plt.show()

# 7. Insights summary (print to console)
print("\nKey Insights:")
print("- Women had a significantly higher survival rate than men.")
print("- First class passengers had higher survival rates.")
print("- Younger passengers (especially children) had better chances of survival.")


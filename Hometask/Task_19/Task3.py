import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

titanic = sns.load_dataset("titanic")

# Scatter Plot
sns.scatterplot(x="age", y="fare", data=titanic)
plt.title("Scatter Plot: Age vs Fare")
plt.show()

# Histogram	Display distribution of a single numerical variable
sns.histplot(x="age", data=titanic)
plt.title('Histogram: Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Box Plot	Show distribution and identify outliers in numerical data
sns.boxplot(x="survived", y="age", data=titanic)
plt.title('Box Plot: Age Distribution by Survival')
plt.xlabel('Survived')
plt.ylabel('Age')
plt.show()

# Violin Plot	Combine box plot with kernel density estimation for better insights
sns.violinplot(x="class", y="age", data=titanic)
plt.title('Violin Plot: Age Distribution by Class')
plt.xlabel('Class')
plt.ylabel('Age')
plt.show()

# Bar Plot	Compare categorical variables
sns.barplot(x="class", y="fare", data=titanic)
plt.title('Bar Plot: Fare by Class')
plt.xlabel('Class')
plt.ylabel('Fare')
plt.show()

# Count Plot	Show count of observations in each category
sns.countplot(x="sex", data=titanic)
plt.title('Count Plot: Passengers by Sex')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.show()


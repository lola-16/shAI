import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Access to csv file
df = pd.read_csv('Salaries.csv')  

# Basic 
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

# Handling empty columns
df = df.dropna(axis=1, how='all')

# stats  
print("Mean Salary: $", df['TotalPay'].mean())
print("Median Salary: $", df['TotalPay'].median())   
print("Minimum Salary: $", df['TotalPay'].min())  
print("Maximum Salary: $", df['TotalPay'].max())

# histogram
df['TotalPay'].plot(kind='hist')   
plt.title('Salary Distribution')  
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# pie chart grouped by year 
year_counts = df['Year'].value_counts()

labels = year_counts.index
sizes = year_counts.values

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title('Employee Distribution by Year')  
plt.show()

# Scatter plot
df.plot(x='OvertimePay', y='TotalPay', kind='scatter')
plt.xlabel('Overtime Pay')
plt.ylabel('Total Pay')  
plt.show()

# Grouping analysis
mean_salary = df.groupby('Agency')['TotalPay'].mean()
print(mean_salary)

# Correlation 
print(df['TotalPay'].corr(df['OvertimePay']))

# Export clean data
df.to_csv('cleaned_salaries.csv', index=False)

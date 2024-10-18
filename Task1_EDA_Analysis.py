# Exploratory Data Analysis (EDA) Task
# Dataset: Automobile Data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Task 1: Data Loading and Initial Exploration
# Load the dataset and perform initial inspection
def load_and_inspect_data():
    # Creating sample automobile dataset
    data = {
        'price': np.random.normal(25000, 5000, 100),
        'mileage': np.random.normal(50000, 20000, 100),
        'year': np.random.randint(2015, 2024, 100),
        'engine_size': np.random.normal(2.5, 0.5, 100),
        'horsepower': np.random.normal(200, 50, 100),
        'fuel_efficiency': np.random.normal(25, 5, 100),
        'manufacturer': np.random.choice(['Toyota', 'Honda', 'Ford', 'BMW', 'Mercedes'], 100)
    }
    
    df = pd.DataFrame(data)
    
    # Tasks:
    # 1.1 Display the first 5 rows of the dataset
    # 1.2 Check for missing values
    # 1.3 Generate basic statistical summary
    # 1.4 Display dataset information (datatypes, non-null counts)
    return df

# Task 2: Distribution Analysis
def analyze_distributions(df):
    # Tasks:
    # 2.1 Create histograms for numerical variables
    plt.figure(figsize=(15, 10))
    for i, col in enumerate(['price', 'mileage', 'horsepower', 'fuel_efficiency'], 1):
        plt.subplot(2, 2, i)
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
    plt.tight_layout()
    
    # 2.2 Create box plots to identify outliers
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df[['price', 'mileage', 'horsepower', 'fuel_efficiency']])
    plt.xticks(rotation=45)
    plt.title('Box Plots for Numerical Variables')

# Task 3: Correlation Analysis
def analyze_correlations(df):
    # Tasks:
    # 3.1 Calculate correlation matrix
    numerical_cols = ['price', 'mileage', 'year', 'engine_size', 'horsepower', 'fuel_efficiency']
    correlation_matrix = df[numerical_cols].corr()
    
    # 3.2 Create a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
    plt.title('Correlation Heatmap')

# Task 4: Categorical Analysis
def analyze_categorical(df):
    # Tasks:
    # 4.1 Create bar plot for manufacturer distribution
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='manufacturer')
    plt.title('Distribution of Manufacturers')
    plt.xticks(rotation=45)
    
    # 4.2 Create box plots for price by manufacturer
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='manufacturer', y='price')
    plt.title('Price Distribution by Manufacturer')
    plt.xticks(rotation=45)

# Task 5: Relationship Analysis
def analyze_relationships(df):
    # Tasks:
    # 5.1 Create scatter plots for important variable pairs
    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    sns.scatterplot(data=df, x='mileage', y='price')
    plt.title('Price vs Mileage')
    
    plt.subplot(1, 3, 2)
    sns.scatterplot(data=df, x='horsepower', y='price')
    plt.title('Price vs Horsepower')
    
    plt.subplot(1, 3, 3)
    sns.scatterplot(data=df, x='fuel_efficiency', y='price')
    plt.title('Price vs Fuel Efficiency')
    
    plt.tight_layout()

# Main execution
def main():
    # Load data
    df = load_and_inspect_data()
    
    # Perform all analyses
    analyze_distributions(df)
    analyze_correlations(df)
    analyze_categorical(df)
    analyze_relationships(df)
    
    # Display all plots
    plt.show()

if __name__ == "__main__":
    main()

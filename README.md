# Task1_EDA
Name: Syed Sharshad
Company: CODTECH IT SOLUTIONS
ID: CT08DS9200
Domain:  Data Science 
Duration: October to November 2024
Mentor: Muzammil Ahmed

This project performs a comprehensive Exploratory Data Analysis (EDA) on automobile data, implementing various statistical and visualization techniques to understand patterns and relationships in vehicle characteristics.
📋 Features
The analysis includes five main components:

Data Loading and Initial Exploration

Dataset creation with synthetic automobile data
Basic statistical summaries
Missing value checks
Data type verification


Distribution Analysis

Histograms for numerical variables (price, mileage, horsepower, fuel efficiency)
Box plots for outlier detection
Distribution visualization with KDE plots


Correlation Analysis

Correlation matrix calculation
Heatmap visualization
Analysis of relationships between numerical variables


Categorical Analysis

Manufacturer distribution visualization
Price distribution across different manufacturers
Bar plots and box plots for categorical insights


Relationship Analysis

Scatter plots for key variable pairs
Price relationships with mileage, horsepower, and fuel efficiency
Multi-panel visualization layout



🔧 Prerequisites
pythonCopypandas
numpy
matplotlib
seaborn
📥 Installation

Clone the repository:

bashCopygit clone https://github.com/yourusername/auto-data-analysis.git

Install required packages:

bashCopypip install -r requirements.txt
💻 Usage
Run the main script:
bashCopypython auto_analysis.py
The script will:

Generate a synthetic dataset
Perform all analyses automatically
Display multiple visualization plots

📊 Sample Outputs
The program generates several visualizations:

Distribution plots for numerical variables
Box plots for outlier detection
Correlation heatmap
Manufacturer distribution plots
Price-feature relationship scatter plots

🔍 Code Structure
Copyauto_analysis.py
│
├── load_and_inspect_data()
│   └── Creates and returns synthetic dataset
│
├── analyze_distributions()
│   ├── Histograms
│   └── Box plots
│
├── analyze_correlations()
│   └── Correlation heatmap
│
├── analyze_categorical()
│   ├── Manufacturer distribution
│   └── Price by manufacturer
│
├── analyze_relationships()
│   └── Feature relationship scatter plots
│
└── main()
    └── Orchestrates all analyses
🛠 Customization
You can modify the code to:

Use your own dataset by changing the data dictionary in load_and_inspect_data()
Adjust plot parameters in visualization functions
Add new analysis components
Modify the synthetic data generation parameters

📝 Functions Description
load_and_inspect_data()
Generates synthetic automobile data with the following features:

price
mileage
year
engine_size
horsepower
fuel_efficiency
manufacturer.

# 24ADI003---24BAD030
Scenario 1 — scenario_1_exp_1_.ipynb

Notebook: scenario_1_exp_1_.ipynb
Dataset used: carrie1/ecommerce-data — file: data.csv
Dataset link: https://www.kaggle.com/carrie1/ecommerce-data
What it does: loads the ecommerce transactions dataset, cleans rows with non-positive Quantity/UnitPrice, computes TotalSales, displays basic info and null counts, plots top products by total sales and total sales over time.

Scenario 2 — scenario_2_exp_1_.ipynb

Notebook: scenario_2_exp_1_.ipynb
Dataset used: uciml/pima-indians-diabetes-database — file: diabetes.csv
Dataset link: https://www.kaggle.com/uciml/pima-indians-diabetes-database
What it does: loads the Pima Indians Diabetes dataset, inspects structure and missing values, replaces zeros with NA for selected clinical columns (Glucose, BloodPressure, SkinThickness, Insulin, BMI), shows updated null counts, and plots a Glucose histogram and Age boxplot.

Scenario 3 — scenario_3_exp_1_.ipynb

Notebook: scenario_3_exp_1_.ipynb
Dataset used: harishkumardatalab/housing-price-prediction — file: Housing.csv
Dataset link: https://www.kaggle.com/harishkumardatalab/housing-price-prediction
What it does: loads a housing price dataset, checks for missing values, plots area vs price scatter, and shows a numeric-feature correlation heatmap (uses seaborn/matplotlib for visual EDA).

Scenario 4 — scenario_4_exp_1_.ipynb

Notebook: scenario_4_exp_1_.ipynb
Dataset used: imakash3011/customer-personality-analysis — file: marketing_campaign.csv
Dataset link: https://www.kaggle.com/imakash3011/customer-personality-analysis
What it does: reads the marketing campaign dataset, computes Age from Year_Birth, reports missing values, and produces histograms and boxplots (Age distribution, Income boxplot, spending boxplots for several product categories).

EXPERIMENT - 2

scenario 1 - Predict ocean water temperature using environmental and depth-related features. Dataset (Kaggle – Public): https://www.kaggle.com/datasets/sohier/calcofi Discription of the code: Ocean temperature is influenced by variables such as depth, salinity, oxygen level, latitude, and longitude. By using regression models (e.g., Linear Regression), we can learn the relationship between these features and temperature and predict continuous temperature values.

scenario 2 - Classify whether LIC stock price will increase (1) or decrease (0) based on historical data. Dataset (Kaggle – Public): https://www.kaggle.com/datasets/debashis74017/lic-stock-price-data Discription of the code: This program uses Logistic Regression to classify LIC stock price movement as increase or decrease based on historical data. The dataset is loaded and cleaned, and a binary target variable is created by comparing the closing and opening prices. The input features used are Open, High, Low, and Volume, and missing values are handled using mean substitution. Feature scaling is applied to improve model performance, and the data is split into training and testing sets. The Logistic Regression model is trained and evaluated using accuracy and a confusion matrix, and its performance is visualized using an ROC curve and a feature importance graph.

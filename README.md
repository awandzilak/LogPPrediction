```diff
- WORK IN PROGRESS -
```

## Prediction of octanol-water partition coefficient of small drug-like molecules based on topological descriptors

### Background
Organic solvents - water partition coefficients are amongst the most meaningful molecular properties in drug design.  An easy access to partition coefficient is therefore instrumental. Unfortunately, systematic measurement of partition coefficient is often prohibitive due to time and resource constraints. To circumvent these constraints, systematic fast and accurate prediction of the partition coefficients is a highly desirable goal. 

### Goal
The purpose of this project is to employ different machine learning methods, such as: **Linear Regression**, **Random Forest** and **Neural Network** to **predict** the value of octanol-water partition coefficient (**logP**) based on a restricted number of topological descriptors. The models will be also compared.

### Workflow, libraries & packages
![workflow](https://github.com/awandzilak/LogPPrediction/blob/main/images/workflow.png)

### Data [_(scraping.ipynb)_](https://github.com/awandzilak/LogPPrediction/blob/main/scraping.ipynb)
Data were sourced from the ZINC20 database (https://zinc20.docking.org/). The information was extracted using the BeautifulSoup library and stored in an SQLite database, primarily comprising mostly topological parameters. Additional descriptors were generated based on Simplified Molecular Input Line Entry Specification (SMILES) strings of molecules, which contain information on atom connectivity, atomic numbers, and charge. RDKit package was employed for this purpose.

### Data cleaning [_(clean.ipynb)_](https://github.com/awandzilak/LogPPrediction/blob/main/clean.ipynb)
Approximately 100,000 molecules' data were collected and thoroughly examined for missing values. Entries recorded at a pH other than the reference (7.0) were removed due to over 95% missing data. Additionally, those with about 60% missing data for multiple features simultaneously at the reference pH were also removed. Discrepancies between database and RDKit-generated descriptors were resolved by retaining the more accurate values for molecular descriptions.

### Exploratory data analysis [_(EDA.ipynb)_](https://github.com/awandzilak/LogPPrediction/blob/main/EDA.ipynb)
This section employs data visualization techniques and includes:
*  **Univariate analysis:** Investigating variable distributions, identifying outliers, and assessing skewness.
*  **Variable-to-target correlation:** Examining the relationship between variables and LogP.
*  **Descriptor correlations:**  Investigating correlations among various descriptors.
*  **Feature engineering:** In this phase, a set of new features was created, taking inspiration from the relationships observed in the Exploratory Data Analysis (EDA). These new features include polynomial features, rational difference features, and power-transformed features.

### Predictions
* Predictions of LogP values were generated using three algorithms: 
  *  Linear Regression [_(Linear Regression.ipynb)_](https://github.com/awandzilak/LogPPrediction/blob/main/LinearRegression.ipynb))
  *  Random Forest
  *  Neural Network [_(Neural Network.ipynb)_](https://github.com/awandzilak/LogPPrediction/blob/main/NeuralNetwork.ipynb))

*  The impact of including polynomial, rational difference, and power-transformed features on each model's performance was investigated.
*  To combat overfitting in MLP models, regularization techniques were employed.
*  Additionally, to manage the increased number of features resulting from feature engineering, Principal Component Analysis (PCA) and feature selection were utilized to improve the models' generalization performance.

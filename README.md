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
Data were sourced from the ZINC20 database (https://zinc20.docking.org/, _Irwin, Tang, Young, Dandarchuluun, Wong, Khurelbaatar, Moroz, Mayfield, Sayle, J. Chem. Inf. Model 2020, https://pubs.acs.org/doi/10.1021/acs.jcim.0c00675._). The information was extracted using the BeautifulSoup library and stored in an SQLite database, primarily comprising mostly topological parameters. Additional descriptors were generated based on Simplified Molecular Input Line Entry Specification (SMILES) strings of molecules, which contain information on atom connectivity, atomic numbers, and charge. RDKit package was employed for this purpose.

### Data cleaning [_(clean.ipynb)_](https://github.com/awandzilak/LogPPrediction/blob/main/clean.ipynb)
Data related to approximately 100,000 molecules was collected. A thorough examination was conducted to identify missing data. They  were checked for missing data, and in cases of data registered at a pH different from the reference over 95 % of data was missing, so these entries were eliminated.  Furthermore, entries containing properties recorded at the reference pH, with approximately 60% missing data for multiple features simultaneously, were also removed. In situations where disparities existed between data obtained directly from the database and data generated with RDKit, preference was given to values that provided a more accurate description of the molecules, and these values were retained. 

### Exploratory data analysis [_(EDA.ipynb)_](https://github.com/awandzilak/LogPPrediction/blob/main/EDA.ipynb)
This section employs data visualization techniques and includes:
*  **Univariate analysis:** Investigating variable distributions, identifying outliers, and assessing skewness.
*  **Variable-to-target correlation:** Examining the relationship between variables and LogP.
*  **Descriptor correlations:**  Investigating correlations among various descriptors.
*  **Feature engineering:** In this phase, a set of new features was created, taking inspiration from the relationships observed in the Exploratory Data Analysis (EDA). These new features include polynomial features, rational difference features, and power-transformed features.

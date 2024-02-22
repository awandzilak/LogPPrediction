# performance_metrics module
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score

global CV_train_R2, CV_train_R2_std, CV_test_R2, CV_test_R2_std, CV_train_MSE, CV_train_MSE_std, CV_test_MSE, CV_test_MSE_std

def get_best_scores(results, r):
    """
    the function extracts and assigns specific performance metrics (mean and std of MSE and R2)
    based on GridSearchCV results (data in the r-th row)
    """
    global CV_train_R2, CV_train_R2_std, CV_test_R2, CV_test_R2_std, CV_train_MSE, CV_train_MSE_std, CV_test_MSE, CV_test_MSE_std
    
    CV_train_R2 = results['mean_train_R-squared'][r]
    CV_train_R2_std = results['std_train_R-squared'][r]
    CV_test_R2 = results['mean_test_R-squared'][r]
    CV_test_R2_std = results['std_test_R-squared'][r]
    CV_train_MSE = results['mean_train_MSE'][r]
    CV_train_MSE_std = results['std_train_MSE'][r]
    CV_test_MSE = results['mean_test_MSE'][r]
    CV_test_MSE_std = results['std_test_MSE'][r]
    
def print_CV_scores():
    """
    the function prints specific performance metrics (mean and std of MSE and R2)
    """
    print('Results obtained from \033[1mGridSearchCV on the training-validation set\033[0m:')
    print()
    print(f'Training set R2 score: {CV_train_R2:.4f} ({CV_train_R2_std:.4f})')
    print(f'Test set R2 score: \033[1m{CV_test_R2:.4f}\033[0m ({CV_test_R2_std:.4f})')
    print()
    print(f'Training set MSE score: {CV_train_MSE:.4f} ({CV_train_MSE_std:.4f})')
    print(f'Test set MSE score: {CV_test_MSE:.4f} ({CV_test_MSE_std:.4f})')
    
def adjusted_r2_score(y_true, y_pred, X):
    """
    the function calculates adjusted R2 score
    """    
    # calculate adjusted R2 score based on:
    n_features = len(X.columns) # the number of features
    r2 = r2_score(y_true, y_pred) # regular r2 score
    n = len(y_true) # the number of data points
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - n_features - 1)
    
    return adjusted_r2

def get_test_scores(y, y_pred, y_test, y_test_pred, X): 
    """
    the function calculates specific performance metrics (mean and std of MSE and Adjusted-R2)
    """
    global train_adjusted_R2, test_adjusted_R2, train_MSE, test_MSE
    
    train_adjusted_R2 = adjusted_r2_score(y, y_pred, X)
    test_adjusted_R2 = adjusted_r2_score(y_test, y_test_pred, X)
    train_MSE = -mean_squared_error(y, y_pred)
    test_MSE = -mean_squared_error(y_test, y_test_pred)

def print_test_scores():
    """
    the function prints specific performance metrics (mean and std of MSE and Adjusted-R2)
    """
    print('Results obtained from the \033[1mtraining-validation and the unseen test set\033[0m:')
    print()
    print(f'Training set adjusted R2 score: {train_adjusted_R2:.4f})')
    print(f'Test set adjusted R2 score: \033[1m{test_adjusted_R2:.4f}\033[0m)')
    print()
    print(f'Training set MSE score: {train_MSE:.4f})')
    print(f'Test set MSE score: {test_MSE:.4f})')

def add_scores(column_name):
    """
    the function adds performance metrics calculated before to a dataframe
    """
    LM_scores[column_name] = [CV_train_R2, CV_train_R2_std, CV_train_MSE, CV_train_MSE_std, train_adjusted_R2, train_MSE, CV_test_R2, CV_test_R2_std, CV_test_MSE, CV_test_MSE_std, test_adjusted_R2, test_MSE]
    
def visualize_fit(y, y_pred):
    """
    the function visualizes predicted values as compared to actual values
    """
    fig, (ax1, ax2, ax3) = plt.subplots(1,3, figsize=(12,4))

    # visualise correlation between actual and predicted values
    sns.scatterplot(x=y, y=y_pred, ax=ax1) 
    sns.lineplot(x=[min(y), max(y)], y=[min(y), max(y)], color='gold', linewidth=3, ax=ax1) 
    ax1.set_xlabel('actual')
    ax1.set_ylabel('predicted')
    ax1.title.set_text('predicted vs. actual')
    
    # visualise residuals
    residuals = (y - y_pred).sample(10000)
    sns.scatterplot(x=y, y=residuals, ax=ax2) 
    ax2.set_xlabel('actual')
    ax2.set_ylabel('residual')
    ax2.title.set_text('residual = actual - predicted')

    # visualise residuals
    sns.histplot(residuals, bins=100, ax=ax3) 
    ax3.set_xlabel('residual')
    ax3.title.set_text('Residuals distribution')

    plt.show()
    
def get_row_index(conditions):
    """
    the function finds index of the row with specified parameters
    """
    # Initialize a boolean mask
    mask = pd.Series([True] * len(results), index=results.index)

    # Apply conditions from the dictionary
    for column, value in conditions.items():
        column_name = 'param_' + column
        mask = mask & ((results[column_name] == value) | ((results[column_name].isna()) & (value is None)))

    # Find the index of the first row that satisfies all conditions
    matching_index = results.loc[mask].index[0] if any(mask) else None
    
    return matching_index
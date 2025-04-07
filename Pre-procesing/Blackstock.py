from datetime import timedelta

import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from sklearn.feature_selection import mutual_info_regression

import matplotlib.pyplot as plt
import seaborn as sns


def iterate_over_months(start,end):
    for i in range(0, 12):
         sns.set_theme(style='darkgrid', palette='flare')
         plt.plot(Blackstock.loc[start:end].index, Blackstock['wl_value'].loc[start:end],
             color='blue')
         plt.scatter(Blackstock.loc[start:end].index,Blackstock['pp_value'].loc[start:end],color='teal')
         plt.title('Scatter plot of Water and Precipitation level')
         plt.show()
         start += timedelta(days=30)
         end += timedelta(days=30)

def cross_correlation(df,x,y):
    cross_corr = np.correlate(df['wl_value'] - np.mean(df['wl_value']),
                              df['pp_value'] - np.mean(df['pp_value']), mode='full')
    lags = np.arange(-len(df['wl_value']) + 1, len(df['pp_value']))
    plt.plot(lags, cross_corr)
    plt.xlim(x,y)
    plt.xlabel("Lag")
    plt.ylabel("Cross-Correlation")
    plt.title("Cross-Correlation Function")
    plt.show()

def wl_vs_pp(df):
    sns.set_theme(style='darkgrid', palette='flare')
    plt.plot(df.index, df['wl_value'])
    plt.scatter(df.index, df['pp_value'])
    plt.title(
        'Scatter plot of Water and Precipitation level after extracting important years')
    plt.show()

# Data Pre-processing
#
Blackstock = pd.read_excel('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Pre-procesing/wl_pp.xlsx',sheet_name='Blackstock')
# print(Blackstock.head())
#
# # print(Blackstock.isna().sum())
# # Just 1 missing value in wl_value
#
# # import missingno as msno
# # msno.matrix(Blackstock)
#
Blackstock.dropna(inplace=True)
# print(Blackstock.isna().sum())
#
#
Blackstock = Blackstock.set_index('Timestamp')
# # print(Blackstock.index)
#
# # print(Blackstock[Blackstock['wl_value']<=0])
#
# # print((len(Blackstock[(Blackstock['wl_value']<=0)])/len(Blackstock))*100)
# # The rows with wl_value less than or equal to zero is less than 0.5% so we can drop them
#
Blackstock = Blackstock[~(Blackstock['wl_value']<=0)]
#
# # print((len(Blackstock[(Blackstock['pp_value']<=0)])/len(Blackstock))*100)
# # We can't drop the rows with pp_value less than zero because it is 95% of the data so
# # we need to impute the data.
#
#

# R,p = pearsonr(Blackstock['wl_value'],Blackstock['pp_value'])
# print("Pearson Correlation value in percentage",R*100)
#
# # Heatmap of the data
# # sns.heatmap(Blackstock.corr(),annot=True,linewidth=.5,fmt=".1f")
# # plt.title('Correlation matrix')
# # plt.show()
#
# # Checking max and min of every column for outlier before outlier removal
# # print('PP_value before outlier removal')
# # print(Blackstock['pp_value'].min())
# # print(Blackstock['pp_value'].max())
# # print('WL_value before outlier removal')
# # print(Blackstock['wl_value'].min())
# # print(Blackstock['wl_value'].max())
#
# # From all this visualization one thing is clear that data need  to go under
# # scaler transformation so we can work on it.
# from scipy.stats import zscore
from scipy.stats import iqr
#
# # Outlier removal
# print(iqr(Blackstock['wl_value']))
# Blackstock = Blackstock[(np.abs(zscore(Blackstock.select_dtypes(include=np.number))) < 3).all(axis=1)]
#
# print(iqr(Blackstock['wl_value']))
print(Blackstock.describe())
Blackstock = Blackstock[~(Blackstock['pp_value']>=25)]
Blackstock = Blackstock[~(Blackstock['wl_value'] < 1)]

# # Checking max and min of every column for outlier after outlier removal
print('PP_value after outlier removal')
print(Blackstock['pp_value'].min())
print(Blackstock['pp_value'].max())
print('WL_value after outlier removal')
print(Blackstock['wl_value'].min())
print(Blackstock['wl_value'].max())
#
# Sahil
Blackstock = Blackstock.resample('4D').mean().fillna(0)

def penalize_suspicious_water_increase(df, precip_col='pp_value', water_col='water_level', threshold_precip=0.2, max_water_change=0.5):

    df = df.copy()

    # Calculate water level change
    df['water_level_change'] = df[water_col].diff()

    # Shift precip up to align with *current row's* water level change
    df['prev_precip'] = df[precip_col].shift(1)

    # Identify suspicious cases:
    # Previous precip == 0.2 AND current water level change > 0.5
    condition = (df['prev_precip'] == threshold_precip) & (df['water_level_change'] > max_water_change)

    # Apply penalty by capping the water level change
    df.loc[condition, 'water_level_change'] = max_water_change

    return df

def drop_noise_rows(df, precip_col='pp_value', water_level_col='water_level'):

    df = df.copy()

    # Calculate water level change
    df['water_level_change'] = df[water_level_col].diff()

    # Previous precipitation (shifted by 1)
    df['prev_precip'] = df[precip_col].shift(1)

    # Condition: current water level increased but previous precipitation was zero
    condition = (df['water_level_change'] > 0) & (df['prev_precip'] == 0)

    # Drop these rows
    df_cleaned = df[~condition].copy()

    # Cleanup
    df_cleaned.drop(columns=['water_level_change', 'prev_precip'], inplace=True)

    return df_cleaned


def drop_rows_after_false_precip(df, precip_col='pp_value', water_col='water_level'):

    df = df.copy()

    # Compute water level change
    df['water_level_change'] = df[water_col].diff()

    # Identify rows where precipitation > 0
    precip_now = df[precip_col] > 0

    # Identify where water level drops in the next row
    water_drop_next = df['water_level_change'] < 0

    # Combine conditions — this marks the NEXT row for dropping
    rows_to_drop = precip_now & water_drop_next.shift(1).fillna(False)

    df_cleaned = df[~rows_to_drop].copy()

    # Optional cleanup
    df_cleaned.drop(columns=['water_level_change'], inplace=True)

    return df_cleaned

Blackstock_processed = penalize_suspicious_water_increase(Blackstock,'pp_value','wl_value')
Blackstock_processed = drop_noise_rows(Blackstock_processed,'pp_value','wl_value')
Blackstock_processed = drop_rows_after_false_precip(Blackstock_processed,'pp_value','wl_value')

cross_correlation(Blackstock_processed,-100,100)
# wl_vs_pp(Blackstock_processed)
R,p = pearsonr(Blackstock_processed['wl_value'],Blackstock_processed['pp_value'])
print(Blackstock_processed.corr())
print("Pearson Correlation value in percentage",R*100)

R, p = spearmanr(Blackstock_processed['wl_value'], Blackstock_processed['pp_value'].shift(periods=0,fill_value=0))
print("Spearman Correlation value in percentage", R * 100)

#
# # Heatmap of the data
# # sns.heatmap(Blackstock_scaled.corr(),annot=True,linewidth=.5,fmt=".1f")
# # plt.title('Correlation matrix after data preprocessing')
# # plt.show()
#

# # There is no linear dependency in data which is clearly visual from the graph and also
# # from the correlation matrix and pearson value, so we need to find non-linear dependancy.
from sklearn.feature_selection import mutual_info_regression
mi = mutual_info_regression(Blackstock_processed[['wl_value']], Blackstock_processed['pp_value'])
print(f'Mutual Information: {mi[0]}')
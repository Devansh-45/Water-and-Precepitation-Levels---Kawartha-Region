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
         plt.plot(PigeonRiverLotus.loc[start:end].index, PigeonRiverLotus['wl_value'].loc[start:end],
             color='blue')
         plt.scatter(PigeonRiverLotus.loc[start:end].index,PigeonRiverLotus['pp_value'].loc[start:end],color='teal')
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

# PigeonRiver Lotus

PigeonRiverLotus = pd.read_excel('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Pre-procesing/wl_pp.xlsx',sheet_name='Pigeon_lotus1')
# print(PigeonRiverLotus.head())

print('Missing value in the dataset')
print(PigeonRiverLotus.isna().sum())
# No missing value in the dataset


PigeonRiverLotus = PigeonRiverLotus.set_index('Timestamp')
# print(PigeonRiverLotus.index)

# print(PigeonRiverLotus[PigeonRiverLotus['wl_value']<=0])

# print((len(PigeonRiverLotus[(PigeonRiverLotus['wl_value']<=0)])/len(PigeonRiverLotus))*100)
# The rows with wl_value less than or equal to zero are only 2 so we can drop theem

PigeonRiverLotus = PigeonRiverLotus[~(PigeonRiverLotus['wl_value']<=0)]

# print((len(PigeonRiverLotus[(PigeonRiverLotus['pp_value']<0)])/len(PigeonRiverLotus))*100)
# We can drop the rows with pp_value less than zero because there are only 2 rows.

# print(PigeonRiverLotus[PigeonRiverLotus['pp_value']<0])

PigeonRiverLotus = PigeonRiverLotus[~(PigeonRiverLotus['pp_value']<0)]


# Correlation

R,p = pearsonr(PigeonRiverLotus['wl_value'],PigeonRiverLotus['pp_value'])
print("Pearson Correlation value in percentage",R*100)

# Heatmap of the data
# sns.heatmap(PigeonRiverLotus.corr(),annot=True,linewidth=.5,fmt=".1f")
# plt.title('Correlation matrix')
# plt.show()

# Checking max and min of every column for outlier before outlier removal
print('PP_value before outlier removal')
print(PigeonRiverLotus['pp_value'].min())
print(PigeonRiverLotus['pp_value'].max())
print('WL_value before outlier removal')
print(PigeonRiverLotus['wl_value'].min())
print(PigeonRiverLotus['wl_value'].max())

# From all this visualization one thing is clear that data need  to go under
# scaler transformation so we can work on it.
from scipy.stats import zscore
from scipy.stats import iqr

# Outlier removal
print(iqr(PigeonRiverLotus['wl_value']))
print(PigeonRiverLotus.describe())
PigeonRiverLotus = PigeonRiverLotus[~(PigeonRiverLotus['pp_value']>=20)]
PigeonRiverLotus = PigeonRiverLotus[~(PigeonRiverLotus['wl_value'] >= 5)]

# PigeonRiverLotus = PigeonRiverLotus[(np.abs(zscore(PigeonRiverLotus.select_dtypes(include=np.number))) < 3).all(axis=1)]

# print(PigeonRiverLotus['pp_value'].mean())
# Checking max and min of every column for outlier after outlier removal
print('PP_value after outlier removal')
print(PigeonRiverLotus['pp_value'].min())
print(PigeonRiverLotus['pp_value'].max())
print('WL_value after outlier removal')
print(PigeonRiverLotus['wl_value'].min())
print(PigeonRiverLotus['wl_value'].max())
# Need to scale the data as the min and max only have difference of (1.2 in wl and 2.2
# in pp)

# Sahil
PigeonRiverLotus = PigeonRiverLotus.resample('4D').mean().fillna(0)

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

PigeonRiverLotus_preprocessed = penalize_suspicious_water_increase(PigeonRiverLotus,'pp_value','wl_value')
PigeonRiverLotus_preprocessed = drop_noise_rows(PigeonRiverLotus_preprocessed,'pp_value','wl_value')
PigeonRiverLotus_preprocessed = drop_rows_after_false_precip(PigeonRiverLotus_preprocessed,'pp_value','wl_value')

cross_correlation(PigeonRiverLotus_preprocessed,-10,10)

R,p = pearsonr(PigeonRiverLotus_preprocessed['wl_value'],PigeonRiverLotus_preprocessed['pp_value'].shift(periods=0,fill_value=0))
print(PigeonRiverLotus_preprocessed.corr())
print("Pearson Correlation value in percentage",R*100)

R, p = spearmanr(PigeonRiverLotus_preprocessed['wl_value'], PigeonRiverLotus_preprocessed['pp_value'].shift(periods=0,fill_value=0))
print("Spearman Correlation value in percentage", R * 100)

# Heatmap of the data
# sns.heatmap(PigeonRiverLotus_minmax.corr(),annot=True,linewidth=.5,fmt=".1f")
# plt.title('Correlation matrix after data preprocessing')
# plt.show()

# Scatter plot between wl_value and pp_value
# sns.set_theme(style='darkgrid',palette='flare')
# sns.scatterplot(data=PigeonRiverLotus_minmax,x='wl_value',y='pp_value')
# plt.title('Wl vs Precipitation value')
# plt.show()

# There is no linear dependency in data which is clearly visual from the graph and also
# from the correlation matrix and pearson value, so we need to find non-linear dependancy.
from sklearn.feature_selection import mutual_info_regression
mi = mutual_info_regression(PigeonRiverLotus_preprocessed[['wl_value']], PigeonRiverLotus_preprocessed['pp_value'].shift(periods=0,fill_value=0))
print(f'Mutual Information: {mi[0]}')



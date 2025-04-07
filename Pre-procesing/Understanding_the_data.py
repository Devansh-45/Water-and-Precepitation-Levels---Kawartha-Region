from datetime import timedelta

import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from sklearn.feature_selection import mutual_info_regression


# MariposaBrook
# Removed values less than 0 and null.
# Done Standard scaling and Min max scaling
# Removed rows with pp_value is less than zero
# Again done min_max and standard scaling and min max
# Distribute the data in the set of 4-5 years to understand the data
# Use lag -1 in pp to find corr because the affect of pp occur on wl in the next row


# Notes
# The data is complete garbage there are years where the Precipitation value is zero still
# there are changes in the wl value due to other factors, now if the pp is zero and wl
# decreases then it makes sense but if it increases due to some other reason then we
# need to drop it because it messes the correlation between variables
# Just a thought instead of dropping the data where water level increases due to external factors
# we can use a impacting factor which only applies where water level increases and
# precipitation is zero, it might cause data integrity issues, so..


MariposaBrook = pd.read_excel(
    '/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Pre-procesing/wl_pp.xlsx',
    sheet_name='MariposaBrook')

# print(MariposaBrook.head())
# print(MariposaBrook.info())
print(MariposaBrook.isna().sum())
# Just 15 missing value in wl_value

MariposaBrook['Timestamp'] = pd.to_datetime(MariposaBrook['Timestamp'])

import matplotlib.pyplot as plt

# import missingno as msno
# msno.matrix(MariposaBrook)
# plt.title('Missing value matrix')
# plt.show()

MariposaBrook.dropna(inplace=True)
print(MariposaBrook.isna().sum())

import seaborn as sns

MariposaBrook = MariposaBrook.set_index('Timestamp')
# print(MariposaBrook.index)

# print(MariposaBrook[MariposaBrook['wl_value']<=0])

print((len(MariposaBrook[(MariposaBrook['wl_value'] <= 0)]) / len(MariposaBrook)) * 100)
# The rows with wl_value less than or equal to zero is less than 0.13% so we can drop them

MariposaBrook = MariposaBrook[~(MariposaBrook['wl_value'] <= 0)]
# print(MariposaBrook[MariposaBrook['wl_value']<=0])

print((len(MariposaBrook[(MariposaBrook['pp_value'] <= 0)]) / len(MariposaBrook)) * 100)
# The rows with pp_value less than zero is less than 0.00021% so we can drop them

MariposaBrook = MariposaBrook[~(MariposaBrook['pp_value'] < 0)]
# print(MariposaBrook[MariposaBrook['pp_value']<=0])

print("The length of the new dataset is now reduced from 465k to", len(MariposaBrook))

print("Percentage of the Precipitation value equal to 0.2 in dataset",
      (len(MariposaBrook[(MariposaBrook['pp_value'] == 0.2)]) / len(MariposaBrook)) * 100)
# MariposaBrook.to_excel('Temp.xlsx',sheet_name='Mariposa_new')

# Checking max and min of every column for outlier before outlier removal
print('PP_value before outlier removal')
print(MariposaBrook['pp_value'].min())
print(MariposaBrook['pp_value'].max())
print('WL_value before outlier removal')
print(MariposaBrook['wl_value'].min())
print(MariposaBrook['wl_value'].max())
# print(MariposaBrook.describe())
# From all this visualization one thing is clear that data need  to go under
# scaler transformation so we can work on it.
from scipy.stats import zscore
from scipy.stats import iqr

# Outlier removal
print(iqr(MariposaBrook['wl_value']))
# We can't use the traditional method of outlier removal with z-score greater than 3
# because 99% of data has value of pp_value 0, so if we use traditional method,
# then it will remove all the pp_value of greater than 1, and it is not useful.
# we are gonna use the z score = 20 to get the pp_value upto 7 mm
# After that we are going to remove the wl value less than 1.79 mm because that is maximum
# value under after removal of outlier with z score of 3
# MariposaBrook = MariposaBrook[(np.abs(zscore(MariposaBrook.select_dtypes(include=np.number))) <3).all(axis=1)]
print(MariposaBrook.describe())

MariposaBrook = MariposaBrook[~(MariposaBrook['pp_value']==85.4)]
MariposaBrook = MariposaBrook[~(MariposaBrook['wl_value'] < 1.79)]

# Checking max and min of every column for outlier after outlier removal
print('PP_value after outlier removal')
print(MariposaBrook['pp_value'].min())
print(MariposaBrook['pp_value'].max())
print('WL_value after outlier removal')
print(MariposaBrook['wl_value'].min())
print(MariposaBrook['wl_value'].max())


# Had a hunch regarding 0.2 as data recording error because after removal of rows with zero
# precipitation levels, I had 60% of new data has value of 0.2. I had done the calculation
# before but, I will do it again below just to clearify
# temp_0 = MariposaBrook[~(MariposaBrook['pp_value']<=0)]
# print(len(temp_0[(temp_0['pp_value']==0.2)])/len(temp_0)*100)


# Calculating the total number of rows in each year which has non zero
# precipitation value
Temp = MariposaBrook[MariposaBrook['pp_value']>0]
print(Temp.groupby(Temp.index.year).count())
print("Length of the dataset before removal of non-useful years",len(MariposaBrook))
# Now, If the year has less than 90 days of Precipitation then we can drop that year, because
# it definately has data integrity issues, let's on safe side only drop years which has less
# than 60 days of precipitation. years 1986,1993,1994,1997 should be dropped
# MariposaBrook = pd.concat([MariposaBrook.loc['1987-01-01':'1992-12-31'],MariposaBrook.loc['1995-01-01':]],join='inner')
# Temp = MariposaBrook[MariposaBrook['pp_value']>0]
# print(Temp.groupby(Temp.index.year).count())
# print(MariposaBrook.head())
print("Length of the dataset after removal of non-useful years",len(MariposaBrook))
print(MariposaBrook.info())
# Checking using loc just to be sure that every year is dropped
# print(MariposaBrook.loc['1993':'1994'],MariposaBrook.loc['1986':'1987 01-01'].head(2),MariposaBrook.loc['1997':'1998 01-01'].head(2))


# Iterate over the data to only extract useful months and remove the ludicrous data.
# years_list = ['1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024']
# end_list = ['1986-12-31','1987-12-31','1988-12-31','1989-12-31','1990-12-31','1991-12-31','1992-12-31','1993-12-31','1994-12-31','1995-12-31','1996-12-31','1997-12-31','1998-12-31','1999-12-31','2000-12-31','2001-12-31','2002-12-31','2003-12-31','2004-12-31','2005-12-31','2006-12-31','2007-12-31','2008-12-31','2009-12-31','2010-12-31','2011-12-31','2012-12-31','2013-12-31','2014-12-31','2015-12-31','2016-12-31','2017-12-31','2018-12-31','2019-12-31','2020-12-31','2021-12-31','2022-12-31','2023-12-31','2024-12-31']
# # Change in pp and wl w.r.t time
# for i,j in zip(years_list,end_list) :
#     sns.set_theme(style='darkgrid', palette='flare')
#     plt.plot(MariposaBrook.loc[i:j].index, MariposaBrook['wl_value'].loc[i:j],
#              color='blue')
#     plt.scatter(x=MariposaBrook.loc[i:j].index,y=MariposaBrook['pp_value'].loc[i:j],color='teal')
#     plt.title('Scatter plot of Water and Precipitation level of'+i+"th year")
#     plt.show()


def iterate_over_months(start,end):
    for i in range(0, 12):
         sns.set_theme(style='darkgrid', palette='flare')
         plt.plot(MariposaBrook.loc[start:end].index, MariposaBrook['wl_value'].loc[start:end],
             color='blue')
         plt.scatter(MariposaBrook.loc[start:end].index,MariposaBrook['pp_value'].loc[start:end],color='teal')
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


# Iterate over months of 1986 year
start = pd.to_datetime('1986-01-01')
end =  pd.to_datetime('1986-01-31')
# iterate_over_months(start,end)
MariposaBrook_1986 = MariposaBrook.loc['1986-01-01':'1986-12-31']
print(MariposaBrook_1986.head(),MariposaBrook_1986.tail())
MariposaBrook_1986 = MariposaBrook_1986.replace({'pp_value':0.2},0)
# wl_vs_pp(MariposaBrook_1986)

# Using cross-correlation function to check that if one data series lag or lead another
# cross_correlation(MariposaBrook_1986)

R, p = pearsonr(MariposaBrook_1986['wl_value'], MariposaBrook_1986['pp_value'].shift(periods=0).fillna(0))
print("Pearson Correlation value in percentage of year 1986", R * 100)

R, p = spearmanr(MariposaBrook_1986['wl_value'], MariposaBrook_1986['pp_value'].shift(periods=0).fillna(0))
print("Spearman Correlation value in percentage of year 1986", R * 100)


mi = mutual_info_regression(MariposaBrook_1986[['pp_value']].shift(periods=0,fill_value=0), MariposaBrook_1986['wl_value'], random_state=42)
print(f'Mutual Information of year 1986: {mi[0]}')


# Iterate over months of 1987
start = pd.to_datetime('1987-01-01')
end =  pd.to_datetime('1987-01-31')
# iterate_over_months(start,end)

# UnImportant days and months
# 09-09,10-30,11-18,11-09
MariposaBrook_1987 = MariposaBrook.loc['1987-01-01':'1987-12-31']
# print(MariposaBrook_1987.loc['1987-09-09'])
# print(MariposaBrook_1987.loc['1987-10-30'])
# print(MariposaBrook_1987.loc['1987-11-18'])
# print(MariposaBrook_1987.loc['1987-11-09'])
MariposaBrook_1987 = MariposaBrook_1987.drop(pd.to_datetime(['1987-09-09 01:00:00','1987-09-09 02:00:00','1987-10-30 06:00:00','1987-10-30 21:00:00','1987-11-18 00:00:00','1987-11-18 01:00:00','1987-11-18 07:00:00','1987-11-18 08:00:00','1987-11-18 09:00:00','1987-11-18 12:00:00','1987-11-18 17:00:00'
                                                             ,'1987-11-09 00:00:00','1987-11-09 01:00:00','1987-11-09 02:00:00','1987-11-09 03:00:00','1987-11-09 04:00:00','1987-11-09 07:00:00','1987-11-09 08:00:00','1987-11-09 09:00:00','1987-11-09 10:00:00','1987-11-09 11:00:00','1987-11-09 12:00:00']))
# MariposaBrook_1987= MariposaBrook_1987[~(MariposaBrook_1987['pp_value']>=10)]
# print(MariposaBrook_1987.head(),MariposaBrook_1987.tail())
# MariposaBrook_1987 = MariposaBrook_1987[~(MariposaBrook_1987['pp_value']<=0.2)]
MariposaBrook_1987 = MariposaBrook_1987.replace({'pp_value':0.2},0)
# wl_vs_pp(MariposaBrook_1987)

# Using cross-correlation function to check that if one data series lag or lead another
# cross_correlation(MariposaBrook_1987)


R, p = pearsonr(MariposaBrook_1987['wl_value'], MariposaBrook_1987['pp_value'].shift(periods=-2).fillna(0))
print("Pearson Correlation value in percentage of 1987", R * 100)

R, p = spearmanr(MariposaBrook_1987['wl_value'], MariposaBrook_1987['pp_value'].shift(periods=-2).fillna(0))
print("Spearman Correlation value in percentage of 1987", R * 100)


from sklearn.feature_selection import mutual_info_regression

mi = mutual_info_regression(MariposaBrook_1987[['pp_value']].shift(periods=-2,fill_value=0), MariposaBrook_1987['wl_value'], random_state=42)
print(f'Mutual Information of 1987: {mi[0]}')


# Iterate over months of 1988
start = pd.to_datetime('1988-01-01')
end =  pd.to_datetime('1988-01-31')
# iterate_over_months(start,end)

# UImportant days and months
# 02-01,*03-27,06,07,08,09,10-11
MariposaBrook_1988 = MariposaBrook.loc['1988-01-01':'1988-12-31']
# print(MariposaBrook_1988.loc['1988-02-01'])
# print(MariposaBrook_1988.loc['1988-03-27'])
MariposaBrook_1988 = MariposaBrook_1988.drop(pd.to_datetime(['1988-02-01 02:00:00','1988-02-01 03:00:00','1988-02-01 04:00:00',
                                                             '1988-02-01 06:00:00','1988-03-27 04:00:00','1988-03-27 05:00:00','1988-03-27 08:00:00']))

MariposaBrook_1988.loc['1988-06-01':'1988-11-09','pp_value'] = 0
# print(MariposaBrook_1988.loc['1988-06-01':'1988-06-30'])


# MariposaBrook_1988= MariposaBrook_1988[~(MariposaBrook_1988['pp_value']>=10)]
MariposaBrook_1988 = MariposaBrook_1988.replace({'pp_value':0.2},0)
# wl_vs_pp(MariposaBrook_1988)

# Using cross-correlation function to check that if one data series lag or lead another
# cross_correlation(MariposaBrook_1988)

R, p = pearsonr(MariposaBrook_1988['wl_value'], MariposaBrook_1988['pp_value'].shift(periods=-3).fillna(0))
print("Pearson Correlation value in percentage of 1988", R * 100)

R, p = spearmanr(MariposaBrook_1988['wl_value'], MariposaBrook_1988['pp_value'].shift(periods=-3).fillna(0))
print("Spearman Correlation value in percentage of 1988", R * 100)


mi = mutual_info_regression(MariposaBrook_1988[['pp_value']].shift(periods=-3,fill_value=0), MariposaBrook_1988['wl_value'], random_state=42)
print(f'Mutual Information of 1988: {mi[0]}')


# Iterate over months of 1989
start = pd.to_datetime('1989-01-01')
end =  pd.to_datetime('1989-01-31')
# iterate_over_months(start,end)

# UImportant days and months
# 05,06-18,08,end,09,**11-09,08-11
MariposaBrook_1989 = MariposaBrook.loc['1989-01-01':'1989-12-31']
# print(MariposaBrook_1988.loc['1988-02-01'])
# print(MariposaBrook_1988.loc['1988-03-27'])
# MariposaBrook_1988 = MariposaBrook_1988.drop(pd.to_datetime(['1988-02-01 02:00:00','1988-02-01 03:00:00','1988-02-01 04:00:00',
#                                                              '1988-02-01 06:00:00','1988-03-27 04:00:00','1988-03-27 05:00:00','1988-03-27 08:00:00']))

MariposaBrook_1989.loc['1989-05-11':'1989-06-18','pp_value'] = 0
MariposaBrook_1989.loc['1989-06-25':'1989-06-30','pp_value'] = 0
MariposaBrook_1989.loc['1989-08-01':'1989-08-31','pp_value'] = 0
MariposaBrook_1989.loc['1989-09-01':'1989-09-03','pp_value'] = 0
# MariposaBrook_1989.loc['1989-09-01':'1989-09-21','pp_value'] = 0
MariposaBrook_1989.loc['1989-11-09':'1989-11-30','pp_value'] = 0
# print(MariposaBrook_1988.loc['1988-06-01':'1988-06-30'])
print(MariposaBrook_1989.loc['1989-08-11'])

# MariposaBrook_1988= MariposaBrook_1988[~(MariposaBrook_1988['pp_value']>=2)]
MariposaBrook_1989 = MariposaBrook_1989.replace({'pp_value':0.2},0)
# MariposaBrook_1989 = MariposaBrook_1989[~(MariposaBrook_1989['pp'])]
# wl_vs_pp(MariposaBrook_1989)

# Using cross-correlation function to check that if one data series lag or lead another
# cross_correlation(MariposaBrook_1989)

R, p = pearsonr(MariposaBrook_1989['wl_value'], MariposaBrook_1989['pp_value'].shift(periods=-36).fillna(0))
print("Pearson Correlation value in percentage of 1989", R * 100)

R, p = spearmanr(MariposaBrook_1989['wl_value'], MariposaBrook_1989['pp_value'].shift(periods=-36).fillna(0))
print("Spearman Correlation value in percentage of 1989", R * 100)


mi = mutual_info_regression(MariposaBrook_1989[['pp_value']].shift(periods=-22,fill_value=0), MariposaBrook_1989['wl_value'], random_state=42)
print(f'Mutual Information of 1989: {mi[0]}')


# Wl value Analysis
# sns.set_theme(style='darkgrid',palette='flare')
# fig ,ax = plt.subplots(2,2)
# sns.scatterplot(data=MariposaBrook.loc['1992-07-17 20:00:00':'1997-07-17 12:00:00'],x='Timestamp',y='wl_value',ax=ax[1,0])
# ax[1,0].set_title('Scatter plot')
# ax[1,0].tick_params("x",rotation=90)
# sns.histplot(data=MariposaBrook,x='wl_value',ax=ax[0,0],kde=True)
# ax[0,0].set_title('Histogram')
# sns.boxenplot(x=MariposaBrook['wl_value'],ax=ax[0,1])
# ax[0,1].set_title('Boxen Plot')
# sns.lineplot(data=MariposaBrook['wl_value'].loc['1992-07-17 20:00:00':'1997-07-17 12:00:00'],ax=ax[1,1])
# ax[1,1].set_title('Line plot')
# ax[1,1].tick_params("x",rotation=90)
# fig.suptitle('Water level value Analysis for MariposaBrook',fontweight='bold',fontsize=16)
# plt.show()

# PP value Analysis
# sns.set_theme(style='darkgrid',palette='flare')
# fig ,ax = plt.subplots(2,2,figsize=(10,12))
# sns.scatterplot(data=MariposaBrook.loc['1992-07-17 20:00:00':'1997-07-17 12:00:00'],x='Timestamp',y='pp_value',ax=ax[1,0])
# ax[1,0].set_title('Scatter plot')
# ax[1,0].tick_params("x",rotation=90)
# sns.histplot(data=MariposaBrook,x='pp_value',ax=ax[0,0],kde=True)
# ax[0,0].set_title('Histogram')
# sns.boxenplot(x=MariposaBrook['pp_value'],ax=ax[0,1])
# ax[0,1].set_title('Boxen Plot')
# sns.lineplot(data=MariposaBrook['pp_value'].loc['1992-07-17 20:00:00':'1997-07-17 12:00:00'],ax=ax[1,1])
# ax[1,1].set_title('Line plot')
# ax[1,1].tick_params("x",rotation=90)
# fig.suptitle('Precipitation level value Analysis for MariposaBrook',fontweight='bold',fontsize=16)
# plt.show()

# Scatter plot between wl_value and pp_value
# sns.set_theme(style='darkgrid',palette='flare')
# sns.scatterplot(data=MariposaBrook,x='wl_value',y='pp_value')
# plt.title('Wl vs Precipitation value')
# plt.show()

# MariposaBrook['pp_value'].replace(0.2,0,inplace=True)

# Using cross-correlation function to check that if one data series lag or lead another
# cross_correlation(MariposaBrook)
# As the lag is significant at x=0 the series move together in real time


# Correlation

# R, p = pearsonr(MariposaBrook['wl_value'], MariposaBrook['pp_value'])
# print("Pearson Correlation value in percentage", R * 100)
#
# R, p = spearmanr(MariposaBrook['wl_value'], MariposaBrook['pp_value'])
# print("Spearman Correlation value in percentage", R * 100)

# Heatmap of the data
# sns.heatmap(MariposaBrook.corr(),annot=True,linewidth=.5,fmt=".1f")
# plt.title('Correlation matrix')
# plt.show()


# # Need to scale the data as the min and max only have difference of (1.2 in wl and 2.2
# # in pp)


# # Min-Max sampling
# from sklearn.preprocessing import MinMaxScaler
#
# min_max = MinMaxScaler(feature_range=(-1,1))
# MariposaBrook_minmax = min_max.fit_transform(MariposaBrook)
# print(type(MariposaBrook_minmax))
# MariposaBrook_minmax = pd.DataFrame(MariposaBrook_minmax)
# MariposaBrook_minmax['Timestamp']  = MariposaBrook.index
# print(MariposaBrook_minmax.head())
#
# MariposaBrook_minmax.rename(columns={0:'wl_value',1:'pp_value'},inplace=True)
# print(MariposaBrook_minmax.head())
#
# print(MariposaBrook_minmax.info())
# MariposaBrook_minmax.set_index('Timestamp',inplace=True)

# We don't need min_max scaling as our data is going to go under normalization method

# MariposaBrook_minmax = MariposaBrook_minmax.asfreq('M')
# MariposaBrook_minmax =MariposaBrook_minmax[MariposaBrook_minmax['pp_value']>0]
# The precipitation data after min-max scaling still follows the unusual distribution,
# need to try some normalization method to scale the pp_value and remove minmax
# Now, we have already used min-max scaling from (-1,1), so we can't use log, square root
# and Box-cox transformation the options left are ye0-johnson, zscore and Quantile Transformation
# We are gonna use yeo-johnson on wl_value because our data is approx normal
# And Quantile transform for the pp_value because it is extreme case.
## As, I have remove min max I can try to use log,sqrt and box-cox

# MariposaBrook_minmax = MariposaBrook_minmax[~(MariposaBrook_minmax['pp_value']<=0)]

# 17,25,27, 31,33,38,42
MariposaBrook = MariposaBrook.resample('42D').mean().fillna(0)
    # Removing noise,and fine tuning the data

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

MariposaBrook_minmax = penalize_suspicious_water_increase(MariposaBrook,'pp_value','wl_value')
MariposaBrook_minmax = drop_noise_rows(MariposaBrook_minmax,'pp_value','wl_value')
MariposaBrook_minmax = drop_rows_after_false_precip(MariposaBrook_minmax,'pp_value','wl_value')
# from sklearn.preprocessing import PowerTransformer
#
# pt = PowerTransformer()
#
# MariposaBrook_minmax['wl_value'] = pt.fit_transform(MariposaBrook_minmax['wl_value'].values.reshape(-1, 1))

# Wl value Analysis after data preprocessing
# sns.set_theme(style='darkgrid',palette='flare')
# fig ,ax = plt.subplots(2,2)
# sns.scatterplot(data=MariposaBrook_minmax.loc['1988-07-17 20:00:00':'1992-07-17 12:00:00'],x='Timestamp',y='wl_value',ax=ax[1,0])
# ax[1,0].set_title('Scatter plot')
# ax[1,0].tick_params("x",rotation=90)
# sns.histplot(data=MariposaBrook_minmax,x='wl_value',ax=ax[0,0],kde=True)
# ax[0,0].set_title('Histogram')
# sns.boxenplot(x=MariposaBrook_minmax['wl_value'],ax=ax[0,1])
# ax[0,1].set_title('Boxen Plot')
# sns.lineplot(data=MariposaBrook_minmax['wl_value'].loc['1997-07-17 20:00:00':'2005-07-17 12:00:00'],ax=ax[1,1])
# ax[1,1].set_title('Line plot')
# ax[1,1].tick_params("x",rotation=90)
# fig.suptitle('Water level value Analysis for MariposaBrook after Data Preprocessing',fontweight='bold',fontsize=16)
# plt.show()

# Precipitation Transformation
# from sklearn.preprocessing import QuantileTransformer
#
#
# unique_years = len(pd.unique(MariposaBrook_minmax.index.year))
# qt = QuantileTransformer(n_quantiles=unique_years, random_state=42, output_distribution='normal')
# #
# MariposaBrook_minmax['pp_value'] = qt.fit_transform(MariposaBrook_minmax['pp_value'].values.reshape(-1, 1))

# PP value Analysis after data preprocessing
# sns.set_theme(style='darkgrid',palette='flare')
# fig ,ax = plt.subplots(2,2)
# sns.scatterplot(data=MariposaBrook_minmax.loc['2001-07-17 20:00:00':'2002-07-17 12:00:00'],x='Timestamp',y='pp_value',ax=ax[1,0])
# ax[1,0].set_title('Scatter plot')
# ax[1,0].tick_params("x",rotation=90)
# sns.histplot(data=MariposaBrook_minmax,x='pp_value',ax=ax[0,0],kde=True)
# ax[0,0].set_title('Histogram')
# sns.boxenplot(x=MariposaBrook_minmax['pp_value'],ax=ax[0,1])
# ax[0,1].set_title('Boxen Plot')
# sns.lineplot(data=MariposaBrook_minmax['pp_value'].loc['1988-07-17 20:00:00':'1992-07-17 12:00:00'],ax=ax[1,1])
# ax[1,1].set_title('Line plot')
# ax[1,1].tick_params("x",rotation=90)
# fig.suptitle('Precipitation level value Analysis for MariposaBrook after Data Preprocessing',fontweight='bold',fontsize=16)
# plt.show()

# from statsmodels.tsa.seasonal import STL
#
# MariposaBrook_minmax = MariposaBrook_minmax.resample('3W').mean().fillna(0)
#
# stl = STL(MariposaBrook_minmax['wl_value'],seasonal=13)
# result = stl.fit()
#
# MariposaBrook_minmax['wl_value'] = MariposaBrook_minmax['wl_value'] - result.seasonal

# cross_correlation(MariposaBrook_minmax,-10,10)
# wl_vs_pp(MariposaBrook_minmax)

R, p = pearsonr(MariposaBrook_minmax['wl_value'], MariposaBrook_minmax['pp_value'].shift(periods=0,fill_value=0))
print(MariposaBrook_minmax.corr())
print("Pearson Correlation value in percentage", R * 100)
#
R, p = spearmanr(MariposaBrook_minmax['wl_value'], MariposaBrook_minmax['pp_value'].shift(periods=0,fill_value=0))
print("Spearman Correlation value in percentage", R * 100)

# Heatmap of the data
# sns.heatmap(MariposaBrook_minmax.corr(),annot=True,linewidth=.5,fmt=".1f")
# plt.title('Correlation matrix after data preprocessing')
# plt.show()

# Scatter plot between wl_value and pp_value
# sns.set_theme(style='darkgrid',palette='flare')
# sns.scatterplot(data=MariposaBrook_minmax,x='wl_value',y='pp_value')
# plt.title('Wl vs Precipitation value')
# plt.show()
#
# # There is no linear dependency in data which is clearly visual from the graph and also
# # from the correlation matrix and pearson value, so we need to find non-linear dependancy.



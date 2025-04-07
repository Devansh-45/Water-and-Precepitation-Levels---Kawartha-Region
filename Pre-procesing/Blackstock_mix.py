import pandas as pd
import numpy as np
from numpy.ma.extras import unique

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


# wl_blackstock = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Blackstock-WSC/Blackstock-WL_2006-2016.csv')
#
# # convert the timestamp column into date-time
# wl_blackstock['Timestamp'] = pd.DatetimeIndex(wl_blackstock['Timestamp'])
# print(wl_blackstock.info())
#
# wl_blackstock.rename(columns={'Value':'wl_value'},inplace=True)
# wl_blackstock.drop(columns=['ts_name','ts_id','Units','station_name','station_id'],inplace=True)
#
# wl_blackstock = wl_blackstock[wl_blackstock['Timestamp']>='2016-11-04 05:00:00']
# print(wl_blackstock.head(10))
#
# wl_blackstock_2 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Blackstock-WSC/Blackstock-WL_2017-2014.csv')
#
# wl_blackstock_2['Timestamp'] = pd.DatetimeIndex(wl_blackstock_2['Timestamp'])
# print(wl_blackstock_2.info())
#
# wl_blackstock_2.rename(columns={'Value':'wl_value'},inplace=True)
# wl_blackstock_2.drop(columns=['ts_name','ts_id','Units','station_name','station_id'],inplace=True)
#
# wl_f_blackstock = pd.concat([wl_blackstock,wl_blackstock_2])
# print(wl_f_blackstock.head())
#
# pp_blackstock = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Blackstock-WSC/Blackstock-PP_2016-2024.csv')
# pp_blackstock['Timestamp'] = pd.DatetimeIndex(pp_blackstock['Timestamp'])
# print(pp_blackstock.info())
#
# pp_blackstock.rename(columns={'Value':'pp_value'},inplace=True)
# pp_blackstock.drop(columns=['ts_name','ts_id','Units','station_name','station_id'],inplace=True)
# print(pp_blackstock.head(5))
#
# wl_pp_blackstock = wl_f_blackstock.merge(pp_blackstock,how='inner',on='Timestamp')
# wl_pp_blackstock.drop(columns=['Unnamed: 0_x','Unnamed: 0_y'],inplace=True)
# print(wl_pp_blackstock.head())
# wl_pp_blackstock.to_excel('wl_pp.xlsx',sheet_name='Blackstock',index=False)


# wl_PigeonRiverL = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/PigeonRiver-Lotus/PigeonRiverL-WL_2005-2016.csv')
#
# # convert the timestamp column into date-time
# wl_PigeonRiverL['Timestamp'] = pd.DatetimeIndex(wl_PigeonRiverL['Timestamp'])
# print(wl_PigeonRiverL.info())
#
# wl_PigeonRiverL.rename(columns={'Value':'wl_value'},inplace=True)
# wl_PigeonRiverL.drop(columns=['ts_name','ts_id','Units','station_name','station_id'],inplace=True)
#
# wl_PigeonRiverL = wl_PigeonRiverL[wl_PigeonRiverL['Timestamp']>='9/6/2005 10:00']
# print(wl_PigeonRiverL.head(10))
#
# wl_PigeonRiverL_2 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/PigeonRiver-Lotus/PigeonRiverL-WL_2017-2014.csv')
#
# wl_PigeonRiverL_2['Timestamp'] = pd.DatetimeIndex(wl_PigeonRiverL_2['Timestamp'])
# print(wl_PigeonRiverL_2.info())
#
# wl_PigeonRiverL_2.rename(columns={'Value':'wl_value'},inplace=True)
# wl_PigeonRiverL_2.drop(columns=['ts_name','ts_id','Units','station_name','station_id'],inplace=True)
#
# wl_f_PigeonRiverL = pd.concat([wl_PigeonRiverL,wl_PigeonRiverL_2])
#
#
# # Load and process the first dataset
# pp_PigeonRiverL = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/PigeonRiver-Lotus/PigeonRiverL-PP_2005-2016.csv')
# pp_PigeonRiverL['Timestamp'] = pd.DatetimeIndex(pp_PigeonRiverL['Timestamp'])
# print(pp_PigeonRiverL.info())
#
# pp_PigeonRiverL.rename(columns={'Value': 'pp_value'}, inplace=True)
# pp_PigeonRiverL.drop(columns=['ts_name', 'ts_id', 'Units', 'station_name', 'station_id'], inplace=True)
#
# # Load and process the second dataset
# pp_PigeonRiverL_2 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/PigeonRiver-Lotus/PigeonRiverL-PP_2017-2024.csv')
# pp_PigeonRiverL_2['Timestamp'] = pd.DatetimeIndex(pp_PigeonRiverL_2['Timestamp'])
# print(pp_PigeonRiverL_2.info())
#
# pp_PigeonRiverL_2.rename(columns={'Value': 'pp_value'}, inplace=True)
# pp_PigeonRiverL_2.drop(columns=['ts_name', 'ts_id', 'Units', 'station_name', 'station_id'], inplace=True)
#
# # Combine the two datasets
# pp_f_PigeonRiverL = pd.concat([pp_PigeonRiverL, pp_PigeonRiverL_2])
#
# wl_pp_pigeon = wl_f_PigeonRiverL.merge(pp_f_PigeonRiverL,how='inner',on='Timestamp')
# wl_pp_pigeon.drop(columns=['Unnamed: 0_x','Unnamed: 0_y'],inplace=True)
# print(wl_pp_pigeon.head())
# file_path = '/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Pre-procesing/wl_pp.xlsx'
#
# # Use ExcelWriter with mode='a' (append) and engine='openpyxl'
# with pd.ExcelWriter(file_path, mode='a', engine='openpyxl', if_sheet_exists='new') as writer:
#     wl_pp_pigeon.to_excel(writer, sheet_name="Pigeon_lotus", index=False)
#
# print("Data written to new sheet successfully!")


# Load and process Water Level (WL) data

# We cannot do this on personal laptop due to memory constraint so the below part is done on kaggle

# wl_MariposaBrook_1 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/MariposaBrook-WSC/MariposaBrook-WL_1986-1995.csv')
# wl_MariposaBrook_1['Timestamp'] = pd.to_datetime(wl_MariposaBrook_1['Timestamp'],format='mixed')
# print(wl_MariposaBrook_1.info())
# wl_MariposaBrook_1.rename(columns={'Value': 'wl_value'}, inplace=True)
# wl_MariposaBrook_1.drop(columns=['ts_name', 'ts_id', 'Units', 'station_name', 'station_id'], inplace=True)
# wl_MariposaBrook_1 = wl_MariposaBrook_1[wl_MariposaBrook_1['Timestamp']>='07/03/1986 7:00']
# print(wl_MariposaBrook_1.isna().sum())
# print(wl_MariposaBrook_1.head(20))

#
# wl_MariposaBrook_2 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/MariposaBrook-WSC/MariposaBrook-WL_1996-2005.csv')
# wl_MariposaBrook_2['Timestamp'] = pd.to_datetime(wl_MariposaBrook_2['Timestamp'],format='mixed')
# wl_MariposaBrook_2.rename(columns={'Value': 'wl_value'}, inplace=True)
# wl_MariposaBrook_2.drop(columns=['ts_name', 'ts_id', 'Units', 'station_name', 'station_id'], inplace=True)
# print(wl_MariposaBrook_2.info())
# #
# wl_MariposaBrook_3 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/MariposaBrook-WSC/MariposaBrook-WL_2006-2015.csv')
# wl_MariposaBrook_3['Timestamp'] = pd.to_datetime(wl_MariposaBrook_3['Timestamp'], format='mixed')
# wl_MariposaBrook_3.rename(columns={'Value': 'wl_value'}, inplace=True)
# wl_MariposaBrook_3.drop(columns=['ts_name', 'ts_id', 'Units', 'station_name', 'station_id'], inplace=True)
# print(wl_MariposaBrook_3.info())
# #
# wl_MariposaBrook_4 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/MariposaBrook-WSC/MariposaBrook-WL_2016-2024.csv')
# wl_MariposaBrook_4['Timestamp'] = pd.to_datetime(wl_MariposaBrook_4['Timestamp'], format='mixed')
# wl_MariposaBrook_4.rename(columns={'Value': 'wl_value'}, inplace=True)
# wl_MariposaBrook_4.drop(columns=['ts_name', 'ts_id', 'Units', 'station_name', 'station_id'], inplace=True)
# print(wl_MariposaBrook_4.info())
# # # Combine all WL data
# wl_MariposaBrook = pd.concat([wl_MariposaBrook_1, wl_MariposaBrook_2, wl_MariposaBrook_3, wl_MariposaBrook_4])
# print("Mariposa",wl_MariposaBrook.head(),wl_MariposaBrook.info())

# # Load and process Precipitation (PP) data
# pp_MariposaBrook_1 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/MariposaBrook-WSC/MariposaBrook-PP_1986-1995.csv')
# pp_MariposaBrook_1['Timestamp'] = pd.to_datetime(pp_MariposaBrook_1['Timestamp'], errors='coerce', infer_datetime_format=True)
# pp_MariposaBrook_1.rename(columns={'Value': 'pp_value'}, inplace=True)
# pp_MariposaBrook_1.drop(columns=['ts_name', 'ts_id', 'Units', 'station_name', 'station_id'], inplace=True)
# print(pp_MariposaBrook_1.info())
#
# pp_MariposaBrook_2 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/MariposaBrook-WSC/MariposaBrook-PP_1996-2005.csv')
# pp_MariposaBrook_2['Timestamp'] = pd.to_datetime(pp_MariposaBrook_2['Timestamp'], errors='coerce', infer_datetime_format=True)
# pp_MariposaBrook_2.rename(columns={'Value': 'pp_value'}, inplace=True)
# pp_MariposaBrook_2.drop(columns=['ts_name', 'ts_id', 'Units', 'station_name', 'station_id'], inplace=True)
# print(pp_MariposaBrook_2.info())
#
# pp_MariposaBrook_3 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/MariposaBrook-WSC/MariposaBrook-PP_2006-2015.csv')
# pp_MariposaBrook_3['Timestamp'] = pd.to_datetime(pp_MariposaBrook_3['Timestamp'], errors='coerce', infer_datetime_format=True)
# pp_MariposaBrook_3.rename(columns={'Value': 'pp_value'}, inplace=True)
# pp_MariposaBrook_3.drop(columns=['ts_name', 'ts_id', 'Units', 'station_name', 'station_id'], inplace=True)
# print(pp_MariposaBrook_3.info())
#
# pp_MariposaBrook_4 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/MariposaBrook-WSC/MariposaBrook-PP_2016-2024.csv')
# pp_MariposaBrook_4['Timestamp'] = pd.to_datetime(pp_MariposaBrook_4['Timestamp'], errors='coerce', infer_datetime_format=True)
# pp_MariposaBrook_4.rename(columns={'Value': 'pp_value'}, inplace=True)
# pp_MariposaBrook_4.drop(columns=['ts_name', 'ts_id', 'Units', 'station_name', 'station_id'], inplace=True)
# print(pp_MariposaBrook_4.info())
#
# # Combine all PP data
# pp_MariposaBrook = pd.concat([pp_MariposaBrook_1, pp_MariposaBrook_2, pp_MariposaBrook_3, pp_MariposaBrook_4])
# pp_MariposaBrook =pp_MariposaBrook.drop(columns=['Unnamed: 0'])
# print(pp_MariposaBrook.head())

# # Merge WL and PP data on Timestamp
# wl_pp_MariposaBrook = wl_MariposaBrook.merge(pp_MariposaBrook, how='inner', on='Timestamp')
#
# wl_pp_MariposaBrook = wl_pp_MariposaBrook.drop(columns=['Unnamed: 0'])
# print(wl_pp_MariposaBrook.head())
# wl_pp_MariposaBrook.to_csv('wl_pp_MariposaBrook.csv')

# wl_pp_Mariposa = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Pre-procesing/wl_pp_MariposaBrook.csv')
# wl_pp_Mariposa = wl_pp_Mariposa.drop(columns=['Unnamed: 0'])
# print(wl_pp_Mariposa.head())
# data = [wl_pp_Mariposa.columns.tolist()] + wl_pp_Mariposa.values.tolist()
#
# from openpyxl import load_workbook
# from pyexcelerate import Workbook
#
# # Using pyexcelerate instead of openpyxl because it provides faster writing.
#
# wb = load_workbook("/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Pre-procesing/wl_pp.xlsx")
# ws = wb.create_sheet("MariposaBrook")
#
# for row_idx, row in enumerate(data, start=1):
#     for col_idx, value in enumerate(row, start=1):
#         ws.cell(row=row_idx, column=col_idx, value=value)
#
# wb.save('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Pre-procesing/wl_pp.xlsx')
# print("New sheet added successfully!")

# Data Pre-processing
#
# Blackstock = pd.read_excel('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Pre-procesing/wl_pp.xlsx',sheet_name='Blackstock')
# print(Blackstock.head())
#
# # print(Blackstock.isna().sum())
# # Just 1 missing value in wl_value
#
# # import missingno as msno
# # msno.matrix(Blackstock)
#
# Blackstock.dropna(inplace=True)
# print(Blackstock.isna().sum())
#
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# Blackstock = Blackstock.set_index('Timestamp')
# # print(Blackstock.index)
#
# # print(Blackstock[Blackstock['wl_value']<=0])
#
# # print((len(Blackstock[(Blackstock['wl_value']<=0)])/len(Blackstock))*100)
# # The rows with wl_value less than or equal to zero is less than 0.5% so we can drop them
#
# Blackstock = Blackstock[~(Blackstock['wl_value']<=0)]
#
# # print((len(Blackstock[(Blackstock['pp_value']<=0)])/len(Blackstock))*100)
# # We can't drop the rows with pp_value less than zero because it is 95% of the data so
# # we need to impute the data.
#
#
# # Wl value Analysis
# # sns.set_theme(style='darkgrid',palette='flare')
# # fig ,ax = plt.subplots(2,2)
# # sns.scatterplot(data=Blackstock,x='Timestamp',y='wl_value',ax=ax[1,0])
# # ax[1,0].set_title('Scatter plot')
# # ax[1,0].tick_params("x",rotation=90)
# # sns.histplot(data=Blackstock,x='wl_value',ax=ax[0,0],kde=True)
# # ax[0,0].set_title('Histogram')
# # sns.boxenplot(x=Blackstock['wl_value'],ax=ax[0,1])
# # ax[0,1].set_title('Box Plot')
# # sns.lineplot(data=Blackstock['wl_value'],ax=ax[1,1])
# # ax[1,1].set_title('Line plot')
# # ax[1,1].tick_params("x",rotation=90)
# # fig.suptitle('Water level value Analysis for Blackstock',fontweight='bold',fontsize=16)
# # plt.show()
#
#
# # PP value Analysis
# # sns.set_theme(style='darkgrid',palette='flare')
# # fig ,ax = plt.subplots(2,2)
# # sns.scatterplot(data=Blackstock,x='Timestamp',y='pp_value',ax=ax[1,0])
# # ax[1,0].set_title('Scatter plot')
# # ax[1,0].tick_params("x",rotation=90)
# # sns.histplot(data=Blackstock,x='pp_value',ax=ax[0,0],kde=True)
# # ax[0,0].set_title('Histogram')
# # sns.boxenplot(x=Blackstock['pp_value'],ax=ax[0,1])
# # ax[0,1].set_title('Boxen Plot')
# # sns.lineplot(data=Blackstock['pp_value'],ax=ax[1,1])
# # ax[1,1].set_title('Line plot')
# # ax[1,1].tick_params("x",rotation=90)
# # fig.suptitle('Precipitation level value Analysis for Blackstock',fontweight='bold',fontsize=16)
# # plt.show()
#
# # Scatter plot between wl_value and pp_value
# # sns.set_theme(style='darkgrid',palette='flare')
# # sns.scatterplot(data=Blackstock,x='wl_value',y='pp_value')
# # plt.title('Wl vs Precipitation value')
# # plt.show()
#
# # Correlation
# from scipy.stats import pearsonr
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
# from scipy.stats import iqr
#
# # Outlier removal
# print(iqr(Blackstock['wl_value']))
# Blackstock = Blackstock[(np.abs(zscore(Blackstock.select_dtypes(include=np.number))) < 3).all(axis=1)]
#
# # Checking max and min of every column for outlier after outlier removal
# # print('PP_value after outlier removal')
# # print(Blackstock['pp_value'].min())
# # print(Blackstock['pp_value'].max())
# # print('WL_value after outlier removal')
# # print(Blackstock['wl_value'].min())
# # print(Blackstock['wl_value'].max())
#
# # Need to scale the data as the min and max only have difference of (1.2 in wl and 2.2
# # in pp)
#
# # Scaling the data
# from sklearn.preprocessing import StandardScaler
#
# Scaler = StandardScaler()
# Blackstock_scaled = Scaler.fit_transform(Blackstock)
#
# print(type(Blackstock_scaled))
# Blackstock_scaled = pd.DataFrame(Blackstock_scaled)
# Blackstock_scaled['Timestamp']  = Blackstock.index
# # print(Blackstock_scaled.head())
#
# Blackstock_scaled.rename(columns={0:'wl_value',1:'pp_value'},inplace=True)
# # print(Blackstock_scaled.head())
# Blackstock_scaled.set_index('Timestamp',inplace=True)
#
# # Min-Max sampling
# from sklearn.preprocessing import MinMaxScaler
#
# min_max = MinMaxScaler(feature_range=(-1,1))
# Blackstock_minmax = min_max.fit_transform(Blackstock_scaled)
# print(type(Blackstock_minmax))
# Blackstock_minmax = pd.DataFrame(Blackstock_minmax)
# Blackstock_minmax['Timestamp']  = Blackstock.index
# # print(Blackstock_scaled.head())
#
# Blackstock_minmax.rename(columns={0:'wl_value',1:'pp_value'},inplace=True)
# # print(Blackstock_scaled.head())
# Blackstock_minmax.set_index('Timestamp',inplace=True)
#
# # # Wl value Analysis after data preprocessing
# # sns.set_theme(style='darkgrid',palette='flare')
# # fig ,ax = plt.subplots(2,2)
# # sns.scatterplot(data=Blackstock_minmax.loc['2017-01-01 00:00:00':'2018-01-01 00:00:00'],x='Timestamp',y='wl_value',ax=ax[1,0])
# # ax[1,0].set_title('Scatter plot')
# # ax[1,0].tick_params("x",rotation=90)
# # sns.histplot(data=Blackstock_minmax,x='wl_value',ax=ax[0,0],kde=True)
# # ax[0,0].set_title('Histogram')
# # sns.boxenplot(x=Blackstock_minmax['wl_value'],ax=ax[0,1])
# # ax[0,1].set_title('Boxen Plot')
# # sns.lineplot(data=Blackstock_minmax['wl_value'].loc['2017-01-01 00:00:00':'2018-01-01 00:00:00'],ax=ax[1,1])
# # ax[1,1].set_title('Line plot')
# # ax[1,1].tick_params("x",rotation=90)
# # fig.suptitle('Water level value Analysis for Blackstock after Data Preprocessing',fontweight='bold',fontsize=16)
# # plt.show()
#
#
# # PP value Analysis after data preprocessing
# # sns.set_theme(style='darkgrid',palette='flare')
# # fig ,ax = plt.subplots(2,2)
# # sns.scatterplot(data=Blackstock_minmax.loc['2017-01-01 00:00:00':'2018-01-31 00:00:00'],x='Timestamp',y='pp_value',ax=ax[1,0])
# # ax[1,0].set_title('Scatter plot')
# # ax[1,0].tick_params("x",rotation=90)
# # sns.histplot(data=Blackstock_minmax,x='pp_value',ax=ax[0,0],kde=True)
# # ax[0,0].set_title('Histogram')
# # sns.boxenplot(x=Blackstock_minmax['pp_value'],ax=ax[0,1])
# # ax[0,1].set_title('Boxen Plot')
# # sns.lineplot(data=Blackstock_minmax['pp_value'].loc['2017-01-01 00:00:00':'2018-01-31 00:00:00'],ax=ax[1,1])
# # ax[1,1].set_title('Line plot')
# # ax[1,1].tick_params("x",rotation=90)
# # fig.suptitle('Precipitation level value Analysis for Blackstock after Data Preprocessing',fontweight='bold',fontsize=16)
# # plt.show()
#
#
# R,p = pearsonr(Blackstock_minmax['wl_value'],Blackstock_minmax['pp_value'])
# print(Blackstock_minmax.corr())
# print("Pearson Correlation value in percentage",R*100)
#
# # Heatmap of the data
# # sns.heatmap(Blackstock_scaled.corr(),annot=True,linewidth=.5,fmt=".1f")
# # plt.title('Correlation matrix after data preprocessing')
# # plt.show()
#
# # Scatter plot between wl_value and pp_value
# # sns.set_theme(style='darkgrid',palette='flare')
# # sns.scatterplot(data=Blackstock_minmax,x='wl_value',y='pp_value')
# # plt.title('Wl vs Precipitation value')
# # plt.show()
#
# # There is no linear dependency in data which is clearly visual from the graph and also
# # from the correlation matrix and pearson value, so we need to find non-linear dependancy.
# from sklearn.feature_selection import mutual_info_regression
# mi = mutual_info_regression(Blackstock_minmax[['wl_value']], Blackstock_minmax['pp_value'])
# print(f'Mutual Information: {mi[0]}')

# MariposaBrook
# MariposaBrook = pd.read_excel('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Pre-procesing/wl_pp.xlsx',sheet_name='MariposaBrook')
#
# # print(MariposaBrook.head())
# # print(MariposaBrook.info())
# print(MariposaBrook.isna().sum())
# # Just 15 missing value in wl_value
#
# MariposaBrook['Timestamp'] = pd.to_datetime(MariposaBrook['Timestamp'])
#
# import matplotlib.pyplot as plt
# # import missingno as msno
# # msno.matrix(MariposaBrook)
# # plt.title('Missing value matrix')
# # plt.show()
#
# MariposaBrook.dropna(inplace=True)
# print(MariposaBrook.isna().sum())
#
# import seaborn as sns
#
# MariposaBrook = MariposaBrook.set_index('Timestamp')
# # print(MariposaBrook.index)
#
# # print(MariposaBrook[MariposaBrook['wl_value']<=0])
#
# print((len(MariposaBrook[(MariposaBrook['wl_value']<=0)])/len(MariposaBrook))*100)
# # The rows with wl_value less than or equal to zero is less than 0.13% so we can drop them
#
# MariposaBrook = MariposaBrook[~(MariposaBrook['wl_value']<=0)]
# # print(MariposaBrook[MariposaBrook['wl_value']<=0])
#
# print((len(MariposaBrook[(MariposaBrook['pp_value']<=0)])/len(MariposaBrook))*100)
# # The rows with pp_value less than zero is less than 0.00021% so we can drop them
#
# MariposaBrook = MariposaBrook[~(MariposaBrook['pp_value']<=0)]
# # print(MariposaBrook[MariposaBrook['pp_value']<=0])
#
# print("The length of the new dataset is now reduced from 465k to",len(MariposaBrook))
#
# print("Percentage of the Precipitation value equal to 0.2 in dataset",(len(MariposaBrook[(MariposaBrook['pp_value']==0.2)])/len(MariposaBrook))*100)
# # MariposaBrook.to_excel('Temp.xlsx',sheet_name='Mariposa_new')
#
# # Wl value Analysis
# # sns.set_theme(style='darkgrid',palette='flare')
# # fig ,ax = plt.subplots(2,2)
# # sns.scatterplot(data=MariposaBrook.loc['1992-07-17 20:00:00':'1997-07-17 12:00:00'],x='Timestamp',y='wl_value',ax=ax[1,0])
# # ax[1,0].set_title('Scatter plot')
# # ax[1,0].tick_params("x",rotation=90)
# # sns.histplot(data=MariposaBrook,x='wl_value',ax=ax[0,0],kde=True)
# # ax[0,0].set_title('Histogram')
# # sns.boxenplot(x=MariposaBrook['wl_value'],ax=ax[0,1])
# # ax[0,1].set_title('Boxen Plot')
# # sns.lineplot(data=MariposaBrook['wl_value'].loc['1992-07-17 20:00:00':'1997-07-17 12:00:00'],ax=ax[1,1])
# # ax[1,1].set_title('Line plot')
# # ax[1,1].tick_params("x",rotation=90)
# # fig.suptitle('Water level value Analysis for MariposaBrook',fontweight='bold',fontsize=16)
# # plt.show()
#
# # PP value Analysis
# # sns.set_theme(style='darkgrid',palette='flare')
# # fig ,ax = plt.subplots(2,2,figsize=(10,12))
# # sns.scatterplot(data=MariposaBrook.loc['1992-07-17 20:00:00':'1997-07-17 12:00:00'],x='Timestamp',y='pp_value',ax=ax[1,0])
# # ax[1,0].set_title('Scatter plot')
# # ax[1,0].tick_params("x",rotation=90)
# # sns.histplot(data=MariposaBrook,x='pp_value',ax=ax[0,0],kde=True)
# # ax[0,0].set_title('Histogram')
# # sns.boxenplot(x=MariposaBrook['pp_value'],ax=ax[0,1])
# # ax[0,1].set_title('Boxen Plot')
# # sns.lineplot(data=MariposaBrook['pp_value'].loc['1992-07-17 20:00:00':'1997-07-17 12:00:00'],ax=ax[1,1])
# # ax[1,1].set_title('Line plot')
# # ax[1,1].tick_params("x",rotation=90)
# # fig.suptitle('Precipitation level value Analysis for MariposaBrook',fontweight='bold',fontsize=16)
# # plt.show()
#
# # Scatter plot between wl_value and pp_value
# # sns.set_theme(style='darkgrid',palette='flare')
# # sns.scatterplot(data=MariposaBrook,x='wl_value',y='pp_value')
# # plt.title('Wl vs Precipitation value')
# # plt.show()
#
# # Correlation
# from scipy.stats import pearsonr
# from scipy.stats import spearmanr
#
# R,p = pearsonr(MariposaBrook['wl_value'],MariposaBrook['pp_value'])
# print("Pearson Correlation value in percentage",R*100)
#
# R,p = spearmanr(MariposaBrook['wl_value'],MariposaBrook['pp_value'])
# print("Spearman Correlation value in percentage",R*100)
#
# # Heatmap of the data
# # sns.heatmap(MariposaBrook.corr(),annot=True,linewidth=.5,fmt=".1f")
# # plt.title('Correlation matrix')
# # plt.show()
#
# # Checking max and min of every column for outlier before outlier removal
# print('PP_value before outlier removal')
# print(MariposaBrook['pp_value'].min())
# print(MariposaBrook['pp_value'].max())
# print('WL_value before outlier removal')
# print(MariposaBrook['wl_value'].min())
# print(MariposaBrook['wl_value'].max())
#
# # From all this visualization one thing is clear that data need  to go under
# # scaler transformation so we can work on it.
# from scipy.stats import zscore
# from scipy.stats import iqr
#
# # Outlier removal
# print(iqr(MariposaBrook['wl_value']))
# MariposaBrook = MariposaBrook[(np.abs(zscore(MariposaBrook.select_dtypes(include=np.number))) < 3).all(axis=1)]
#
# # Checking max and min of every column for outlier after outlier removal
# print('PP_value after outlier removal')
# print(MariposaBrook['pp_value'].min())
# print(MariposaBrook['pp_value'].max())
# print('WL_value after outlier removal')
# print(MariposaBrook['wl_value'].min())
# print(MariposaBrook['wl_value'].max())
#
# # # Need to scale the data as the min and max only have difference of (1.2 in wl and 2.2
# # # in pp)
#
#
# # # Min-Max sampling
# # from sklearn.preprocessing import MinMaxScaler
# #
# # min_max = MinMaxScaler(feature_range=(-1,1))
# # MariposaBrook_minmax = min_max.fit_transform(MariposaBrook)
# # print(type(MariposaBrook_minmax))
# # MariposaBrook_minmax = pd.DataFrame(MariposaBrook_minmax)
# # MariposaBrook_minmax['Timestamp']  = MariposaBrook.index
# # print(MariposaBrook_minmax.head())
# #
# # MariposaBrook_minmax.rename(columns={0:'wl_value',1:'pp_value'},inplace=True)
# # print(MariposaBrook_minmax.head())
# #
# # print(MariposaBrook_minmax.info())
# # MariposaBrook_minmax.set_index('Timestamp',inplace=True)
#
# # We don't need min_max scaling as our data is going to go under normalization method
#
# MariposaBrook_minmax = MariposaBrook
#
# # The precipitation data after min-max scaling still follows the unusual distribution,
# # need to try some normalization method to scale the pp_value and remove minmax
# # Now, we have already used min-max scaling from (-1,1), so we can't use log, square root
# # and Box-cox transformation the options left are ye0-johnson, zscore and Quantile Transformation
# # We are gonna use yeo-johnson on wl_value because our data is approx normal
# # And Quantile transform for the pp_value because it is extreme case.
# ## As, I have remove min max I can try to use log,sqrt and box-cox
# from sklearn.preprocessing import PowerTransformer
#
# pt = PowerTransformer()
#
# MariposaBrook_minmax['wl_value'] = pt.fit_transform(MariposaBrook_minmax['wl_value'].values.reshape(-1,1))
#
# # Wl value Analysis after data preprocessing
# # sns.set_theme(style='darkgrid',palette='flare')
# # fig ,ax = plt.subplots(2,2)
# # sns.scatterplot(data=MariposaBrook_minmax.loc['1988-07-17 20:00:00':'1992-07-17 12:00:00'],x='Timestamp',y='wl_value',ax=ax[1,0])
# # ax[1,0].set_title('Scatter plot')
# # ax[1,0].tick_params("x",rotation=90)
# # sns.histplot(data=MariposaBrook_minmax,x='wl_value',ax=ax[0,0],kde=True)
# # ax[0,0].set_title('Histogram')
# # sns.boxenplot(x=MariposaBrook_minmax['wl_value'],ax=ax[0,1])
# # ax[0,1].set_title('Boxen Plot')
# # sns.lineplot(data=MariposaBrook_minmax['wl_value'].loc['1988-07-17 20:00:00':'1992-07-17 12:00:00'],ax=ax[1,1])
# # ax[1,1].set_title('Line plot')
# # ax[1,1].tick_params("x",rotation=90)
# # fig.suptitle('Water level value Analysis for MariposaBrook after Data Preprocessing',fontweight='bold',fontsize=16)
# # plt.show()
#
# # Precipitation Transformation
# from sklearn.preprocessing import QuantileTransformer
#
# print(pd.unique(MariposaBrook_minmax.index.year))
# unique_years = len(pd.unique(MariposaBrook_minmax.index.year))
# qt = QuantileTransformer(n_quantiles=unique_years,random_state=42,output_distribution='normal')
#
# MariposaBrook_minmax['pp_value'] = qt.fit_transform(MariposaBrook['pp_value'].values.reshape(-1,1))
#
#
# # # PP value Analysis after data preprocessing
# # sns.set_theme(style='darkgrid',palette='flare')
# # fig ,ax = plt.subplots(2,2)
# # sns.scatterplot(data=MariposaBrook_minmax.loc['1988-07-17 20:00:00':'1992-07-17 12:00:00'],x='Timestamp',y='pp_value',ax=ax[1,0])
# # ax[1,0].set_title('Scatter plot')
# # ax[1,0].tick_params("x",rotation=90)
# # sns.histplot(data=MariposaBrook_minmax,x='pp_value',ax=ax[0,0],kde=True)
# # ax[0,0].set_title('Histogram')
# # sns.boxenplot(x=MariposaBrook_minmax['pp_value'],ax=ax[0,1])
# # ax[0,1].set_title('Boxen Plot')
# # sns.lineplot(data=MariposaBrook_minmax['pp_value'].loc['1988-07-17 20:00:00':'1992-07-17 12:00:00'],ax=ax[1,1])
# # ax[1,1].set_title('Line plot')
# # ax[1,1].tick_params("x",rotation=90)
# # fig.suptitle('Precipitation level value Analysis for MariposaBrook after Data Preprocessing',fontweight='bold',fontsize=16)
# # plt.show()
#
#
# R,p = pearsonr(MariposaBrook_minmax['wl_value'],MariposaBrook_minmax['pp_value'])
# print(MariposaBrook_minmax.corr())
# print("Pearson Correlation value in percentage",R*100)
# #
# R,p = spearmanr(MariposaBrook_minmax['wl_value'],MariposaBrook_minmax['pp_value'])
# print("Spearman Correlation value in percentage",R*100)
#
# # Heatmap of the data
# # sns.heatmap(MariposaBrook_minmax.corr(),annot=True,linewidth=.5,fmt=".1f")
# # plt.title('Correlation matrix after data preprocessing')
# # plt.show()
#
# # Scatter plot between wl_value and pp_value
# # sns.set_theme(style='darkgrid',palette='flare')
# # sns.scatterplot(data=MariposaBrook_minmax,x='wl_value',y='pp_value')
# # plt.title('Wl vs Precipitation value')
# # plt.show()
# #
# # # There is no linear dependency in data which is clearly visual from the graph and also
# # # from the correlation matrix and pearson value, so we need to find non-linear dependancy.
# from sklearn.feature_selection import mutual_info_regression
# mi = mutual_info_regression(MariposaBrook_minmax[['pp_value']], MariposaBrook_minmax['wl_value'],random_state=42)
# print(f'Mutual Information: {mi[0]}')


# PigeonRiver Lotus

PigeonRiverLotus = pd.read_excel('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Pre-procesing/wl_pp.xlsx',sheet_name='Pigeon_lotus1')
print(PigeonRiverLotus.head())


print(PigeonRiverLotus.isna().sum())
# No missing value in the dataset

import matplotlib.pyplot as plt
import seaborn as sns

PigeonRiverLotus = PigeonRiverLotus.set_index('Timestamp')
# print(PigeonRiverLotus.index)

# print(PigeonRiverLotus[PigeonRiverLotus['wl_value']<=0])

print((len(PigeonRiverLotus[(PigeonRiverLotus['wl_value']<=0)])/len(PigeonRiverLotus))*100)
# The rows with wl_value less than or equal to zero are only 2 so we can drop theem

PigeonRiverLotus = PigeonRiverLotus[~(PigeonRiverLotus['wl_value']<=0)]

print((len(PigeonRiverLotus[(PigeonRiverLotus['pp_value']<0)])/len(PigeonRiverLotus))*100)
# We can drop the rows with pp_value less than zero because there are only 2 rows.

# print(PigeonRiverLotus[PigeonRiverLotus['pp_value']<0])

PigeonRiverLotus = PigeonRiverLotus[~(PigeonRiverLotus['pp_value']<=0)]

# Wl value Analysis
# sns.set_theme(style='darkgrid',palette='flare')
# fig ,ax = plt.subplots(2,2,figsize=(10,12))
# sns.scatterplot(data=PigeonRiverLotus,x='Timestamp',y='wl_value',ax=ax[1,0])
# ax[1,0].set_title('Scatter plot')
# ax[1,0].tick_params("x",rotation=90)
# sns.histplot(data=PigeonRiverLotus,x='wl_value',ax=ax[0,0],kde=True)
# ax[0,0].set_title('Histogram')
# sns.boxenplot(x=PigeonRiverLotus['wl_value'],ax=ax[0,1])
# ax[0,1].set_title('Box Plot')
# sns.lineplot(data=PigeonRiverLotus['wl_value'],ax=ax[1,1])
# ax[1,1].set_title('Line plot')
# ax[1,1].tick_params("x",rotation=90)
# fig.suptitle('Water level value Analysis for Pigeon River Lotus',fontweight='bold',fontsize=16)
# plt.show()

# PP value Analysis
# sns.set_theme(style='darkgrid',palette='flare')
# fig ,ax = plt.subplots(2,2,figsize=(10,12))
# sns.scatterplot(data=PigeonRiverLotus,x='Timestamp',y='pp_value',ax=ax[1,0])
# ax[1,0].set_title('Scatter plot')
# ax[1,0].tick_params("x",rotation=90)
# sns.histplot(data=PigeonRiverLotus,x='pp_value',ax=ax[0,0],kde=True)
# ax[0,0].set_title('Histogram')
# sns.boxenplot(x=PigeonRiverLotus['pp_value'],ax=ax[0,1])
# ax[0,1].set_title('Boxen Plot')
# sns.lineplot(data=PigeonRiverLotus['pp_value'],ax=ax[1,1])
# ax[1,1].set_title('Line plot')
# ax[1,1].tick_params("x",rotation=90)
# fig.suptitle('Precipitation level value Analysis for PigeonRiverLotus',fontweight='bold',fontsize=16)
# plt.show()

# Scatter plot between wl_value and pp_value
# sns.set_theme(style='darkgrid',palette='flare')
# sns.scatterplot(data=PigeonRiverLotus,x='wl_value',y='pp_value')
# plt.title('Wl vs Precipitation value')
# plt.show()

# Correlation
from scipy.stats import pearsonr

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
PigeonRiverLotus = PigeonRiverLotus[(np.abs(zscore(PigeonRiverLotus.select_dtypes(include=np.number))) < 3).all(axis=1)]

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

# Scaling the data
from sklearn.preprocessing import StandardScaler

Scaler = StandardScaler()
PigeonRiverLotus_scaled = Scaler.fit_transform(PigeonRiverLotus)

print(type(PigeonRiverLotus_scaled))
PigeonRiverLotus_scaled = pd.DataFrame(PigeonRiverLotus_scaled)
PigeonRiverLotus_scaled['Timestamp']  = PigeonRiverLotus.index
print(PigeonRiverLotus_scaled.head())

PigeonRiverLotus_scaled.rename(columns={0:'wl_value',1:'pp_value'},inplace=True)
print(PigeonRiverLotus_scaled.head())
PigeonRiverLotus_scaled.set_index('Timestamp',inplace=True)

# Min-Max sampling
PigeonRiverLotus_minmax = PigeonRiverLotus
# from sklearn.preprocessing import MinMaxScaler
#
# min_max = MinMaxScaler(feature_range=(-1,1))
# PigeonRiverLotus_minmax = min_max.fit_transform(PigeonRiverLotus_scaled)
# print(type(PigeonRiverLotus_minmax))
# PigeonRiverLotus_minmax = pd.DataFrame(PigeonRiverLotus_minmax)
# PigeonRiverLotus_minmax['Timestamp']  = PigeonRiverLotus.index
# print(PigeonRiverLotus_minmax.head())
#
# PigeonRiverLotus_minmax.rename(columns={0:'wl_value',1:'pp_value'},inplace=True)
# print(PigeonRiverLotus_minmax.head())
# PigeonRiverLotus_minmax.set_index('Timestamp',inplace=True)

# Wl value Analysis after data preprocessing
# sns.set_theme(style='darkgrid',palette='flare')
# fig ,ax = plt.subplots(2,2,figsize=(10,12))
# sns.scatterplot(data=PigeonRiverLotus_minmax.loc['2005-09-06 10:00:00':'2007-09-03 10:00:00'],x='Timestamp',y='wl_value',ax=ax[1,0])
# ax[1,0].set_title('Scatter plot')
# ax[1,0].tick_params("x",rotation=90)
# sns.histplot(data=PigeonRiverLotus_minmax,x='wl_value',ax=ax[0,0],kde=True)
# ax[0,0].set_title('Histogram')
# sns.boxenplot(x=PigeonRiverLotus_minmax['wl_value'],ax=ax[0,1])
# ax[0,1].set_title('Boxen Plot')
# sns.lineplot(data=PigeonRiverLotus_minmax['wl_value'].loc['2005-09-06 10:00:00':'2007-09-03 10:00:00'],ax=ax[1,1])
# ax[1,1].set_title('Line plot')
# ax[1,1].tick_params("x",rotation=90)
# fig.suptitle('Water level value Analysis for Pigeon River Lotus after Data Preprocessing',fontweight='bold',fontsize=16)
# plt.show()

# PP value Analysis after data preprocessing
# sns.set_theme(style='darkgrid',palette='flare')
# fig ,ax = plt.subplots(2,2)
# sns.scatterplot(data=PigeonRiverLotus_minmax.loc['2005-09-06 10:00:00':'2007-10-31 00:00:00'],x='Timestamp',y='pp_value',ax=ax[1,0])
# ax[1,0].set_title('Scatter plot')
# ax[1,0].tick_params("x",rotation=90)
# sns.histplot(data=PigeonRiverLotus_minmax,x='pp_value',ax=ax[0,0],kde=True)
# ax[0,0].set_title('Histogram')
# sns.boxenplot(x=PigeonRiverLotus_minmax['pp_value'],ax=ax[0,1])
# ax[0,1].set_title('Boxen Plot')
# sns.lineplot(data=PigeonRiverLotus_minmax['pp_value'].loc['2005-09-06 10:00:00':'2007-10-31 00:00:00'],ax=ax[1,1])
# ax[1,1].set_title('Line plot')
# ax[1,1].tick_params("x",rotation=90)
# fig.suptitle('Precipitation level value Analysis for Pigeon River Lotus after Data Preprocessing',fontweight='bold',fontsize=16)
# plt.show()

cross_correlation(PigeonRiverLotus_minmax,2800,2900)

R,p = pearsonr(PigeonRiverLotus_minmax['wl_value'],PigeonRiverLotus_minmax['pp_value'].shift(periods=2890,fill_value=0))
print(PigeonRiverLotus_minmax.corr())
print("Pearson Correlation value in percentage",R*100)

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
mi = mutual_info_regression(PigeonRiverLotus_minmax[['wl_value']], PigeonRiverLotus_minmax['pp_value'].shift(periods=2890,fill_value=0))
print(f'Mutual Information: {mi[0]}')



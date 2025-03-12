import pandas as pd
import numpy as np

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


wl_PigeonRiverL = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/PigeonRiver-Lotus/PigeonRiverL-WL_2005-2016.csv')

# convert the timestamp column into date-time
wl_PigeonRiverL['Timestamp'] = pd.DatetimeIndex(wl_PigeonRiverL['Timestamp'])
print(wl_PigeonRiverL.info())

wl_PigeonRiverL.rename(columns={'Value':'wl_value'},inplace=True)
wl_PigeonRiverL.drop(columns=['ts_name','ts_id','Units','station_name','station_id'],inplace=True)

wl_PigeonRiverL = wl_PigeonRiverL[wl_PigeonRiverL['Timestamp']>='9/6/2005 10:00']
print(wl_PigeonRiverL.head(10))

wl_PigeonRiverL_2 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/PigeonRiver-Lotus/PigeonRiverL-WL_2017-2014.csv')

wl_PigeonRiverL_2['Timestamp'] = pd.DatetimeIndex(wl_PigeonRiverL_2['Timestamp'])
print(wl_PigeonRiverL_2.info())

wl_PigeonRiverL_2.rename(columns={'Value':'wl_value'},inplace=True)
wl_PigeonRiverL_2.drop(columns=['ts_name','ts_id','Units','station_name','station_id'],inplace=True)

wl_f_PigeonRiverL = pd.concat([wl_PigeonRiverL,wl_PigeonRiverL_2])


# Load and process the first dataset
pp_PigeonRiverL = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/PigeonRiver-Lotus/PigeonRiverL-PP_2005-2016.csv')
pp_PigeonRiverL['Timestamp'] = pd.DatetimeIndex(pp_PigeonRiverL['Timestamp'])
print(pp_PigeonRiverL.info())

pp_PigeonRiverL.rename(columns={'Value': 'pp_value'}, inplace=True)
pp_PigeonRiverL.drop(columns=['ts_name', 'ts_id', 'Units', 'station_name', 'station_id'], inplace=True)

# Load and process the second dataset
pp_PigeonRiverL_2 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/PigeonRiver-Lotus/PigeonRiverL-PP_2017-2024.csv')
pp_PigeonRiverL_2['Timestamp'] = pd.DatetimeIndex(pp_PigeonRiverL_2['Timestamp'])
print(pp_PigeonRiverL_2.info())

pp_PigeonRiverL_2.rename(columns={'Value': 'pp_value'}, inplace=True)
pp_PigeonRiverL_2.drop(columns=['ts_name', 'ts_id', 'Units', 'station_name', 'station_id'], inplace=True)

# Combine the two datasets
pp_f_PigeonRiverL = pd.concat([pp_PigeonRiverL, pp_PigeonRiverL_2])

wl_pp_pigeon = wl_f_PigeonRiverL.merge(pp_f_PigeonRiverL,how='inner',on='Timestamp')
wl_pp_pigeon.drop(columns=['Unnamed: 0_x','Unnamed: 0_y'],inplace=True)
print(wl_pp_pigeon.head())
file_path = '/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Pre-procesing/wl_pp.xlsx'

# Use ExcelWriter with mode='a' (append) and engine='openpyxl'
with pd.ExcelWriter(file_path, mode='a', engine='openpyxl', if_sheet_exists='new') as writer:
    wl_pp_pigeon.to_excel(writer, sheet_name="Pigeon_lotus", index=False)

print("Data written to new sheet successfully!")
import pandas as pd
import numpy as np

wl_blackstock = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Blackstock-WSC/Blackstock-WL_2006-2016.csv')

# convert the timestamp column into date-time
wl_blackstock['Timestamp'] = pd.DatetimeIndex(wl_blackstock['Timestamp'])
print(wl_blackstock.info())

wl_blackstock.rename(columns={'Value':'wl_value'},inplace=True)
wl_blackstock.drop(columns=['ts_name','ts_id','Units','station_name','station_id'],inplace=True)

wl_blackstock = wl_blackstock[wl_blackstock['Timestamp']>='2016-11-04 05:00:00']
print(wl_blackstock.head(10))

wl_blackstock_2 = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Blackstock-WSC/Blackstock-WL_2017-2014.csv')

wl_blackstock_2['Timestamp'] = pd.DatetimeIndex(wl_blackstock_2['Timestamp'])
print(wl_blackstock_2.info())

wl_blackstock_2.rename(columns={'Value':'wl_value'},inplace=True)
wl_blackstock_2.drop(columns=['ts_name','ts_id','Units','station_name','station_id'],inplace=True)

wl_f_blackstock = pd.concat([wl_blackstock,wl_blackstock_2])
print(wl_f_blackstock.head())

pp_blackstock = pd.read_csv('/Volumes/Devansh/BDA/Research Paper /2025-ULinks-Precipitation-WaterLevel-Data/Blackstock-WSC/Blackstock-PP_2016-2024.csv')
pp_blackstock['Timestamp'] = pd.DatetimeIndex(pp_blackstock['Timestamp'])
print(pp_blackstock.info())

pp_blackstock.rename(columns={'Value':'pp_value'},inplace=True)
pp_blackstock.drop(columns=['ts_name','ts_id','Units','station_name','station_id'],inplace=True)
print(pp_blackstock.head(5))

wl_pp_blackstock = wl_f_blackstock.merge(pp_blackstock,how='inner',on='Timestamp')
wl_pp_blackstock.drop(columns=['Unnamed: 0_x','Unnamed: 0_y'],inplace=True)
print(wl_pp_blackstock.head())
wl_pp_blackstock.to_excel('wl_pp.xlsx',sheet_name='Blackstock',index=False)
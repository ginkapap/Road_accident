# -*- coding: utf-8 -*
import pandas as pd
import numpy as np

#pd.options.mode.chained_assignment = None
# plt.style.use('ggplot')
df = pd.read_csv('Kaagle_Upload.csv')
# print(df.info())


#df2 = pd.DataFrame((df.isnull().mean()), columns=['a'])
# df2 = df2.reset_index()#\
# for i in range(len(df2)):
# if df2.iloc[i,1] >= 0.05:
#       #print(df2.iloc[i,0])
# print(df.shape)
df = df.replace(-1, np.nan)
df1 = df.isnull().sum().reset_index(name='count')
# print(df1)
# print(df1[df1['count'] >= 285331]) #缺師資料高於5% driver_imd_decile、vehicle_imd_decile
#df2 = df.drop(['vehicle_imd_decile','driver_imd_decile','accident_index','vehicle_reference','location_easting_osgr','location_northing_osgr','longitude','latitude','local_authority_(highway)','1st_road_number','2nd_road_number','vehicle_reference','age_of_driver','driver_home_area_type','casualty_reference','age_of_casualty','casualty_imd_decile'],axis=1)
df2 = df.drop(['vehicle_imd_decile', 'driver_imd_decile', 'accident_index', 'vehicle_reference', 'location_easting_osgr', 'location_northing_osgr', 'local_authority_(highway)', '1st_road_number', '2nd_road_number', 'vehicle_reference', 'age_band_of_driver', 'driver_home_area_type', 'casualty_reference', 'age_band_of_casualty', 'date', 'lsoa_of_accident_location'], axis=1)
df2 = df2.dropna()
df2['time'] = df2['time'].str[11:]
# 造虛擬變數
df1 = df.isnull().sum().reset_index(name='nacount')
df1['nacount'] = df1['nacount'].apply(lambda x: x / 285331)
dfna = df1.sort_values(['nacount'], ascending=[False])
# print(dfna)
#df = df.drop(['vehicle_imd_decile','driver_imd_decile'],axis=1)


def a(x):
    if x == 1:
        return 1
    elif x == 2:
        return 1
    elif x == 3:
        return 0
    else:
        return x


df21 = df2.copy()
df21['accident_severity'] = df2['accident_severity'].apply(a)


#df2['accident_severity'] = df2['accident_severity'].apply(a)
# print(df2['propulsion_code'])
#df_dummy =df2.drop(['number_of_vehicles','number_of_casualties','date','day_of_week','time','speed_limit','age_band_of_driver','engine_capacity_(cc)','age_of_vehicle','age_band_of_casualty','casualty_severity'],axis=1)
# df['dd']=df['accident_severity']-df['casualty_home_area_type']


# print(m)
# print(n)
# print(df_corr.corr())

# annot 上面是否顯示數字、fmt數字曲道小數點幾位、mask辦三角型
#plt.title('Correlations - win vs factors (all games)')


#df3 = df.dropna()
# print(df3.shape)
# print(df['vehicle_imd_decile'])#全為-1

#print((df3 == -1).astype(int).sum(axis=0)/174538)
# print(df3)

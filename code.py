# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
data=pd.read_csv(path,sep=',')
data.rename({'Total':'Total_Medals'},axis='columns',inplace=True)
#Code starts here
data.head(10)


# --------------
#Code starts here
def conditions(x,y):
    if x > y:
        return "Summer"
    elif x < y:
        return "Winter"
    else:
        return "Both"

func = np.vectorize(conditions)
better_event_np = func(data['Total_Summer'],data['Total_Winter'])
data['Better_Event']=better_event_np
#data['Better_Event']=np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')
#(data['Total_Summer'] < data['Total_Winter'], 'Winter', 'Both'))
#data.head()
better_event=data['Better_Event'].value_counts().index[0]
print(better_event)


# --------------
#Code starts here
top_countries= data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

top_countries=top_countries[:(len(top_countries)-1)]
top_countries.tail()

def top_ten(x,col):
   country_list=x.nlargest(10,col)['Country_Name']
   return country_list


top_10_summer=list(top_ten(top_countries,'Total_Summer'))
top_10_winter=list(top_ten(top_countries,'Total_Winter'))
top_10=list(top_ten(top_countries,'Total_Medals'))
#print(type(top_10_summer))
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)


# --------------
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
#print(summer_df.head())
#summer_df[['Country_Name','Total_Summer']].plot(kind='bar')
# initialize the figure
plt.figure(figsize=[14,8])
# label the axes
plt.xlabel("Country Name")
plt.ylabel("Total Summer Medals")
plt.xticks(rotation=45)
# build and show the plot

plt.bar(summer_df['Country_Name'],summer_df['Total_Summer'],label='Summer')

plt.bar(winter_df['Country_Name'],winter_df['Total_Winter'],label='Winter')

#plt.bar(top_df['Country_Name'],top_df['Total_Medals'],label='Top')
plt.legend()



# --------------
#Code starts here
#summer_df.set_index('Country_Name',inplace=True)
summer_df['Golden_Ratio']=summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio=summer_df.loc[:,'Golden_Ratio'].max()
summer_country_gold=summer_df[summer_df['Golden_Ratio']==summer_max_ratio]['Country_Name'].values[0]
print(summer_country_gold)

winter_df['Golden_Ratio']=winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio=winter_df.loc[:,'Golden_Ratio'].max()
winter_country_gold=winter_df[winter_df['Golden_Ratio']==winter_max_ratio]['Country_Name'].values[0]
print(winter_country_gold)

top_df['Golden_Ratio']=top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio=top_df.loc[:,'Golden_Ratio'].max()
top_country_gold=top_df[top_df['Golden_Ratio']==top_max_ratio]['Country_Name'].values[0]
print(top_country_gold)



# --------------
#Code starts here
data_1=data[:-1]
data_1['Total_Points']=(3 * data_1['Gold_Total']+ 2* data_1['Silver_Total']+data_1['Bronze_Total'])
most_points=data_1['Total_Points'].max()
best_country=data_1[data_1['Total_Points']==most_points]['Country_Name'].values[0]
print(best_country)


# --------------
#Code starts here
best=data[data['Country_Name']==best_country].set_index('Country_Name')

best=best[['Gold_Total','Silver_Total','Bronze_Total']]
#print(best)
#plt.figure(figsize=[20,8])
best.plot(kind='bar',stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)





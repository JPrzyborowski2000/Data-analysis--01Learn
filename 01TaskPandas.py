import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import pandasgui
import tables
import regex 
# Generate Test Data01
'''
num_days = 20
temperature = np.random.uniform(20, 28, size=(num_days, 1))
pressure = np.random.uniform(990, 1010, size=(num_days, 1))
rain = np.random.uniform(0, 20, size=(num_days, 1))
random_data = np.hstack((temperature, pressure, rain))
df_weather = pd.DataFrame(index=pd.date_range("20200501", periods=num_days, freq="1D"),
                         data=random_data, columns=["Temperature", "Pressure", "Rain"])

#Print Data
print(df_weather)

#Test Data as Ditcionary
df_people = pd.DataFrame({"Height": [180, 160, 195],
                          "Weight": [77, 52, 200]})
print(df_people)

#Show data describe function
df_weather_summary = df_weather.describe()
print(df_weather_summary)

#Show data plot
df_weather.plot(kind = 'scatter', x = 'Temperature', y = 'Rain')
plt.show()

# PandasGUI
pandasgui.show(df_weather, settins ={'block':True})
'''

# Generate Test Data02
'''
vals = np.random.randn(6,4)
df = pd.DataFrame(vals, index = [0.0, 0.2, 0.3, 0.7, 1.0, 1.3], columns = ["A", "B", "C", "D"])

#print(df)
#print(df.index)
#print(df.columns)

list_of_columns = list(df.columns)

for c in list_of_columns:
    print(c)

df.values #--> data to table

#Get data from col or index
df['B']
df[['C','D']]
df[0.2:1.0]
#df.loc by name df.iloc -> like numpy array
#print(df.iloc[0:3, df.columns.get_loc('C')]) # mix index of row and name of col
#print(df.loc[(df["A"] > -0.75) & (df["B"] < 0.25), :])
'''

# Generate Test Data03 & Save and Read
'''
alpha = np.array([0, np.pi/4, np.pi/2, np.pi*3/4, np.pi])

trig = pd.DataFrame({"sinus": np.round(np.sin(alpha), 10),
                     "cosinus" : np.round(np.cos(alpha), 10),
                     "x^2" : alpha**2,
                     "random" : np.random.randn(len(alpha))}, index=alpha)

#trig.loc[0:4, "random"] = 0
trig.loc[trig["cosinus"] >= 0, "random"] = np.array([1, 3, 5])
#trig["New column"] = -1 #->New Col
#trig.loc[1337, :] = -1 #->New Row

#trig.set_index(trig["sinus"], inplace=True) -> to set new index from sinus val, inplace do not create new obj


#rename_dict = {"sinus": "sin", "cosinus": "cos"}
#trig.rename(columns=rename_dict, inplace=True) #-> change col name 

#trig.sort_values("cos", axis=0, inplace=True, ascending=False)  # sort_by_row in cosine col, same_thing, decrease

#Save and Read file

trig.to_csv("trig.csv")
trig_from_csv = pd.DataFrame(pd.read_csv("trig.csv", index_col=0)) #index_col -> col like index
print(trig)
print(trig_from_csv)

#HDF5 format is faster and more complex
trig.to_hdf("trig.hdf5", "data", format="fixed", mode="w", complevel=5)  
trig_from_hdf = pd.DataFrame(pd.read_hdf("trig.hdf5"))
'''

#Task to do with new DataSet from
#Source: https://www.kaggle.com/tanuprabhu/population-by-country-2020

#Display Data

population_data = pd.DataFrame(pd.read_csv("population_by_country_2019_2020.csv"))
#pandasgui.show(population_data)
#print("Show data in console ")
#print(population_data)
#print("\n Summary: ")
#print(population_data.describe())

#Relative and absolute value to population 2020 vs 2019

New_Population_Change = population_data.loc[:,"Population (2020)"] - population_data.loc[:,"Population (2019)"]

Population_Change = (population_data.loc[:,"Population (2020)"] - population_data.loc[:,"Population (2019)"])/population_data.loc[:,"Population (2020)"]*100

population_data["Net population change"] = New_Population_Change
population_data["Population change [%]"] = Population_Change
pd_old = population_data

#Sorted by Relative value

population_data.sort_values(by=["Population change [%]"], inplace = True, ascending = False)
#print(population_data)

#Generate a bar chart of the 10 countries that had the highest percentage population growth. Include the populations of 2019 and 2020 on it.
#Use a regular expression filter to select the columns.

population_data.set_index(population_data["Country (or dependency)"],inplace=True)

population201920_col = population_data.filter(regex=r"Population \(2020\)|Population \(2019\)")
population201920_col = population201920_col[0:10]

#print(population201920_col)
population201920_col.plot(kind='bar')
#plt.show()

#Add new col and write there 'LOW'
population_data["Density (2020)"] = 'Low'
#print(population_data)

#Count the population density and, in countries where it exceeds 500 people per km2, 
#write the word "High" in the Density column

Density2020 = population_data.loc[:,"Population (2020)"]/population_data.loc[:,"Land Area (Km²)"]
#print(Density2020)

population_data.loc[Density2020>500,"Density (2020)"] = 'High'
save_data = population_data[::2]
save_data.to_csv("endTASK.csv")
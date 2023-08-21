import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import pandasgui

# Generate Test Date
num_days = 20
temperature = np.random.uniform(20, 28, size=(num_days, 1))
pressure = np.random.uniform(990, 1010, size=(num_days, 1))
rain = np.random.uniform(0, 20, size=(num_days, 1))
random_data = np.hstack((temperature, pressure, rain))
df_weather = pd.DataFrame(index=pd.date_range("20200501", periods=num_days, freq="1D"),
                         data=random_data, columns=["Temperature", "Pressure", "Rain"])

'''
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

# New Test Data02

vals = np.random.randn(6,4)
df = pd.DataFrame(vals, index = [0.0, 0.2, 0.3, 0.7, 1.0, 1.3], columns = ["A", "B", "C", "D"])
print(df)
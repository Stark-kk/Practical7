import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/home/11404/IBI1_2020-21/Practical7")
getcwd()

covid_data = pd.read_csv("full_data.csv")
covid_data.iloc[0:9:1,0:2]


covid_data.describe()
#mean=7896
#NEW DEATHS=74544

covid_data = pd.read_csv("full_data.csv")
world_data = covid_data.loc[covid_data['location']=="World"]
world_dates = world_data["date"]
world_new_cases = world_data["new_cases"]
plt.plot(world_dates, world_new_cases, 'b+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()
#It is similar to that



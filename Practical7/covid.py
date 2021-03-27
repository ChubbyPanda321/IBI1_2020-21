#import packages
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import the data
os.chdir("D:/ZJU/IBI/python/IBI1_2020-21/Practical7")
covid_data = pd.read_csv('full_data.csv')
# show all columns, and every second row between (and including) 0 and 10
print(covid_data.iloc[0:11:2,])
# show “total cases” for all rows corresponding to Afghanistan
print(covid_data.loc[(covid_data['location']=='Afghanistan'),'total_cases'])
# extract data for later manipulation
world_new_cases = covid_data.loc[(covid_data['location']=='World'),'new_cases']
world_dates = covid_data.loc[(covid_data['location']=='World'),'date']
world_new_deaths = covid_data.loc[(covid_data['location']=='World'),'new_deaths']
# get the median and mean of world new cases
median = np.median(world_new_cases)
mean = np.mean(world_new_cases)
print('median=%s'%median)
print('mean=%s'%mean)
# make a boxplot of wnc
plt.boxplot(
    world_new_cases,
    notch=False,
    patch_artist=True,
    boxprops={'facecolor':'gray'}
    )
plt.xticks([])
plt.grid(True)
plt.title('world new cases')
plt.show()
# make plot of new cases and new deaths worldwide
plt.plot(world_dates,
    world_new_cases,
    color='royalblue',
    marker='^',
    label='world new cases'
    )
plt.plot(world_dates,
    world_new_deaths,
    color='crimson',
    marker='.',
    label='world new deaths'
    )
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-80)
plt.subplots_adjust(bottom=0.2)
plt.legend()
plt.title('WORLD NEW CASES AND DEATHS OF COVID19')
plt.show()
# places in the World where there have not yet been more than 10 total infections(as of 31 March)
low_cases_places = covid_data.loc[(covid_data['date']=='2020-03-31') & (covid_data['total_cases']<=10),'location']
print(low_cases_places)
# USING Pandas FOR CSV FILE

import pandas as pd
#CSV file
import requests
response = requests.get('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

with open('time_series_covid19_confirmed_global.csv', 'wb') as file:
    file.write(response.content)
covid_confirmed = pd.read_csv('time_series_covid19_confirmed_global.csv')


# creating a condition
condition = covid_confirmed['Country/Region'] == 'India'
covid_confirmed_india = covid_confirmed[condition]

covid_confirmed_india = covid_confirmed_india.rename(index={143: 'India'})

covid_confirmed_india.T[4:].plot()

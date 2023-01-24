import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator)
import numpy as np
import group1_output
import group2_output
import materials
#The endpoint (Group 3) develops an API to collect data from user with argparse:
#Latitude - in decimal degrees
#Longitude - in decimal degrees
#Soiltype - an integer 1-5 corresponding to the 5 FAO soil textural classes 1-5 FAO class (1-coarse, 2-Medium, 3-Medium-Fine, 4-Fine, 5-Very Fine)
#pFCritical - the soil tension from which there is plant specific stress (pF at field capacity:2.3, pF at wilting point:4.2)
#Next24Rain_treshold - the ammount of rain forecasted in the next 24h, that could prevent the irrigation event
#VPD_treshold - Vapour Pressure Deficit, below which transpiration is unlikely to occur 

#test your application with
#Latitude - 37.64
#Longitude - -7.66
#Soiltype - 3
#pFCritical - 3.1
#Next24Rain_treshold - 2
#VPD_treshold - 0.5

#Connect the dots
# 1 -Organize your user input data for easier reading
inLat                     = 37.64 # replace this value with what you collect with your API
inLon                     = -7.66 # replace this value with what you collect with your API
inSoilType                = 1 # replace this value with what you collect with your API
inpFCritical              = 3.1 # replace this value with what you collect with your API
invpd_treshold            = 0.5 # replace this value with what you collect with your API
innext24h_rain_treshold   = 2 # replace this value with what you collect with your API

# 2 - Create a dictionary of weather forecast with the group1 work. In the meantime you can use materials.Output1Group1 as a mockup result
Forecast = materials.Output1Group1

# 3 - Organize your data series
dates = Forecast['hourly']['time']
dates = list(map(lambda x: x[-8:-3], dates))# just to get the Day and Hour
#... continue to create the following lists and populate them with forecasted data
temp = [] # replace the empty list with result of group1 work
vpd = [] # replace the empty list with result of group1 work
rh = [] # replace the empty list with result of group1 work
ETo = [] # replace the empty list with result of group1 work
precipitation = [] # replace the empty list with result of group1 work
SoilMoisture_3_9 = [] # replace the empty list with result of group1 work
SoilMoisture_9_27 = [] # replace the empty list with result of group1 work

# 4 Use group2 function to create the soil tension (pF) dataseries for the two soil layers. 
pF_3_9=[] # replace the empty list with result of group2 work
pF_9_27=[] # replace the empty list the list with result of group2 work

#Decision to irrigate ( 3-9 cm)
plan_3_9 = [0] * len(dates) # replace the empty list with a list with same nr elements as 'dates', but filled with zeros
plan_9_27 = [0] * len(dates) # replace the empty list with a list with same nr elements as 'dates', but filled with zeros
plan_3_9_dates = [] # leave as is. This list will store the irrigation event for this soil layer
plan_9_27_dates = [] # leave as is. This list will store the irrigation event for this soil layer

# Decision algorithm to trigger irrigation event - Improve if you feel it nees improvement
# Rules: 1) soil tension is higher than pFCritical, 2) VPD is higher than vpd_treshold, 3) the sum of rain in the next 24 hours is less than 1 liter per m2
for idx,i in enumerate(vpd):
    next24_rain = sum(precipitation[idx:idx+24])
    if pF_3_9[idx]>=inpFCritical and vpd[idx] > invpd_treshold and next24_rain < innext24h_rain_treshold:
        if sum(filter(None, plan_3_9))<1:
            plan_3_9[idx] = 1
            plan_3_9_dates.append(dates[idx])
    if pF_9_27[idx]>=inpFCritical and vpd[idx] > invpd_treshold and next24_rain < innext24h_rain_treshold:
         if sum(filter(None, plan_9_27))<1:
            plan_9_27[idx] = 1
            plan_9_27_dates.append(dates[idx])
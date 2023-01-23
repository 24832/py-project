# **py-project**

    GDS - Python class project

## **Introduction and mission set up**


You have been assigned to a working group, which will contribute to a collaborative project. The collaborative project has 3 working groups contributing to a common goal:

**The development of a decision support tool for irrigation needs for 1) early stage plants, 2) established plants**

The decision to irrigate relies on the following 3 premises:

- Soil water tension (pF) should be above certain threshold defined by user/farmer (e.g. 3.2 log (-h))
- Irrigation decision should account for the rain forescast in the next 24 hours, i.e. if ammount of rain is over a certain threshold (defined by user), no need to irrigate (e.g. 2 mm)
- Irrigation, even if needed, should not occur if vapour pressure deficit is below a certain threshold, defined by user (e.g. 0.5 kPa)
Each group will focus on a part of this tool

**Group 1** - Will Retrieve weather data and soil state predictions from online api
delivers/continue the file group1.py

**Group 2** - Calculates soil tension (pF)
delivers/continue the file group2.py

**Group 3 (end point)** - Creates the API to interact with enduser
delivers/continue the file group3_endpoint.py
the file materials.py provides supporting code


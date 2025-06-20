**Project status**: Completed - closed.

This project is a data analysis of a publicly available data from: 
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv

The project consists of data analysis and data modeling of historical wildfires in Australia by using Pandas, Matplotlib, Numpy and Seaborn Python libraries. 
All data was pushed and managed on Github via Git bash. The data did not require cleaning so this step was omitted.


**Structure of the project is as follows:**


_Folder "data":_
- "Historical_wildfires" : File with input data used for analysis.


_Folder "scripts":_
- "data_cleaning_exploration.py" : Python file used for data cleaning, basic exploration of data and generating 'dleaned_data.csv'.


_Folder "outputs":_
- "fire_area_change.png" : Line plot with change of average estimated area change between years.
- "fire_area_change_month.png" : Line plot with change of average estimated area change between months.
- "fire_brightness_regions.png" : Bar chart showing mean estimated fire brightness per region.
- "fire_brightness_regions_hist.png" : Histogram showing mean estimated fire change between regions.
- "fire_power.png" : Scatter plot showing mean estimated fire power vs. mean confidence.
- "fire_vegetation.png" : Pie chart showing percentage for presumed vegetation fires by region.
- "australia_map.html" : Canada map with marked regions.
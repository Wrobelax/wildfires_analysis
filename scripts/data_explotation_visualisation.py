"""This is a script for data exploration and visualisation used for generating outputs.
Some lines with code are commented as they were used solely for analysis and left for reference.
"""


# Modules importing.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import datetime as dt


# Importing file with cleaned data into dataframe.
source = "../data/Historical_Wildfires.csv"
df = pd.read_csv(source)



"""Basic data exploration"""
# print(df.head()) # 5 rows, 10 columns.
# print(df.columns) # 'Region', 'Date', 'Estimated_fire_area', 'Mean_estimated_fire_brightness', 'Mean_estimated_fire_radiative_power', 'Mean_confidence', 'Std_confidence', 'Var_confidence', 'Count', 'Replaced'
# print(df.dtypes) # Region, Date and Replaced - objects. Count - int. Rest float.
# print(df["Region"].unique()) # 'NSW' 'NT' 'QL' 'SA' 'TA' 'VI' 'WA'


# Changing "Date" into datatime and extracting year and month.
df["Year"] = pd.to_datetime(df["Date"]).dt.year
df["Month"] = pd.to_datetime(df["Date"]).dt.month
# print(df.dtypes) # Verifying changes



"""Variables creation, grouping, sorting etc."""
# Grouping.
df_fire_area_change = df.groupby("Year")["Estimated_fire_area"].mean()
df_fire_area_change_month = df.groupby(["Year", "Month"])["Estimated_fire_area"].mean()
df_region_count = df.groupby("Region")["Count"].sum()

# Folium.
region_data = {"region" : ["NSW", "QL", "SA", "TA", "VI", "WA", "NT"],
               "Lat" : [-31.8759835,-22.1646782,-30.5343665,-42.035067,-36.5986096,-25.2303005,-19.491411],
               "Lon" : [147.2869493,144.5844903,135.6301212,146.6366887,144.6780052,121.0187246,132.550964]}
reg = pd.DataFrame(region_data)


"""Visualisation"""
# Change in average estimated fire area over time.
plt.figure(figsize = (12, 6))
df_fire_area_change.plot(x = df_fire_area_change.index, y = df_fire_area_change.values, color = "darkred")

plt.title("Estimated Fire Area Over Time")
plt.xlabel("Year")
plt.ylabel("Average Estimated Fire Area (km²)")

# plt.savefig("../outputs/fire_area_change.png") # Saving results to file


# Change in average estimated fire area over time. Grouped by Year and Month.
plt.figure(figsize = (12, 6))
df_fire_area_change_month.plot(x = df_fire_area_change_month.index, y = df_fire_area_change_month.values, color = "violet")

plt.title("Estimated Fire Area Over Time")
plt.xlabel("Year, Month")
plt.ylabel("Average Estimated Fire Area (km²)")

# plt.savefig("../outputs/fire_area_change_month.png") # Saving results to file


# Mean estimated fire brightness across the regions.
plt.figure(figsize = (12, 6))
sns.barplot(data = df, x = "Region", y = "Mean_estimated_fire_brightness", color = "darkgreen")

plt.title("Distribution of Mean Estimated Fire Brightness across Regions")
plt.xlabel("Region")
plt.ylabel("Mean Estimated Fire Brightness (Kelvin)")

# plt.savefig("../outputs/fire_brightness_regions.png") # Saving results to file


# Mean estimated fire brightness across the regions - histogram.
plt.figure(figsize = (10, 6))
sns.histplot(data = df, x = "Mean_estimated_fire_brightness", hue = "Region", multiple = "stack")

plt.title("Mean Estimated Fire Brightness across Regions")
plt.xlabel("Count")
plt.ylabel("Mean Estimated Fire Brightness (Kelvin)")

# plt.savefig("../outputs/fire_brightness_regions_hist.png") # Saving results to file


# Percentage of Pixels for Presumed Vegetation Fires by Region.
plt.figure(figsize = (14, 9))
explode = [0, 0, 0, 0.1, 0.1, 0.1, 0]

plt.pie(df_region_count, labels = df_region_count.index, autopct = "%1.1f%%", explode = explode, shadow = True)

plt.title("Percentage of Pixels for Presumed Vegetation Fires by Region")
plt.axis("equal")

# plt.savefig("../outputs/fires_vegetation.png") # Saving results to file


# Mean Estimated Fire Radiative Power vs. Mean Confidence.
plt.figure(figsize = (8, 6))
sns.scatterplot(data = df, x = "Mean_confidence", y = "Mean_estimated_fire_radiative_power")

plt.title("Mean Estimated Fire Radiative Power vs. Mean Confidence")
plt.xlabel("Mean Estimated Fire Radiative Power (MW)")
plt.ylabel("Mean Confidence")

# plt.savefig("../outputs/fire_power.png") # Saving results to file


# Regions marking.
australia_regions = folium.map.FeatureGroup()
australia_map = folium.Map(location = [-25, 135], zoom_start = 4)

for lat, lng, lab in zip(reg.Lat, reg.Lon, reg.region):
    australia_regions.add_child(
        folium.features.CircleMarker(
            [lat,lng],
            popup = lab,
            radius = 5,
            color = "red",
            fill = True,
            fill_color = "blue",
            fill_opacity = 0.6
        )
    )

australia_map.add_child(australia_regions)
# australia_map.save("../outputs/australia_map.html") # Saving results to file

# plt.show() # Uncomment to generate all charts.
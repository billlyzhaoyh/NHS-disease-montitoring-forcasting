#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import libraries
import pandas as pd
import numpy as np
import folium
from tqdm import tqdm
 
# Load the shape of the zone (US states)
# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
# You have to download this file and set the directory where you saved it
from urllib.request import urlopen
import json
def main():
	url_geo = "https://opendata.arcgis.com/datasets/ef3c7d5a49c24aa7a318e95f93564899_0.geojson"
	with urlopen(url_geo) as response:
	    ccg = json.load(response)
	    
	print('json loaded')
	# Load the unemployment value of each state
	# Find the original file here: https://github.com/python-visualization/folium/tree/master/examples/data
	list_of_csv=['asian.csv','black.csv','other.csv','mixed.csv']
	for csv in tqdm(list_of_csv):
		name_map=csv.split('.')[0]
		data = pd.read_csv(csv)
		columns_to_select=['GeoCode','Relative_difference']
		data=data[columns_to_select]
		updated_rel_difference=np.asarray(data['Relative_difference'].values.tolist())
		data['Relative_difference']=np.abs(updated_rel_difference)*100

		# Initialize the map:
		m = folium.Map(location=[51, -0], zoom_start=5)

		# Add the color for the chloropleth:
		folium.Choropleth(
		 geo_data=ccg,
		 name='choropleth',
		 data=data,
		 columns=['GeoCode', 'Relative_difference'],
		 key_on='feature.properties.CCG19CD',
		 fill_color='YlGn',
		 fill_opacity=0.7,
		 line_opacity=0.2,
		 legend_name='Relaive difference between expected number of diagnosis and actual number of diagnosis'
		).add_to(m)
		folium.LayerControl().add_to(m)
		# Save to html
		print('Folium map generated and now saving it')
		m.save(name_map+'.html')

if __name__ == '__main__':
    main()


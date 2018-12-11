""" Visualizing RCMP Open Data with gmplot"""
import sys
import pandas as pd
import gmplot


def main(args):
    # Get stolen bike data
    bike_data = pd.read_json('https://opendata.arcgis.com/datasets/9a2dba0f0fed47e08ab179fe9eae4104_0.geojson')
    # TODO: take data category as a parameter 

    # Parse out lat and long;
    # TODO: make it an object with more props and then map a pin instead of a shape
    latitude = []
    longitude = []

    for index, row in bike_data.iterrows():
        latitude.append(row['features']['properties']['Lat'])
        longitude.append(row['features']['properties']['Long'])

    # Place map
    gmap = gmplot.GoogleMapPlotter(43.70011, -79.4163, 13)

    # Scatter points
    gmap.scatter(latitude, longitude, '#3B0B39', size=15, marker=False)

    # Marker
    hidden_gem_lat, hidden_gem_lon = 37.770776, -122.461689
    gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')

    # Draw
    gmap.draw("output.html")


if __name__ == "__main__":
    main(sys.argv)


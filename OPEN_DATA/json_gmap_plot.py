import sys, gmplot
import pandas as pd


DEFAULT_DATASET = 'https://opendata.arcgis.com/datasets/9a2dba0f0fed47e08ab179fe9eae4104_0.geojson'


def main(argv):
    try:
        input_file = argv[1] if len(argv) > 1 else DEFAULT_DATASET 
        bike_data = pd.read_json(input_file)
        
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
        gmap.draw("plot_output.html")
    except ValueError as exception:
        print(exception)


if __name__ == "__main__":
    main(sys.argv)


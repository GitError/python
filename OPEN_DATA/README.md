### JSON GMap Plot
A simple script to visualize JSON datasets from the [RCMP Open Data](https://hub.arcgis.com/pages/open-data) onto Google Maps in the Greater Toronto Area

### Script Usage
python plot_data.py [api_data_set_url]

#### Defaults
- api_data_set_url: [Stolen bikes in the Greater Toronto Area](https://opendata.arcgis.com/datasets/9a2dba0f0fed47e08ab179fe9eae4104_0.geojson) 
- output_file: \\.plot_output.html

#### TODO
- find an alternative to google maps api
- map generic object for json data point
- make plot location an argument [long, lat, zoom]
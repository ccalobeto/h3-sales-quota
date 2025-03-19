import json
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point, box
import topojson as tp

def getAreaCodeId(df, topojson, level = 'level3'):
  ## detect the areaCodeId given the coordinates
  
# load cartography canton and convert to geopandas
  with open(topojson) as f:
    carto_load = json.load(f)
  area_code_topo = tp.Topology(carto_load, object_name=level)
  area_code_dict = json.loads(area_code_topo.to_geojson())
  area_code_gdf = gpd.GeoDataFrame.from_features(area_code_dict['features']) 
  
  # convert bbox into a polygon
  geom = box(*area_code_gdf.total_bounds)
  
  df2 = df.copy()
  # prepare the coordinates and convert to geopandas
  df2['coordinates'] = list(zip(df2['longitud'], df2['latitud']))
  df2['coordinates'] = df2['coordinates'].apply(Point)
  # check if the coordinates are inside Ecuador
  df2['in_bounds'] = df2.apply(lambda x: geom.contains(x['coordinates']), axis=1)
  df2_gdf = gpd.GeoDataFrame(df2, geometry='coordinates')

  # https://autogis-site.readthedocs.io/en/2019/notebooks/L3/spatial_index.html
  # spatial join
  sjoin = gpd.sjoin(df2_gdf, area_code_gdf, how='left')
  df3 = pd.DataFrame(sjoin)
  
  df3.rename(columns={'id': 'areacd_recalculated'}, inplace=True)
  # remove unused columns
  df3.drop(columns=['coordinates', 'index_right'], inplace=True)
  return df3
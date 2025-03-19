import pandas as pd
import numpy as np
import glob
from utils import getAreaCodeId 

# specify the folder path containing csv files
folder_path = './static/data/input/'
output_path = './static/data/output/'

topo_file = "./static/data/input/support/peru-100k.json"

# get a list of all csv files in the folder
csv_files = glob.glob(folder_path + '/*.csv')

# initialize an empty list to store the dataframes
dfs = []

# loop through each csv file and append to the list of dataframes
for file in csv_files:
    df = pd.read_csv(file, 
                     usecols=['id', 'especifico', 'longitud', 'latitud','anio', 'areacd', 'modalidad'],
                     dtype={'areacd': str})
    dfs.append(df)
    

# concatenate all dataframes into a single dataframe
df_concat_ = pd.concat(dfs, ignore_index=True)

df_concat_.rename(columns={
    'anio': 'año', 'id': 'incident_id'}, inplace=True)

# detect the areaCodeId
df_concat = getAreaCodeId(df_concat_, topo_file, 'level4')

# filter sample of MIRAFLORES
df_sample = df_concat[['incident_id', 'longitud', 'latitud', 'año', 'areacd', 'areacd_recalculated']]
df_sample = df_sample[df_sample['areacd_recalculated'] == '150122'].sample(n=5000)

df_sample['ticket'] = np.random.normal(122, 66, 5000) 

# export the concatenated dataframe to a parquet file
df_concat.to_parquet(output_path + 'output.parquet', index=False)
df_sample.to_parquet(output_path + 'synthetic.parquet', index=False)
df_sample.to_csv(output_path + 'synthetic.csv', index=False)

# exported files
print('3 files created in ' + output_path)
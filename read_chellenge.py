import pandas as pd
import json

def convert(file):
    data_json = pd.read_json(file)[0:1000]
    data_json.to_hdf('user_study.h5', key='df1')

convert('user_data.json')
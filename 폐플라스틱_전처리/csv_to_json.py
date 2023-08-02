import csv
import json
import pandas as pd

df = pd.read_csv('./폐플라스틱 이미지 데이터/modified_data.csv')
json_string = df.to_json(orient='records')

with open('./file.json', 'w') as f:
    f.write(json_string)



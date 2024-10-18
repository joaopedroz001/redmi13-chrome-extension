from getData import getData
import json 

data = getData()

with open('data.json', 'w') as json_file:
  json.dump(data, json_file, indent=2)
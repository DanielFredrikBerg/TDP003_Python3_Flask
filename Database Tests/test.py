#!/usr/bin/python3
import json

with open('data.json', 'r') as json_file:
    for line in json_file:
        print(line)
    # data = json.load(json_file)
    # for p in data:
    #     print(p['project_name'])

s_list = sorted(data, key=lambda p_id: p_id['project_id'])

project_id_list = [p_id['project_id'] for p_id in s_list]
print(project_id_list)

#print(s_list)

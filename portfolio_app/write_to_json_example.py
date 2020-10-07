#!/usr/bin/python3
import sys
import json

project = {
        "start_date": "2019-09-08",
        "short_description": "no",
        "course_name": "tdp003",
        "long_description": "no no no",
        "group_size": 3,
        "academic_credits": "WUT?",
        "lulz_had": "medium",
        "external_link": "YY",
        "small_image": "X",
        "techniques_used": [
            "ada",
            "python"
        ],
        "project_name": "Daniel Test",
        "course_id": "TDP003",
        "end_date": "2009-09-09",
        "project_id": 5,
        "big_image": "XXX"
}

json_project = json.dumps(project)

file_name = sys.argv[1]

with open(str(file_name), 'r') as json_file:
    db = sorted(json.load(json_file), key=lambda project: int(project['project_id']))

db.append(project)
print(db)

with open(str(file_name), 'w') as json_file:
    json.dump(db, json_file)

    
with open(str(file_name), 'r') as json_file:
    db = sorted(json.load(json_file), key=lambda project: project['project_id'])
print('opening db again')
print(db)

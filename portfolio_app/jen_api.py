#!/usr/bin/python3
import json
import copy
import sys

def load(path):
	"""Loads json from `path` and returns list sorted on projects ID"""
	try:
		with open(str(path), 'r') as data:
                        return sorted(json.load(data), key=lambda project: project['project_id'])
	except Exception as e:
		print('invalid json: %s' % e)
		return None

def add_project(db, project):
	"""Adds project to `db`"""
	db.append(project)

def remove_project(db, id_):
        """Removes project from 'db' if id matches project."""
        for project in db:
                if project['project_id'] == id_:
                        db.remove(project)
        
def write_db_to_json(db, save_file):
	"""Writes `db` to file with path `save_file`, overwriting existing data."""
	with open(str(save_file), 'w') as json_file:
		json.dump(db, json_file)

def get_project_count(db):
	"""Returns int of how many projects in `db`'"""
	return len(db)

def get_project(db, id_):
	"""Returns `project` matching `id` in `db`."""
	for project in db:
		if project['project_id'] == id_:
			return project

def search(db, sort_by='start_date', sort_order='desc', techniques=None, search=None, search_fields=None):
	"""##Search
	Will return a list of projects in `db` matching **all** search requirements:

	1. Only match projects containing all `techniques`.

	2. Only match projects containing string `search` in atleast **one** field in `search_fields`.
		If `search_fields` is empty, all fields will be checked.

	Will sort by field `sort_by`. In ascending order if `sort_order` has value `desc`, descending if value is `asc`.
	"""
	projects = copy.deepcopy(db)
	try:
		if techniques:
			projects = [project for project in projects if set([str(technique).lower() for technique in techniques]).issubset(project['techniques_used'])]
			#projects = [project for project in projects for technique in project['techniques_used'] if all(str(x).lower() in str(technique).lower() for x in techniques)]
			#projects = [project for project in projects if all(str(x).lower() in str(technique).lower() for technique in project['techniques_used'] for x in techniques)]
	except Exception:
		print("Failed searching for techniques.")
	if search:
		if search_fields == None:
			projects = [project for project in projects if str(search).lower() in " ".join([str(item[1]) for item in project.items()]).lower()]
		elif isinstance(search_fields, list):
			projects = [project for project in projects for search_field in search_fields if str(search).lower() in str(project[search_field]).lower()]
	if sort_order == 'desc':
		isreverse = True
	elif sort_order == 'asc':
		isreverse = False
	return sorted(projects, key=lambda results: results[sort_by], reverse=isreverse)

def get_technique_stats(db):
	"""Returns a dictionary where all techniques used are the keys, and the contents are lists of dictionaries of projects IDs and names."""
	return {technique: [{'id': project['project_id'], 'name': project['project_name']} for project in search(db, search=technique, search_fields=['techniques_used'])] for technique in get_techniques(db)}

def get_search_fields(db):
	"""Returns available fields to search in `db`."""
	return db[0].keys()

def get_techniques(db):
	"""Returns available techniques in `db`."""
	return list(dict.fromkeys(sorted([techniques for project in db for techniques in project['techniques_used']])))


def main():
	"""Only used for testing purposes."""
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
	f = sys.argv[1]
	db = load(f)
	add_project(db, project)
	# Write will overwrite file f.
	write_db_to_json(db, f)
	db = load(f)
	print(db)

if __name__ == '__main__':
	main()

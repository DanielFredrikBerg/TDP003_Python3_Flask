import json
import copy

def load(path):
	try:
		with open(path, 'r') as data:
			return sorted(json.load(data), key = lambda project: project['project_id'])
	except Exception:
		return None

def get_project_count(db): return len(db)

def get_project(db, id):
	for project in db:
		if project['project_id'] == id:
			return project

def search(db, sort_by='start_date', sort_order='desc', techniques=None, search=None, search_fields=None):
	projects = copy.deepcopy(db)
	try:
		if techniques:
			projects = [project for project in projects for technique in project['techniques_used'] if all(str(x).lower() in str(technique).lower() for x in techniques)]
	except Exception:
		print("Failed searching for techniques.")
	if search:
		if search_fields == None:
			projects = [project for project in projects if str(search).lower() in str(project).lower()]
		elif isinstance(search_fields, list):
			projects = [project for project in projects for search_field in search_fields if str(search).lower() in str(project[search_field]).lower()]
	if sort_order == 'desc':
		isreverse = True
	elif sort_order == 'asc':
		isreverse = False
	return sorted(projects, key=lambda results: results[sort_by] , reverse=isreverse)

def get_technique_stats(db): return {technique: [{'id': project['project_id'], 'name': project['project_name']} for project in search(db, search=technique, search_fields=['techniques_used'])] for technique in get_techniques(db)}

def get_techniques(db): return list(dict.fromkeys(sorted([techniques for project in db for techniques in project['techniques_used']])))

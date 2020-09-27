#!/usr/bin/python3
import json
import sys

#This file includes the implemented functions for our API
def catch(func, handle=lambda e: e, *args, **kwargs):
        try:
                return func(*args, **kwargs)
        except Exception as e:
                return handle(e)
        
def load(json_file):
        try:
                with open(str(json_file), 'r') as json_file:
                        data = json.load(json_file)
                        db = sorted(data, key=lambda p_id: p_id['project_id'])
                return db
        except Exception as e:
                return None

def get_project_count(db):
        return len([project['project_id'] for project in db])

def get_project(db, p_id):
        for project in db:
                if project['project_id'] == p_id:
                        return project
        return None

def search(db, sort_by='start_date', sort_order='desc', techniques=None, search=None, search_fields=None):
        search_results = []
        if search != None:
                search = str(search).lower()        
        elif techniques != None:
                
        elif search_fields == None:
                for project in db:
                        for key in project.keys():
                                field_lc = str(project[key]).lower()
                                if field_lc == None:
                                        break
                                elif field_lc.__contains__(search):
                                        search_results.append(project)
                                        print(field_lc)
                                        break
        elif search_fields != None:
                for project in db:
                        for search_field in search_fields:
                                search_field_lc = str(project[search_field]).lower()
                                if search_field_lc.__contains__(search):
                                        search_results.append(project)
                                        break
        if sort_order == 'desc':
                sorted_search_results = sorted(search_results, key=lambda results: results[sort_by], reverse=True)
        elif sort_order == 'asc':
                sorted_search_results = sorted(search_results, key=lambda results: results[sort_by])
        return sorted_search_results


def get_techniques(db):
        big_t_list = [project['techniques_used'] for project in db]
        return list(dict.fromkeys(sorted([technique for mini_tech_list in big_t_list for technique in mini_tech_list])))

def get_technique_stats(db):
        t_dict = {}
        technique_list = get_techniques(db)
        for technique in technique_list:
                t_dict[technique] = []
        for p_id in range(get_project_count(db)):
                if len(db[p_id]['techniques_used']) > 0:
                        project_techniques = db[p_id]['techniques_used']
                        for p_tech in project_techniques:
                                t_dict[p_tech].append({'id': p_id + 1, 'name': db[p_id]['project_name']})
        return t_dict

def main():
        p_list = load(sys.argv[1])
       # print(get_project_count(p_list))
        #print(get_project(p_list, 0))
        print(get_techniques(p_list))
        #print(search(p_list, sort_by='start_date', sort_order='desc', techniques=None, search='python', search_fields=None))
        #print(get_technique_stats(p_list))
        
        




if __name__ == '__main__':
        main()
else:
        print('nothing')

#!/usr/bin/python3
import json
import sys

# ******This file includes the implemented functions for our Datalayer*********************

def load(json_file):
    """Attempts to load JSON file json_file. Returns project list sorted by key project_id. Returns None if unsuccessful."""
    try:
        with open(str(json_file), 'r') as json_file:
            data = json.load(json_file)
        return sorted(data, key=lambda p_id: p_id['project_id'])
    except Exception as e:
        print('invalid json: %s' % e)
        return None


def add_project(db, project):
    """Adds project to current project list."""
    db.append(project)


def write_db_to_json(db, save_file):
    """Writes current project list in JSON format to save_file"""
    with open(str(save_file), 'w') as json_file:
        json.dump(db, json_file)


def get_project_count(db):
    """Returns amount of projects in project list."""
    return len(db)


def get_project(db, p_id):
    """Returns project with 'project_id' p_id if it exists in project list otherwise returns None"""
    aquired_project = [
        project for project in db if project['project_id'] == p_id]
    return aquired_project[0] if len(aquired_project) > 0 else None
    # for project in db:
    #         if project['project_id'] == p_id:
    #                 return project
    # return None


def search(db, sort_by='start_date', sort_order='desc', techniques=None, search=None, search_fields=None):
    """Returns sorted unique project list matching techniques, search and search_fields requirements.
    If all are None, returns whole project list."""
    search_results = []
    #print(techniques, search, search_fields, marker, sep='\t')
    if techniques == None and search == None and search_fields == None:
        #print('returning whole database')
        search_results = [project for project in db]
        if sort_order == 'desc':
            is_reverse = True
        elif sort_order == 'asc':
            is_reverse = False
        return sorted(search_results, key=lambda results: results[sort_by], reverse=is_reverse)
    if search != None:
        search = str(search).lower()
        #print('Search: ' + str(search))
    if techniques != [] and techniques != None:
        #print('searching in techniques')        
        #print('sEarch_result:', search_results, sep='\t')
        search_results = []
        for project in db:
            for technique in techniques:
                for p_tech in project['techniques_used']:
                    if p_tech.__contains__(str(technique).lower()):
                        if search_results.__contains__(project):
                            break
                        else:
                            search_results.append(project)
                            break

    if search_fields == None:
        #print('searching in all search fields')
        for project in db:
            for key in project.keys():
                field_lc = str(project[key]).lower()
                if search == None:
                    break
                elif field_lc.__contains__(search):
                    if search_results.__contains__(project):
                        break
                    else:
                        search_results.append(project)
                        break
    if search_fields != None:
        #print('searching in specific search fields')
        # Search results returns too many projects when many search_fields are chosen.
        #search_results = [project for project in db for search_field in search_fields if str(
        #    project[search_field]).lower().__contains__(search)]
        #print('seArch_result:', search_results, sep='\t')
        for project in db:
                for search_field in search_fields:
                        search_field_lc = str(project[search_field]).lower()
                        if search_field_lc.__contains__(search):
                                if search_results.__contains__(project):
                                        break
                                else:
                                        search_results.append(project)
                                        break
    if sort_order == 'desc':
        is_reverse = True

    elif sort_order == 'asc':
        is_reverse = False
    #print('len of search_results   ' + str(len(sorted_search_results)))
    return sorted(search_results, key=lambda results: results[sort_by], reverse=is_reverse)


def get_search_fields(db):
    """Returns list of search_fields used by projects in project list."""
    return db[0].keys()


def get_techniques(db):
    """Returns list of all techniques used in project list."""
    #big_t_list = [project['techniques_used'] for project in db]
    return list(dict.fromkeys(sorted([technique for mini_tech_list in [project['techniques_used'] for project in db] for technique in mini_tech_list])))


def get_technique_stats(db):
    """Returns dict with statistics for all techniques used in project list."""
    t_dict = {}
    technique_list = get_techniques(db)
    for technique in technique_list:
        t_dict[technique] = []
    for p_id in range(get_project_count(db)):
        if len(db[p_id]['techniques_used']) > 0:
            project_techniques = db[p_id]['techniques_used']
            for p_tech in project_techniques:
                t_dict[p_tech].append(
                    {'id': p_id + 1, 'name': db[p_id]['project_name']})
    #print("This is t_dict: ", t_dict, sep='\t')
    return t_dict


def main():
    """Used for testing functions."""
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
    print(db)
    add_project(db, project)
    db = load(f)
    print(get_project_count(db))

    # db = load(sys.argv[1])
    # print(get_project_count(p_list))
    # print(get_project(p_list, 0))
    # print(len(get_techniques(p_list)))
    # print(len(search(p_list)))
    # print(len(search(p_list)))
    # print(get_technique_stats(p_list))


if __name__ == '__main__':
    main()
else:
    print('nothing')

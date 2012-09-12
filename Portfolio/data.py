import json

def load(filename):
    try:
        data = []
        json_data=open(filename)
        data = json.load(json_data)
        json_data.close()
        return data
    except IOError:
       # print("File does not exist!")
        pass

def get_project(db,id):
    for x in range(get_project_count(db)):
        if db[x]['project_no'] == id:
            return db[x]


def get_project_count(db):
    return len(db)


def search(db, sort_by=u'start_date',sort_order=u'desc',techniques=None,search=None,search_fields=None):
    search_list = []
    proj_count = get_project_count(db)
    
    if search == None and techniques == None and search_fields == None:
        for x in range(proj_count):
            search_list.append(db[x])
    elif search == None and techniques != None:
        for x in range(proj_count):
            for tech in db[x]['techniques_used']:
                if tech == techniques[0]:
                    search_list.append(db[x])
                    print(tech)
    elif search != None:
        for x in range(proj_count):
            for fields in db[x]:
                if db[x][fields] == search:
                    search_list.append(db[x])
    
    if sort_order == 'desc':
        search_list = sorted(search_list, key=lambda x: x[sort_by],reverse=True)
    elif sort_order == 'asc':
        search_list = sorted(search_list, key=lambda x: x[sort_by])
    print(len(search_list))
    return search_list

def get_techniques(db):
    """Fetches a list of all the techniques from the specified project list and sorts them"""
    tech_list = []
    for x in range(get_project_count(db)):
        for b in db[x]['techniques_used']:
            if b not in tech_list:
                tech_list.append(b)
    tech_list.sort()
    return tech_list

def get_technique_stats(db):
    tech_dict = {}
    tech_list = []
    techniques = get_techniques(db)
    for _tech in techniques:
        for x in range(get_project_count(db)):
            if _tech in db[x]['techniques_used']:
                project_dict = {}
                project_dict['id'] = db[x]['project_no']
                project_dict['name'] = db[x]['project_name']
                tech_list.append(project_dict)
        tech_list = sorted(tech_list, key=lambda x: x['name'])
        tech_dict[_tech] = tech_list
        tech_list = []
    return tech_dict
    
db = load('data.json')
search(db,techniques =[u'csv'])

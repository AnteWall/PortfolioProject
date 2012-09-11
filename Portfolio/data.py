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
    pass

def get_techniques(db):
    """Fetches a list of all the techniques from the specified project list and sorts them"""
    tech_list = []
    for x in range(get_project_count(db)):
        for b in db[x]['techniques_used']:
            if b not in tech_list:
                tech_list.append(b)
    tech_list.sort()
    return tech_list

def get_techniques_stats(db):
    """techniques = get_techniques(db)
    tech_stats = {} 
    for tech in techniques:
        for x in range(get_project_count(db)):
            if tech in db[x]['techniques_used']:
                tech_stats.update([{tech:db[x]['project_no']}])
                tech_stats.update([{tech:db[x]['course_id']}])
 
    return tech_stats"""

db = load('data.json')
print(get_techniques_stats(db))

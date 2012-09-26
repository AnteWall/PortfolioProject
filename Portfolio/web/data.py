#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,unicodedata

def init():
    return load("our_data.json")

def load(filename):
    """Loads JSON formatted project data from a file and returns a list."""
    try:
        data = []
        json_data=open(filename)
        data = json.load(json_data)
        json_data.close()
        return data
    except IOError:
        #If trying to load that does not exist, display error message
        print("File does not exist :" + filename)

def get_project(db,id):
    """Fetches the project with the specified id from the specified list."""
    id = int(id)
    for x in range(get_project_count(db)):
        if db[x]['project_no'] == id:
            return db[x] 
    return None


def get_project_count(db):
    """ Retrieves the number of projects in a project list."""
    return len(db)

def get_fields(db):
    """Returns all fields in database"""
    returnList = []
    for i in range(get_project_count(db)):
        for a in db[i]:
            if a.replace("_", " ") not in returnList:
                returnList.append(a.replace("_", " "))
    return returnList

def search(db, sort_by=u'start_date',sort_order=u'desc',techniques=None,search=None,search_fields=None):
    """ Fetches and sorts projects matching criteria from the specified list."""

    #If search is filled with a value, unicode it so that special charachters works:
    if search != None:
        try:
            search = unicode(search, 'utf-8')
        except TypeError:
            pass

    search_list = []

    #Get number of projects in database
    proj_count = get_project_count(db)
    
    #If nothing is set, display all project in database
    if (search == None or search == "") and techniques == None and search_fields == None:
        for x in range(proj_count):
            search_list.append(db[x])
    #if searching by techniques
    elif search == None and techniques != None:
        for x in range(proj_count):
            for tech in db[x]['techniques_used']:
                if tech == techniques[0]:
                    search_list.append(db[x])
    #if searching by search and with special search fields
    elif search != None and search_fields != None:
        for x in range(proj_count):
            for z in search_fields:
                if equalIgnoreCase(db[x][z],search):
                    search_list.append(db[x])

    #If only search parameter is set
    elif search != None:
        for x in range(proj_count):
            for fields in db[x]:
                if equalIgnoreCase(search,db[x][fields]):
                    search_list.append(db[x])
                    break

    #Sorts the fields by descending or ascending before returning it
    if sort_order == 'desc':
        search_list = sorted(search_list, key=lambda x: x[sort_by],reverse=True)
    elif sort_order == 'asc':
        search_list = sorted(search_list, key=lambda x: x[sort_by])
    return search_list

def equalIgnoreCase(a, b):
    """Ignores case sensativiy"""
    #Try,except if it is Unicode
    try:
        a = str(a)
        b = str(b)
    except UnicodeEncodeError:
        pass
    #Try,except incase a or b is int
    try:
        if a.lower() in b.lower():
            return True
        else:
            return False
    except AttributeError:
        if a in b:
            return True
        else:
            return False

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
    """Collects and returns statistics for all techniques in the specified project list."""
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

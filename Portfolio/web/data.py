#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,unicodedata, time
from time import gmtime, strftime
#import texttable as tt

def init():
    db = load("our_data.json")
    errorCode = 0
    write_log(errorCode, "Initiated databasefile:")
    return db

def load(filename):
    """Loads JSON formatted project data from a file and returns a list."""
    try:
        data = []
        json_data=open(filename)
        data = json.load(json_data)
        json_data.close()
        write_log(0, "Loaded Databasefile:")
        return data
    except IOError:
        write_log(1,"Loaded Databasefile:")


def get_project(db,id):
    """Fetches the project with the specified id from the specified list."""
    id = int(id)
    for x in range(get_project_count(db)):
        if db[x]['project_no'] == id:
            write_log(0,"Fetched project id:")
            return db[x] 
    write_log(2,"Fetched project id:")
    return None


def get_project_count(db):
    """ Retrieves the number of projects in a project list."""
    write_log(0,"Fetched number of projects:")
    return len(db)

def get_fields(db):
    """Returns all fields in database"""
    returnList = []
    for i in range(get_project_count(db)):
        for a in db[i]:
            if a not in returnList:
                returnList.append(a)
    write_log(0,"Fetched all fields in database:")
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
    elif techniques != None and (search == None or search == ""):
        if search == None or search == "":
            for x in range(proj_count):
                for tech in db[x]['techniques_used']:
                    if tech in techniques and not db[x] in search_list:
                        search_list.append(db[x])
    
#if searching by search and with special search fields
    elif search != None and search_fields != None:
        for x in range(proj_count):
            for z in search_fields:
                if equalIgnoreCase(search,db[x][z]):
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
    
    write_log(0,"Searched database:")
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
        try:
            if a in b:
                return True
            return False
        except TypeError:
            if a == b:
                return True
            return False

def get_techniques(db):
    """Fetches a list of all the techniques from the specified project list and sorts them"""
    tech_list = []
    for x in range(get_project_count(db)):
        for b in db[x]['techniques_used']:
            if b not in tech_list:
                tech_list.append(b)
    tech_list.sort()
    write_log(0,"Fetched all techniques:")
    return tech_list/home/dan/Dropbox/Lab med Thaimat/TDP003/PortfolioProject/Portfolio/web

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

    write_log(0,"Fetched all techniques in the specified project:")
    return tech_dict

def write_log(errorCode,message):
    """ Writes errorCode and message to log file"""
    strftime("%Y-%m-%d %H:%M:%S", gmtime())
    #ErrorCode 1  = OK ErrorCode 2 = Could not access Database File ErrorCode3  = Project ID does not exist
    _errorMessage = ['OK','Could not access Database file.','Project ID does not exist.',]
    #Open Log file or creates one if it does not exist
    log_file = open("log/log.txt","a+r")
    # Get Current time and date
    date = str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    #Write to file
    log_file.write(date +"\t"*2 + _errorMessage[errorCode] + "\t" + message  + "\n")
    log_file.close()

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 07 13:08:18 2014

@author: Michael Hood
email: michael.allen.hood314@gmail.com
"""
##############################################################################

# The comment writer is a program that will auto generate advisor comments for  
# a midshipmen based on available information such as grades, aptitude 
# rankings, conduct issues, etc.

# Auto generated comments must follow a specific structure.

# The structure consists of three parts:

#   1. An introduction line w/ a general sentiment statement.
#   2. A specific statement about the mid, grades, major, and PFA score.   
#   3. A reccommendation for improvement

###############################################################################




def create_dict(file_name):
    #First, read the csv file and write to rows to a list called stud_data
    import csv
    stud_data = []

    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            stud_data.append(row)

#Next, create a data structure, stud_dict w/ the CSV column headers as the keys, and write the column values to dict 
    stud_dict = {}

    for field in stud_data[0]: stud_dict[field] = []

    for field in range(len(stud_data[0])):
        key = stud_data[0][field]  
        for record in range(1, len(stud_data)):
            stud_dict[key].append(stud_data[record][field])

    return stud_dict



# Get the MIDN name and sex appropriate pronoun, e.g. he, his, she, her
def get_name(stud_dict, index):
    return stud_dict['Last_Name'][index]
    
def get_pronouns(stud_dict, index):
    
    sex = stud_dict['Sex'][index]
    
    if sex == 'M':
        pronouns = ['he', 'his', 'He', 'His']
    else:
        pronouns = ['she', 'her', 'She', 'Her']
    
    return pronouns
    

# Get the aptitude ranking of a mid and at the given index
def get_ranking(stud_dict, index):
    return stud_dict['Ranking'][index]

def get_class_size(stud_dict):
    return len(stud_dict['Last_Name'])

    
    
# Determine the sentiment of the opening line by which third of the rankings the mid # is in
def determine_third(class_size, ranking):
       
    if ranking == 1:
        return
    
    if (ranking <=  class_size / 3) and (ranking != 1):
        third = 1
     
    elif (ranking <=  class_size * 2 / 3) and (ranking > class_size / 3):
        third = 2
    
    elif ranking > class_size * 2 / 3:
        third = 3
        
    return third
    

def get_class(stud_dict, index):
    return stud_dict['Class'][index]

# If MIDN is ranked #1, he gets a special intro
#####################################################################
#####################################################################
def make_intro_line(stud_dict, index):
    
    last_name = get_name(stud_dict, index) 
    ranking = int(get_ranking(stud_dict, index)) 
    class_size = get_class_size(stud_dict) 
    third = determine_third(class_size, ranking)    
    grade_level = get_class(stud_dict, index)
    
    
    if ranking == 1:
        statement = """MIDN %s has finished the semester as the top midshipman in the %s class!""" % (last_name, grade_level)
    
    elif int(ranking) == class_size:
        statement = "MIDN %s has finished the semester at the bottom of the %s class." % (last_name, grade_level)
    
    elif third == 1:
        statement = "MIDN %s has finished the semester in the top third of the %s class." % (last_name, grade_level)
     
    elif third == 2:
        statement = "MIDN %s has finished the semester in the middle third of the %s class." % (last_name, grade_level)
    
    elif third == 3:
        statement = "MIDN %s has finished the semester in the bottom third of the %s class." % (last_name, grade_level)
        
    return statement  
### Remember to address conduct issues and PRB's at a later point.
#############################################################################   
#############################################################################
def get_gpa(stud_dict, index):
    return stud_dict['Term_GPA'][index]


def get_major(stud_dict, index):
    return stud_dict['Major'][index]


def get_prt(stud_dict, index):
    return stud_dict['PRT'][index]
    
def get_conduct(stud_dict, index):
    return stud_dict['PRB'][index]
    
def get_tardy(stud_dict, index):
    return stud_dict['Tardy_To_NROTC_Events'][index]


##################################################################
def prt_comment(df, index):
    
    prt = get_prt(df, index)
    gpa = get_gpa(df, index)
    pronouns = get_pronouns(df, index)

    if (prt == "MED"):
        prt_comment = "and did not earn a score on the PRT for medical reasons."
    
    else:
        prt = int(prt)
        
        if (prt == 100):
            prt_comment = "and earned an impressive maximum score on the PRT."
            
        if (prt >= 90) and (prt < 100):
            prt_comment = "and earned a score of 'OUTSTANDING' on the PRT."
                
        if (prt < 90):
            prt_comment = "earned a score of %d on the PRT." % (prt)
        
        
    
    return prt_comment
    
######################################################

def make_second_line(df, index):
    
    pronouns = get_pronouns(df, index)    
    major = get_major(df, index)    
    if (major == "Engineering") or (major == "Economics"):
        article = "an"
    else:
        article = 'a'
    gpa = float(get_gpa(df, index))
    

    
    if gpa >= 3.50:
        statement = "As %s %s major, %s earned an impressive %s GPA for the semester " % (article, major, pronouns[0], gpa)
    
    elif (gpa < 3.5) and (gpa >= 2.9):
        statement = "As %s %s major, %s earned a %s GPA for the semester " % (article, major, pronouns[0], gpa)
    
    elif (gpa < 2.9) and (gpa >= 2.5):
        statement = "As %s %s major, %s struggled academically with a %s GPA for the semester " % (article, major, pronouns[0], gpa)
    
    elif (gpa < 2.5) and (gpa >= 2.0):
        statement = "As %s %s major, %s struggled academically with a %s GPA and is failing to meet NROTC standards.  %s " % (article, major, pronouns[0], gpa, pronouns[0])
        
    elif gpa < 2.0:
        statement = "As %s %s major, %s struggled academically with a %s GPA and is failing to meet both NROTC and University of Notre Dame standards.  %s " % (article, major, pronouns[0], gpa, pronouns[2])
    
    return statement + prt_comment(df, index)
#############################################################################   
#############################################################################
def make_last_line(df, index):
    
    pronouns = get_pronouns(df, index)    
        
    
    core_statement = "To improve %s ranking, %s should concentrate on improving" % (pronouns[1], pronouns[0])
        
    suggestion_statement = suggestion(df, index)
    professional = professional_comment(df, index)
    if professional_comment != '':
        return core_statement + " " + suggestion_statement + "  " + professional
    else:
        return core_statement + " " + suggestion_statement 


def suggestion(df, index):
    
    pronouns = get_pronouns(df, index)    
       
        # GPA less than 3.5
    if (get_gpa(df, index) < 3.4):
               
        suggestion_gpa = "%s academic performance" % (pronouns[1])
    else:
        suggestion_gpa = ''
    # PRT less than 80%
    
    #if (get_prt(df, index) == 'MED'):
        
    if ( get_prt(df, index) != 'MED'):
        if ( int(get_prt(df, index)) <= 80):            
            suggestion_prt = "%s physical fitness" % (pronouns[1]) 
        else:
            suggestion_prt = ''
    else:
        suggestion_prt = ''
 
    
    if (suggestion_gpa != '') and (suggestion_prt != ''):    
        return suggestion_gpa + " and " + suggestion_prt + "."  
    if (suggestion_gpa != '') and (suggestion_prt == ''):
        return suggestion_gpa + " and " + "%s involvement in the Battalion while finding ways to assume positions of greater responsibility." % (pronouns[1])
    if (suggestion_gpa == '') and (suggestion_prt != ''):
        return suggestion_prt + " and " + "%s involvement in the Battalion while finding ways to assume positions of greater responsibility." % (pronouns[1])    
    if  (suggestion_gpa == '') and (suggestion_prt == ''):
        return "%s involvement in the Battalion while finding ways to assume positions of greater responsibility." % (pronouns[1])
        
        
def professional_comment(df, index):

    pronouns = get_pronouns(df, index)    
    
    if ( get_conduct(df, index) == 'Y') and ( get_tardy(df, index) == 'Y'):
        return "%s needs to ensure that %s complies with NROTC regulations and attends all military obligations.  " % (pronouns[2], pronouns[0])
                 
    elif ( get_conduct(df, index) == 'Y') and ( get_tardy(df, index) == 'N'):
        return "%s needs to ensure that %s complies with NROTC regulations.  " % (pronouns[2], pronouns[0])
    elif ( get_conduct(df, index) == 'N') and ( get_tardy(df, index) == 'Y'):    
        return "%s has had problems with multiple unauthorized absences from military obligations.  " % (pronouns[2])
    else:
        return ""
        
#####################################################################
        
######################################################################
def complete_comment(stud_dict, index):
    
    first_line = make_intro_line(stud_dict, index)
    second_line = make_second_line(stud_dict, index)
    last_line = make_last_line(stud_dict, index)
    class_size = get_class_size(stud_dict)
    
    pronouns = get_pronouns(stud_dict, index)    
    ranking = get_ranking(stud_dict, index)
    ranking_comment = "As a result of %s performance, %s is ranked %d of %d in %s class." % (pronouns[1], pronouns[0], int(ranking), class_size, pronouns[1])    
    
    return first_line + "  " + second_line + "  " + last_line + ranking_comment    
    

###############################################

    
    
    
    
    
    
    
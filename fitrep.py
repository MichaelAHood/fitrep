# -*- coding: utf-8 -*-
"""
Created on Thu Aug 07 13:08:18 2014

@author: mhood2
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


# Part 1: The introduction line

#top_three_adjectives = ['top-notch', ' ]

# if #1
# "MIDN X has distinguished himself as the top-performer/head of the class
# during the last semester.



# Get the MIDN name and sex appropraite pronoun, e.g. he, his, she, her
def get_name(df, index):
    return df.at[index, 'Last_Name']
    
def get_pronouns(df, index):
    
    sex = df.at[index, 'Sex']
    
    if sex == 'M':
        pronouns = ['he', 'his', 'He', 'His']
    else:
        pronouns = ['she', 'her', 'She', 'Her']
    
    return pronouns
    

# Get the aptitude ranking of a mid and at the given index
def get_ranking(df, index): 
    return df.at[index, 'Ranking']

def get_class_size(df):
    return df.Ranking.count()
    
    
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
    

def get_class(df, index):
    return df.at[index, 'Class']

# If MIDN is ranked #1, he gets a special intro
#####################################################################
#####################################################################
def make_intro_line(df, index):
    
    last_name = get_name(df, index) 
    ranking = get_ranking(df, index) 
    class_size = get_class_size(df) 
    third = determine_third(class_size, ranking)    
    grade_level = get_class(df, index)
    
    
    if ranking == 1:
        statement = """MIDN %s has finished the semester as the top midshipman in the %s class!""" % (last_name, grade_level)
    
    elif third == 1:
        statement = "MIDN %s has finished the semester in the top third of the %s class." % (last_name, grade_level)
     
    elif third == 2:
        statement = "MIDN %s has finished the semester in the middle third of the %s class." % (last_name, grade_level)
    
    elif third == 3:
        statement = "MIDN %s has finished the semester in the bottom third of the %s class." % (last_name, grade_level)
        
    elif ranking == len(df) - 1:
        statement = "MIDN %s has finished the semester at the bottom of the %s class." % (last_name, grade_level)
        return statement
     
    return statement  
### Remember to address conduct issues and PRB's at a later point.
#############################################################################   
#############################################################################
def get_gpa(df, index):
    return df.at[index, 'Term_GPA']


def get_major(df, index):
    return df.at[index, 'Major']


def get_prt(df, index):
    return df.at[index, 'PRT']
    
def get_conduct(df, index):
    return df.at[index, 'PRB']
    
def get_tardy(df, index):
    return df.at[index, 'Tardy_To_NROTC_Events']


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
    gpa = get_gpa(df, index)
    

    
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
def complete_comment(df, index):
    
    first_line = make_intro_line(df, index)
    second_line = make_second_line(df, index)
    last_line = make_last_line(df, index)
    
    pronouns = get_pronouns(df, index)    
    ranking = get_ranking(df, index)
    ranking_comment = "As a result of %s performance, %s is ranked %d of %d in %s class." % (pronouns[1], pronouns[0], ranking, len(df), pronouns[1])    
    
    return first_line + "  " + second_line + "  " + last_line + ranking_comment    
    

###############################################

    
    
    
    
    
    
    
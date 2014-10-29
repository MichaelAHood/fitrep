# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 08:33:16 2014

@author: mhood2
"""

import fitrep
import csv

file_name = raw_input("What is the name of the file with the student data in it? \nNote: This file must end in '.csv'.  Ex: student_data.csv : " )

stud_dict = fitrep.create_dict(file_name)

comments = []
destination_file_name = raw_input("What is the name of the file that you want the comments written to? \nNote: Your filename must end in '.csv'.  Ex: my_comments.csv :  " )

number_students = len(stud_dict['Last_Name'])

#try:
for student in range(number_students):
    comments.append([fitrep.complete_comment(stud_dict, student)])
    
dest_file = open(destination_file_name, 'wb')
csv_writer = csv.writer(dest_file)
for i in range(0, number_students):
    csv_writer.writerow(comments[i])

dest_file.close()

print "Comments successfully written to %s." % (destination_file_name) 

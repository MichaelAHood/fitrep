# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 08:33:16 2014

@author: mhood2
"""
import pandas
import fitrep
import csv

df = pandas.read_csv('4c_data.csv')

comments = [["Comments"]]
destination_file_name = raw_input("What is the name of the file that you want the comments written to? \nNote: Your filename must end in '.csv'.  Ex: my_comments.csv :  " )

number_students = len(df)

try:
    for student in range(number_students):
        comments.append([fitrep.complete_comment(df, student)])
    
    with open(destination_file_name, 'wb') as destination_file:
        csv_writer = csv.writer(destination_file)
        for i in range(0, number_students):
            csv_writer.writerow(comments[i])

finally:
    close(destination_file)

print "Comments successfully written to %s." % (destination_file_name) 

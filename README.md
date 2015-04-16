fitrep
======

A collection of scripts to automate error correction and comment generation for my student FITREPs.

You can find a post I wrote discussing the development of this module at: http://michaelahood.com/

I've never written documentation for anything before, so this is a work in progress.  Feel free to email if you have any questions or comments: michael.allen.hood314@gmail.com

1.  formatter.py:
This module will perform simple formatting fixes on the collateral duties section (Block 29).  It will capitalize the appropriate words and ensure that there are commas in the right spots for the majority of use cases, I have encountered as a teacher.

2.  fitrep.py:
This module contains the procedures that write the individual sentences for the comment section of a students FITREP.

3.  writer.py:
Run this module in the same working directory as the data.csv file and follow the on-screen prompt.  It's pretty self-explanatory and the script will create a new .CSV file, whose name you specify, with the comments in it.

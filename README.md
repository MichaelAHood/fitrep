fitrep
======

A collection of scripts to automate error correction and comment generation for my student FITREPs.

You can find a post I wrote discussing the development of this module at: https://medium.com/@michaelahood

I've never written documentation for anything before, so this is a work in progress.  Feel free to email if you have any questions or comments: michael.allen.hood314@gmail.com

1.  formatter.py:
This module will perform simple formatting fixes on the collateral duties section (Block 29).  It will capitalize the appropraite words and ensure that there are commas in the right spots (hopefully).

2.  fitrep.py:
This module contains a bunch of procedures that write the individiaul sentences for the comment section of a students FITREP.  The procedure complete_comment() is the most useful, if you just want to use the thing and don't really care how it works.


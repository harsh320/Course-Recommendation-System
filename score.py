# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:47:48 2019

@author: Harsh bansal
"""
import re
import string
from nltk.corpus import stopwords
from fuzzywuzzy import fuzz
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import pandas as pd
import csv
from itertools import zip_longest

sites={"Coursera":1,"EDX":2,"Youtube":3,"LyndaCourses":6,"MIT":5,"FutureLearnCourses":7,"Udemy":4}

finalname=[]
finaldetail=[]
finalsite=[]
finallink=[]
finalCoursename=[]
finalcoursedetail=[]
finalcoursecode=[]
finalscoreCourse=[]
finalsiteScore=[]

d = [finalname,finaldetail,finalsite,finallink,finalcoursecode,finalcoursedetail,finalCoursename,finalscoreCourse,finalsiteScore]
export_data = zip_longest(*d, fillvalue = '')


a=""
syllabus=pd.read_csv("numbers1final.csv") 
for index,item in syllabus.iterrows():
    site=str(item["Site"])
    if a != site :
        count = 1
        a = site
    finalscoreCourse.append(count)
    count += 1
    finalsiteScore.append(sites[site])
    finalname.append(item["Name"])
    finaldetail.append(item["Detail"])
    finalsite.append(item["Site"])
    finallink.append(item["Link"])
    finalcoursecode.append(item["Code"])
    finalCoursename.append(item["Cname"])
    finalcoursedetail.append(item["Cdetail"])


with open('csedatabase.csv', 'w', encoding="utf-8", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Name","Detail","Site","Link","Code","Cdetail","Cname","CourseScore","SiteScore"))
      wr.writerows(export_data)
myfile.close()

    
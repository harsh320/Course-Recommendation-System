# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:53:55 2019

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

finalname=[]
finaldetail=[]
finalsite=[]
finallink=[]
finalCoursename=[]
finalcoursedetail=[]
finalcoursecode=[]
finalwordsmatch=[]
finalratio=[]
d = [finalname,finaldetail,finalsite,finallink,finalcoursecode,finalcoursedetail,finalCoursename,finalwordsmatch,finalratio]
export_data = zip_longest(*d, fillvalue = '')




def normal(input_str):
    input_str = input_str.lower()
    
    bad_chars = [';', ':', '!', '*','-',',',"''",'``','#'] 
    for i in bad_chars : 
        input_str = input_str.replace(i,' ')
    result = re.sub(r'\d+','', input_str)
    result = result.translate(str.maketrans("","", string.punctuation))
    result = result.strip()
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(result)
    result = [i for i in tokens if not i in stop_words]
    output = ""
    for i in result:
        output += i + " "
   
    return output

def normal1(output):
    stemmer= PorterStemmer()
    input_str=word_tokenize(output)
    output = ""
    for word in input_str:
        output += stemmer.stem(word) + " "
    
    lemmatizer=WordNetLemmatizer()
    input_str=word_tokenize(output)
    output = ""
    for word in input_str:
        output += lemmatizer.lemmatize(word) + " "
    
    return output
    
syllabus=pd.read_csv("csedatabase.csv") 
for index,item in syllabus.iterrows():
    name=str(item["Name"])
    details=str(item["Detail"])
    if(name in (None, "", "nan") or details in (None, "","nan")):
        continue
    if(name[0] == ','):
        continue
    
    if(details[0] == ','):
        continue
        
    a = normal(str(item["Detail"]))
    b = normal(str(item["Cdetail"]))
    
    h=""
    words=[]
    words1=[] 
    tokensyll = word_tokenize(a)
    for i in tokensyll :
        words.append(i)
    words=set(words)
    tokenscrape = word_tokenize(b)
    
    for i in tokenscrape :
        if i in words :
            words1.append(str(i))
    words1=set(words1)
    for i in words1:
        h += i + " "
    a=normal1(a)
    b=normal1(b)
    words.clear()
    words1.clear()
    Token_W_Ratio = fuzz.WRatio(a,b)
    Token_set_Ratio=fuzz.token_set_ratio(a,b)
    ratio=item["SiteScore"]
    ratio1=item["CourseScore"]
    ratio=((8-int(ratio))/7)*100
    ratio1=((26-int(ratio1))/25)*100
    finalratio123=Token_W_Ratio*0.3+Token_set_Ratio*0.4+ratio*0.1+ratio1*0.2
    finalratio.append(Token_set_Ratio)
    finalwordsmatch.append(h)
    finalname.append(item["Name"])
    finaldetail.append(item["Detail"])
    finalsite.append(item["Site"])
    finallink.append(item["Link"])
    finalcoursecode.append(item["Code"])
    finalCoursename.append(item["Cname"])
    finalcoursedetail.append(item["Cdetail"])



with open('finalfinalfinalfinal1.csv', 'w', encoding="utf-8", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Name","Detail","Site","Link","Code","Cdetail","Cname","WordsMatch","Ratio"))
      wr.writerows(export_data)
myfile.close()
    
        




# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:08:51 2019

@author: Harsh
"""

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import pandas as pd
from fuzzywuzzy import fuzz
from autocorrect import spell 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from nltk.stem import PorterStemmer
import time as timewait
from nltk.tokenize import sent_tokenize, word_tokenize
from selenium.common.exceptions import NoSuchElementException

from threading import Thread

    
#coursera(1)
#udemy()
#edxCourses()
#futureLearnCourses()
#youtubeCourses()
#alison()
name=[]
rating=[]
difficulty=[]
match=[]
enrollment_number=[]
link=[]
detail=[]
detail_score=[]
view=[]
time=[]       
instructor=[]
norating=[]
noreviews=[]
site=[]



mitname=[]
mitdetail=[]
mitsite=[]
mitlink=[]

lyndaname=[]
lyndadetail=[]
lyndasite=[]
lyndalink=[]

edxname=[]
edxdetail=[]
edxsite=[]
edxlink=[]


futurename=[]
futuredetail=[]
futuresite=[]
futurelink=[]

youtubename=[]
youtubedetail=[]
youtubesite=[]
youtubelink=[]


courseraname=[]
courseradetail=[]
courserasite=[]
courseralink=[]

udemyname=[]
udemydetail=[]
udemysite=[]
udemylink=[]


finalname=[]
finaldetail=[]
finalsite=[]
finallink=[]
finalCoursename=[]
finalcoursedetail=[]
finalcoursecode=[]






d = [finalname,finaldetail,finalsite,finallink,finalcoursecode,finalcoursedetail,finalCoursename]

export_data = zip_longest(*d, fillvalue = '')
def mitcourses(query):
    driver = webdriver.Firefox(executable_path=r'C:\\Users\\Harsh\\Desktop\\geckodriver.exe')
    timewait.sleep(1)
    links_href = []
    links=[]
    driver.get("https://ocw.mit.edu/search/ocwsearch.htm?q="+query)
    timewait.sleep(2)
    try :
        driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[5]/div/div[3]/div/div/div/div/div[2]/div/div/div[2]').click()
    except NoSuchElementException:
        None
    try :
        title=driver.find_elements_by_xpath('//div[@class="gs-title"]/a')
    except NoSuchElementException:
        None
    for i in title :
        links.append(i.get_attribute('data-ctorig'))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    timewait.sleep(2)
    for i in range(2,2):
        driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[5]/div/div[3]/div/div/div/div/div[5]/div[2]/div[2]/div/div[2]/div/div['+str(i)+']').click()
        timewait.sleep(2)
        try:
            title=driver.find_elements_by_xpath('//div[@class="gs-title"]/a')
        except NoSuchElementException:
            None
        for i in title :
            links.append(i.get_attribute('data-ctorig'))
    
    
    for i in links:
        temp = str(i)
        temp = temp.rsplit('/')
        if(temp[0][0]!='N' and temp[2][0]=='o' and temp[3][0]=='c' ):
            links_href.append(temp)
    
    url_lists = []
    for i in links_href:
        temp = str(i[0])+ "//" + str(i[2]) + "/" + str(i[3]) + "/" + str(i[4]) + "/" + str(i[5])
        url_lists.append(temp)
    print(len(url_lists))
    courses = {}
    for i in url_lists:
        driver.get(i)
        try:
            x = driver.find_element_by_xpath('//h1[@class="title"]')
        except NoSuchElementException:
            continue
        courses[x.text]=i
    
    for h in courses:
        
        url_course = str(courses[h] + "/calendar/" )
        driver.get(str(courses[h]))
        #instructor = driver.find_element_by_xpath('//p[@class="ins"]')
        #print(instructor.text)
        #startdate = driver.find_element_by_xpath('//p[@itemprop="startDate"]')
        #print(startdate.text)
        driver.get(url_course)
        driver.implicitly_wait(10)
        d=""
        description = driver.find_elements_by_xpath('//div[@class="maintabletemplate"]/table/tbody/tr/td[2]')
        for i in description :
            d += i.text +  " "
        if d == "" :
             url_course = str(courses[h] + "/syllabus/" )
             driver.get(url_course)
             driver.implicitly_wait(10)
             description = driver.find_elements_by_xpath('//main[@id="course_inner_section"]')
                    
             for j in description:
                cd = str(j.text)
                cd = cd.splitlines()
                x = False
                for k in range(len(cd)):
                    if(cd[k] == "Calendar"):
                        x=True
                    if(x == True):
                        d = d + str(cd[k])
        if d == "" :
            url_course = str(courses[h] + "/lecture-notes/" )
            driver.get(url_course)
            driver.implicitly_wait(10)
            description = driver.find_elements_by_xpath('//div[@class="maintabletemplate"]/table/tbody/tr/td[2]/a')
            for i in description :
                d += i.text +  " "
        if d != "" :
            print(d)
            mitdetail.append(d)
            mitlink.append(str(courses[h]))
            mitname.append(h)
            mitsite.append("MIT")
    driver.close()
                




def lyndaCourses(topic):

    driver = webdriver.Firefox(executable_path=r'C:\\Users\\Harsh\\Desktop\\geckodriver.exe')
    link1="https://www.linkedin.com/learning/search?entityType=COURSE&keywords="
    topic = topic.split()
    for t in topic:
        link1=link1+t+"%20"
    link1 = link1[:-3]
    driver.get(link1)
    driver.implicitly_wait(2)
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    driver.implicitly_wait(2)
    timewait.sleep(5)
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    timewait.sleep(5)
    driver.execute_script("window.scrollTo(0, 1080)")
    timewait.sleep(5)
    try :
	    links = driver.find_elements_by_xpath('//a[@data-control-name="search_result_card_title"]')
    except NoSuchElementException :
	    pass
    for i in range(len(links)):
        temp = links[i].get_attribute("href")
        if temp is None:
            pass
        else:
            links[i]= temp

    for link1 in links:
        s1=""
        driver.get(link1)
        try:
            name1 = driver.find_element_by_xpath('//h1[@class="content__header-headline"]').text
        except NoSuchElementException:
            name1= ""
        lyndaname.append(name1)
        lyndasite.append("LyndaCourses")
        lyndalink.append(link1)

        try:
            syll = driver.find_elements_by_xpath('//div[@class="toc__sublist__item__content__title"]')
            for s in syll:
                s1 += s.text + " "
        except NoSuchElementException:
            s1=""
        lyndadetail.append(s1)
    driver.close()





def edxCourses(query):
    # course = ""
    # input("Enter course name : ",course)
    query=query.split()
    a=""
    for i in query :
       a += i + "+"
    driver = webdriver.Firefox(executable_path=r'C:\\Users\\Harsh\\Desktop\\geckodriver.exe')
    driver.maximize_window()
    driver.get("https://www.edx.org/")

    def check_exists_by_xpath(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    #open sign in page
    try:
        driver.find_element_by_link_text("Sign In").click()
    except NoSuchElementException:
        driver.close()
        return

    #enter username
    driver.implicitly_wait(50)

    try:
        username = driver.find_element_by_xpath('//*[@id="login-email"]')
        username.clear()
        username.send_keys("blogit52@gmail.com")
    except NoSuchElementException:
        driver.close()
        return
    try:
        password = driver.find_element_by_xpath('//*[@id="login-password"]')
        password.clear()
        password.send_keys("lavi@8875")
    except NoSuchElementException:
        driver.close()
        return

    #signing in
    try:
        driver.find_element_by_xpath('//*[@id="login"]/button').click()
    except NoSuchElementException:
        driver.close()
        return
    try:
        driver.find_element_by_xpath('/html/body/div[2]/header/div[2]/div[2]/div[1]/div[3]/a').click()
    except NoSuchElementException:
        driver.close()
        return
    #search for particular topic
    try:
        driver.get("https://www.edx.org/course?search_query="+a)
    except NoSuchElementException:
        driver.close()
        return
    timewait.sleep(3)
    driver.implicitly_wait(2)

    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(2)
        timewait.sleep(5)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        timewait.sleep(5)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        timewait.sleep(5)
    except Exception:
        pass

    try:
        courses = driver.find_elements_by_xpath('//a[@class="course-link"]')
    except NoSuchElementException:
        pass
    num_pages = len(courses)
    print(num_pages)
    links=[]
    for i in  range(num_pages):
        try:
            links.append(courses[i].get_attribute("href"))
        except Exception:
            pass


    count=0
    for i in links:
        if count==25:
            break
        driver.get(str(i))
        edxlink.append(i)
        edxsite.append("EDX")

        try:
                name10=driver.find_element_by_xpath('//h1[@class="course-intro-heading"]/span').text

                timewait.sleep(2)
                try:
                    if check_exists_by_xpath('//div[@class="course-enroll-actions"]/a'):
                        driver.find_element_by_xpath('//div[@class="course-enroll-actions"]/a').click()
                        driver.find_element_by_xpath('//input[@name="audit_mode"]').click()
                    else :
                        driver.get(driver.find_element_by_xpath('//div[@class="course-enroll-actions"]/a').get_attribute("href"))
                    expand=driver.find_elements_by_xpath('//button[@id="expand-collapse-outline-all-button"]')
                    for i in expand :
                        i.click()
                    syllabus_ = driver.find_elements_by_xpath('//div[@class="vertical-details"]/div')
                    q=''
                    for s in syllabus_:
                        q += s.text + " "
                except Exception:
                    q=""

                edxdetail.append(q)
                edxname.append(name10)

        except:
            try:
                try:
                    name10=driver.find_element_by_xpath('//h1[@class="course-intro-heading mb-2"]').text
                except Exception:
                    name10=""
                """a=driver.find_element_by_xpath('//ul[@class="list-group list-group-flush w-100"]/li[1]/div[2]/span').text
                a=a.split()
                b=int(a[0])
                b=b*7*24*60
                time.append(b)
                print(b)
    
                university = driver.find_element_by_xpath('//ul[@class="list-group list-group-flush w-100"]/li[4]/div[2]/a').text
                difficulty.append(driver.find_element_by_xpath('//ul[@class="list-group list-group-flush w-100"]/li[6]/div[2]').text)
                language = driver.find_element_by_xpath('//ul[@class="list-group list-group-flush w-100"]/li[7]/div[2]').text
                #instructor = driver.find_element_by_xpath('//div[@class="d-flex flex-column instructor-details"/a]').text"""
                try:
                    if check_exists_by_xpath('//div[@class="enroll-cta"]/button'):
                        driver.find_element_by_xpath('//div[@class="enroll-cta"]/button').click()
                        driver.find_element_by_xpath('//input[@name="audit_mode"]').click()
                    else :
                        driver.get(driver.find_element_by_xpath('//div[@class="enroll-cta"]/a').get_attribute("href"))
                    expand=driver.find_elements_by_xpath('//button[@id="expand-collapse-outline-all-button"]')
                    for i in expand :
                        i.click()
                    syllabus_ = driver.find_elements_by_xpath('//div[@class="vertical-details"]/div')
                    q=''
                    for s in syllabus_:
                        q += s.text + " "
                except Exception:
                    q=""
                print(q)
                edxdetail.append(q)
                edxname.append(name10)
            except:
                edxname.append("")
                edxdetail.append("")
            
        count += 1
                

    driver.close()
    














def futureLearnCourses(query):
    #add topic in this search url
    query=query.split()
    a=""
    for i in query :
       a += i + "+" 
    driver = webdriver.Firefox(executable_path=r'C:\\Users\\Harsh\\Desktop\\geckodriver.exe')
    driver.get("https://www.futurelearn.com/search?q="+a)
    #name,duration,university,topics_covered,instructor,link
    name1=[]
    link1=[]
    detail1=[]
    course_links = driver.find_elements_by_xpath('//a[@class="js-ahoy-track"]')
    print(len(course_links))
    for i in range(len(course_links)):
        q=course_links[i].text
        r=course_links[i].get_attribute("href")
        if r != None:       
            link1.append(course_links[i].get_attribute("href"))
            if q != None:
                name1.append(course_links[i].text)
            else :
                name1.append(" ")
        
    count=0
    
    detail=[]
    for links in link1:
        if count == 20:
            break
        driver.get(links)
        
        topics_covered=' '
        contents = driver.find_elements_by_xpath('//*[@id="section-topics"]/div/ul/li')
        for t in contents:
            topics_covered += str(t.text) + " "
        futuredetail.append(topics_covered)
        futurelink.append(links)
        futurename.append(name1[count])
        futuresite.append("FutureLearnCourses")
        weeks = driver.find_elements_by_xpath('//span[@class="m-key-info__content"]')
        a=[]
        for i in weeks:
            if len(i.text.split())==2 and i.text.split()[1]=="weeks":
                a.append(i.text)
            if len(i.text.split())==2 and i.text.split()[1]=="hours":
                a.append(i.text)
        if len(a)!=2:
            time.append(" ")
        else:
            no_of_weeks = int(weeks[0].text.split()[0])
            hrs_per_week = int(weeks[1].text.split()[0])
            duration=no_of_weeks*hrs_per_week*60
            time.append(duration)
        #university= driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/div[2]/div[1]/div[1]/a/img').get_attribute("title")
        instruct=driver.find_elements_by_xpath('//h3[@class="m-info-block__title"]/a')
        inst=''
        for ins in instruct:
            inst += str(ins.text) + " "
        count += 1
        #detail.append([topics_covered,links,name1[count-1],inst])
    #print(detail)      
    driver.close()
        



def youtubeCourses(query1,query2):#problem in scraping duration
    # course = ""
    # input("Enter course name : ",course)
    q=""
    w=""
    query1 = query1.split()
    query2 = query2.split()
    for i in query1 :
        q += i + "+"
    for i in query2 :
        w += i + "+"
    driver = webdriver.Firefox(executable_path=r'C:\\Users\\Harsh\\Desktop\\geckodriver.exe')
    driver.get("https://www.youtube.com/results?search_query="+q+"in "+w+"&sp=EgIQAw%253D%253D")
    
    
    
    SCROLL_PAUSE_TIME = 1

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        # Wait to load page
        timewait.sleep(SCROLL_PAUSE_TIME)
    
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    
    
    
    #timewait.sleep(15)

    def check_exists_by_xpath(xpath):
        try:
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    playlist_links = driver.find_elements_by_xpath('//ytd-playlist-renderer[@class="style-scope ytd-item-section-renderer"]/div/yt-formatted-string/a')
    i=0
    for links in playlist_links:
        q=links.get_attribute("href")
        if q != None :
            playlist_links[i] = links.get_attribute("href")
            i=i+1
            
    print(len(playlist_links))
    print(playlist_links)


    #name,views,duration,noOfVideos,topics_covered,channel
    for links in playlist_links:
        syllabus=' '
        topics = driver.find_elements_by_xpath('//*[@id="video-title"]')
        for topic in topics:
            syllabus += str(topic.text) + " "
            if syllabus == ' ' :
                continue
        
        youtubedetail.append(syllabus)
        youtubelink.append(links)
        youtubesite.append("Youtube")
        driver.get(links)
        name1=" "
        try:
            name1 = driver.find_element_by_xpath('//yt-formatted-string[@class="style-scope ytd-playlist-sidebar-primary-info-renderer"]/a').text
        except NoSuchElementException:
            name1 = " "
        
        youtubename.append(name1)
        no_of_videos = driver.find_element_by_xpath('//div[@id="stats"]/yt-formatted-string[1]').text
        no_of_videos= int(no_of_videos.split()[0])
        views = driver.find_element_by_xpath('//div[@id="stats"]/yt-formatted-string[2]').text
        if views.split()[1]=="views":
            a=(views.split()[0]).split(',')
            b=''
            for i in a:
                b=b+i
            view.append(b)
        else:
            view.append(" ")
        times = driver.find_elements_by_xpath('//span[@class="style-scope ytd-thumbnail-overlay-time-status-renderer"]')
        count=0
        b=1
        if len(times)==1:
            for time1 in times:
                print(time1.text)
                a=time1.text.split(':')
                if len(a)==3:
                 b=int(a[1])+int(a[0])*60   
                elif len(a)==2:
                 b=int(a[0])
                else:
                 b=1
                print(no_of_videos)
                print(b)
                break
        else :
            for time1 in times:
                        if count==1:
                            print(time1.text)
                            a=time1.text.split(':')
                            if len(a)==3:
                             b=int(a[1])+int(a[0])*60   
                            elif len(a)==2:
                             b=int(a[0])
                            else:
                             b=1
                            print(no_of_videos)
                            print(b)
                            break
                        count += 1
        
                    
                
            
        time.append(b*no_of_videos)
    driver.close()
        
        #print(times)
        #duration=0
        # for t in times:
        #     s = t.text
        #     print(s)
        #     duration = duration + ((int)(s.split(":")[0]) + (int)(s.split(":")[1])/100)








def alison():
    driver = webdriver.Firefox(executable_path=r'C:\\Users\\Harsh\\Desktop\\geckodriver.exe')
    driver.get("https://alison.com/")
    driver.find_element_by_xpath('//span[@class="text"]').click()
    driver.find_element_by_xpath('//input[@placeholder="Email address"]').send_keys("ashutoshsah2000@hotmail.com")
    driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys("minorproject")
    driver.find_element_by_xpath('//input[@type="submit"]').click()
    query = "machine learning"
    j=1
    url = "https://alison.com/courses?query=" + query + "&page=" + str(j)
    driver.get(url)
    driver.implicitly_wait(40)
    timewait.sleep(10)
    no_courses =int(driver.find_element_by_xpath('//span[@id="num-results"]').text)
    print(no_courses)
    course ={} 
    
    c=1
    for j in range(1,2): # badha liyo khud se  
        c =c+1
        driver = webdriver.Firefox(executable_path=r'C:\\Users\\Harsh\\Desktop\\geckodriver.exe')
        url = "https://alison.com/courses?query=" + query + "&page=" + str(j)
        driver.get(url)
        driver.implicitly_wait(30)
        co = driver.find_elements_by_xpath('//div[@class="course-block course-tile"]')
        for i in co:
            print(i.get_attribute('data-more'))
            course[i]=(i.get_attribute('data-more'))
        count = 0 
    for i in range(len(course)):
        if count == 2 :
            break
        count += 1
        driver.get(course[i])
        driver.implicitly_wait(40)
        course_name  = driver.find_element_by_xpath('//div[@class="course-brief--title"]')
        
        course_name = course_name.find_element_by_xpath('//h1')
        name.append(course_name.text)
        site.append("Alison")
        course_detail1  = driver.find_element_by_xpath('//div[@class="course-banner"]')
        
        no_enrolled = course_detail1.find_element_by_xpath('//h4')
        enrollment_number.append(no_enrolled.text)
        duration=driver.find_element_by_xpath('//div[@class="course-brief--col2 match-height"]/ul[1]/li[1]/div[2]/span')
        time.append(duration.text)
        rate=driver.find_element_by_xpath('//div[@class="course-brief-container"]/div[1]/ul/li[2]/div[2]/h4')
        print(rate.text)
        rating.append(rate.text)
        h=''
        link.append(course[i])
        driver.get(course[i]+"/content")
        outlines = driver.find_elements_by_xpath('//div[@class="new-modules--topics"]/a/span/h4')
        
        driver.implicitly_wait(4)
        for i in outlines:
            print(i.text)
            h += i.text +" "
        for i in range(3,10):
            q=driver.find_elements_by_xpath('/html/body/div[5]/div/div/div[3]/div/div[2]/div[1]/ul/li['+str(i)+']/a')
            for w in q:
                w.click()
                timewait.sleep(1)
                outlines = driver.find_elements_by_xpath('//div[@class="new-modules--topics"]/a/span/h4')
                
                timewait.sleep(2)
                for i in outlines:
                    print(i.text)
                    h += i.text +" "
        detail.append(h)
    driver.close()







def coursera(query,max_pages):
    driver = webdriver.Firefox(executable_path=r'C:\\Users\\Harsh\\Desktop\\geckodriver.exe')
    driver1 = webdriver.Firefox(executable_path=r'C:\\Users\\Harsh\\Desktop\\geckodriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(50)
    driver1.maximize_window()
    driver1.implicitly_wait(50)
    q=""
    type1=[]
    query = query.split()
    for i in query :
        q += i + "%20"
    
    #val = input("Enter your value: ")
    driver.get("https://www.coursera.org/search?query="+q+"&indices%5Bprod_all_products%5D%5Bpage%5D="+str(max_pages)+"&indices%5Bprod_all_products%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Bprod_all_products%5D%5Bconfigure%5D%5BhitsPerPage%5D=10&configure%5BclickAnalytics%5D=true")
    driver.implicitly_wait(5)
    timewait.sleep(5)
    for links in driver.find_elements_by_xpath("//div[@class='card-info vertical-box']/div[1]"):
        type1.append(links.text)
    count=0
    for links in driver.find_elements_by_xpath("//h2[@class='color-primary-text card-title headline-1-text']"):
            if type1[count]!="COURSE":
                count+=1
                continue
            count+=1
            #courseraname.append(links.text)
            #courserasite.append("Coursera")
            print(links.text)
    count=0
    for links1 in  driver.find_elements_by_xpath("//span[@class='ratings-text']"):
            if type1[count]!="COURSE":
                count+=1
                continue
            count+=1
            rating.append(links1.text)
    count=0
    for links2 in driver.find_elements_by_xpath("//span[@class='difficulty']"):
        if type1[count]!="COURSE":
            count+=1
            continue
        count+=1
        difficulty.append(links2.text)
    count=0
    for links3 in driver.find_elements_by_xpath("//span[@class='enrollment-number']"):
        if type1[count]!="COURSE":
            count+=1
            continue
        count+=1
        enrollment_number.append(links3.text)    
    print(type1)
    count=0
    for links4 in driver.find_elements_by_xpath("//a[@class='rc-DesktopSearchCard anchor-wrapper']"):
        if type1[count]!="COURSE":
            count+=1
            continue
        count+=1
        url=str(links4.get_attribute('href'))
        print(url)
        driver1.get(url)
        timewait.sleep(3)
        '''for links5 in driver1.find_elements_by_xpath("//div[@class='AboutCourse']/div[2]/div[1]/div[1]/div/div[1]/div[2]/p"):
            detail.append(links5.text)
            detail_score.append(fuzz.token_set_ratio(links5.text,"Bussiness"))
            print(links5.text)'''
        
        for links6 in driver1.find_elements_by_xpath("//div[@class='rc-ProductMetrics']/div[1]/span[1]/span[1]"):
                view.append(str(links6.text))
                print(links6.text)
        
        for links7 in driver1.find_elements_by_xpath("//span[@itemprop='reviewCount']"):
            time.append(links7.text)
            print(links7.text)
        
        for links8 in  driver1.find_elements_by_xpath("//div[@class='Instructors']/div[2]/div/div/div/h3/a"):
            s=""
            if links8.text!="" :
                s=s+links8.text+","
            print(s)
        instructor.append(s)
            
        for links10 in driver1.find_elements_by_xpath("//div[@class='CourseReviewOverview']/div/div[1]/div/div[1]/div/span"):
                norating.append(links10.text)
            
        courseralink.append(links4.get_attribute('href')) 
        courserasite.append("Coursera")
        q123=""
        try:
            q123=driver.find_element_by_xpath("//h1[@class='H2_1pmnvep-o_O-weightNormal_s9jwp5-o_O-fontHeadline_1uu0gyz max-text-width-xl m-b-1s']")
        except:
            q123=" "
        courseraname.append(q123)
       
        final=''
        ex=driver1.find_elements_by_css_selector('button.m-t-1 > span:nth-child(1)')
        for items in ex:
            items.click()
        timewait.sleep(2)
        for j in range(1,8):
            for i in range(1,5):
                #expandable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ud-component--clp--curriculum > div:nth-child("+str(i)+") > a:nth-child(1)")))
                expandables = driver1.find_elements_by_css_selector('.Syllabus > div:nth-child(2) > div:nth-child('+str(j)+') > div:nth-child(2) > div:nth-child('+str(i)+') > div:nth-child(4) > button:nth-child(2)')
                
                for item in expandables:
                    try:
                        item.click() 
                    except :
                        timewait.sleep(2)
                        print("hello")
                    driver1.implicitly_wait(1)
                    timewait.sleep(1)
                    
                expandables = driver1.find_elements_by_css_selector('div.transitionContainer_xmmnjl:nth-child(1) > div:nth-child(1) > div:nth-child('+str(j)+') > div:nth-child(2) > div:nth-child('+str(i)+') > div:nth-child(4) > button:nth-child(2) > span:nth-child(1)')
               
                for item in expandables:
                     try:
                        item.click() 
                     except :
                        timewait.sleep(2)
                        print("bye")
                     driver1.implicitly_wait(1) 
                     timewait.sleep(1)
        l = driver1.find_elements_by_xpath("//div[@class='ItemGroupView border-top p-t-2']/div[1]/div")
        for j in l:
            final += j.text + " "
        courseradetail.append(final)
    



def udemy(query,page):
    q=""
    query = query.split()
    for i in query :
        q += i + "%20"
    
    link1=[]
    driver = webdriver.Firefox(executable_path=r'C:\\Users\\Harsh\\Desktop\\geckodriver.exe')
    driver.minimize_window();
    driver.get("https://www.udemy.com/courses/search/?q="+q+"&src=sac&kw=mac&p="+str(page))
    
    SCROLL_PAUSE_TIME = 1

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
        # Wait to load page
        timewait.sleep(SCROLL_PAUSE_TIME)
    
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    """a = driver.find_elements_by_xpath("//div[@class='list-view-course-card--title--2pfA0']/h4")
    for i in a:
        udemyname.append(i.text)
        udemysite.append("Udemy")"""
    a = driver.find_elements_by_xpath("//div[@class='list-view-course-card--rating--za-yU']/span[1]")
    for i in a:
        rating.append(i.text)
    
    a = driver.find_elements_by_xpath("//div[@class='list-view-course-card--rating--za-yU']/span[2]")
    for i in a:
        t=i.text.split()
        e=t[0]
        e=e[1:]
        
        list2=e.split(',')
        p=''
        for i in list2:
           p=p+i 
        norating.append(p)
    
    
    a = driver.find_elements_by_xpath("//div[@class='list-view-course-card--meta-with-badge--3oqjF']/span[2]/span")
    for i in a:
        difficulty.append(i.text)
    
    a = driver.find_elements_by_xpath("//div[@class='list-view-course-card--course-card-wrapper--TJ6ET']/a")
    for i in a:
        #udemylink.append(i.get_attribute("href"))
        link1.append(i.get_attribute("href"))
    count = 0
    for i in link1:
        driver.get(str(i))
        q12=" "
        try:
            q12 = driver.find_element_by_xpath("//h1[@data-purpose='lead-title']")
        except :
            q12=" "
        
        udemyname.append(q12.text)
        udemylink.append(i)
        udemysite.append("Udemy")
        
            
            
        
        
        a1 = driver.find_elements_by_xpath("//div[@data-purpose='enrollment']")
        f=''
        for j in a1:
            f=f+j.text+" "
        list1=f.split()
        list3=list1[0].split(',')
        p=''
        for i in list3:
           p=p+i 
        enrollment_number.append(p)
        
        h=''
        
        e=driver.find_elements_by_xpath("//a[@data-purpose='toggle-all-sections']")
        for i in e:
            i.click()
        driver.implicitly_wait(5) 
        l = driver.find_elements_by_xpath("//div[@class='lecture-container']/div[1]/div/div")
        for y in l:
            h=h+str(y.text)+','
        udemydetail.append(h)
        a1 = driver.find_elements_by_xpath("//span[@data-purpose='video-content-length']")
        y=''
        for j in a1:
            y=y+j.text+','
        list1=y.split()
        e=float(list1[0])
        e=e*60
        time.append(e)
        a1 = driver.find_elements_by_xpath("//div[@class='instructor--instructor__title-and-job-title--1nr2Z']/div[1]/a")
        ins=''
        for j in a1:
            ins=ins+str(j)+','
        instructor.append(j.text)
        count += 1
    driver.close()
                
    
def detail1():   
    udemy=pd.read_csv("udemy.csv",usecols = ['detail']) 
    cse=pd.read_csv("cse123.csv")
    for index,item in cse.iterrows():
        if item["topic"]=="CSN 102":
            y=item["syllabus"]
    porter=PorterStemmer()
    item1=[]
    item2=[]
    item3=[]
    def stemSentence(sentence):
        token_words=word_tokenize(sentence)
        token_words
        stem_sentence=[]
        for word in token_words:
            stem_sentence.append(porter.stem(word))
            stem_sentence.append(" ")
        return "".join(stem_sentence)
    
    bad_chars = [';', ':', '!', "*",'-',',',"''",'``'] 
    y=("Data Structures and Algorithms,Measuring Running time of Algorithms,Asymptotic Analysis,Big O Notation,Finding Big O,Tight and Loose Upper Bounds,Introduction Quiz A,Big O analysis of Algorithms,Finding Time Comlexity,Big O analysis of Algorithms: Examples,Worst case, Best case and Average Case Analysis,Common Complexities,Abstract Data Types,Introduction Quiz B,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,Data Structures and Algorithms,Measuring Running time of Algorithms,Asymptotic Analysis,Big O Notation,Finding Big O,Tight and Loose Upper Bounds,Introduction Quiz A,Big O analysis of Algorithms,Finding Time Comlexity,Big O analysis of Algorithms: Examples,Worst case, Best case and Average Case Analysis,Common Complexities,Abstract Data Types,Introduction Quiz B,Introduction,Traversing and Searching a Single Linked List,Finding pointers in a single linked list,Insertion in a Single Linked List..contd,Deletion in a Single Linked List,Reversing a Single Linked List,Linked List Quiz A,Doubly linked list,Insertion in a doubly linked List,Deletion from doubly linked list,Reversing a doubly linked list,Circular linked list,Insertion in a circular Linked List,Deletion in a circular linked list,Concatenation,Linked List with Header Node,Sorted linked list,Merging of sorted Linked lists,Sorting a Linked list using Bubble Sort,Sorting a Linked list using Merge Sort,Finding and Removing a cycle in a Linked list,Linked List Quiz B,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,Data Structures and Algorithms,Measuring Running time of Algorithms,Asymptotic Analysis,Big O Notation,Finding Big O,Tight and Loose Upper Bounds,Introduction Quiz A,Big O analysis of Algorithms,Finding Time Comlexity,Big O analysis of Algorithms: Examples,Worst case, Best case and Average Case Analysis,Common Complexities,Abstract Data Types,Introduction Quiz B,Introduction,Traversing and Searching a Single Linked List,Finding pointers in a single linked list,Insertion in a Single Linked List..contd,Deletion in a Single Linked List,Reversing a Single Linked List,Linked List Quiz A,Doubly linked list,Insertion in a doubly linked List,Deletion from doubly linked list,Reversing a doubly linked list,Circular linked list,Insertion in a circular Linked List,Deletion in a circular linked list,Concatenation,Linked List with Header Node,Sorted linked list,Merging of sorted Linked lists,Sorting a Linked list using Bubble Sort,Sorting a Linked list using Merge Sort,Finding and Removing a cycle in a Linked list,Linked List Quiz B,Introduction,Stack,Array Implementation of Stack,Linked List Implementation of Stack,Queue,Array Implementation of Queue,Linked List implementation of Queue,Queue through Circular Linked List,Circular Queue,Deque,Priority Queue,Checking validity of an expression containing nested parentheses,Function calls,Evaluating Arithmetc Expressions,Polish Notations,Converting infix expression to postfix expression,Evaluation of postfix expression,Stack and Queue Quiz,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,Data Structures and Algorithms,Measuring Running time of Algorithms,Asymptotic Analysis,Big O Notation,Finding Big O,Tight and Loose Upper Bounds,Introduction Quiz A,Big O analysis of Algorithms,Finding Time Comlexity,Big O analysis of Algorithms: Examples,Worst case, Best case and Average Case Analysis,Common Complexities,Abstract Data Types,Introduction Quiz B,Introduction,Traversing and Searching a Single Linked List,Finding pointers in a single linked list,Insertion in a Single Linked List..contd,Deletion in a Single Linked List,Reversing a Single Linked List,Linked List Quiz A,Doubly linked list,Insertion in a doubly linked List,Deletion from doubly linked list,Reversing a doubly linked list,Circular linked list,Insertion in a circular Linked List,Deletion in a circular linked list,Concatenation,Linked List with Header Node,Sorted linked list,Merging of sorted Linked lists,Sorting a Linked list using Bubble Sort,Sorting a Linked list using Merge Sort,Finding and Removing a cycle in a Linked list,Linked List Quiz B,Introduction,Stack,Array Implementation of Stack,Linked List Implementation of Stack,Queue,Array Implementation of Queue,Linked List implementation of Queue,Queue through Circular Linked List,Circular Queue,Deque,Priority Queue,Checking validity of an expression containing nested parentheses,Function calls,Evaluating Arithmetc Expressions,Polish Notations,Converting infix expression to postfix expression,Evaluation of postfix expression,Stack and Queue Quiz,Introduction,Flow of control in Recursive functions,Winding and unwinding phase,Factorial,Printing numbers from 1 to n,Sum of digits of an integer,Base conversion,Finding nth power of a number,Euclids Algorithm,Fibonacci Series,Tower of Hanoi,Tail recursion,Recursion vs. Iteration,Recursion Quiz,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,Data Structures and Algorithms,Measuring Running time of Algorithms,Asymptotic Analysis,Big O Notation,Finding Big O,Tight and Loose Upper Bounds,Introduction Quiz A,Big O analysis of Algorithms,Finding Time Comlexity,Big O analysis of Algorithms: Examples,Worst case, Best case and Average Case Analysis,Common Complexities,Abstract Data Types,Introduction Quiz B,Introduction,Traversing and Searching a Single Linked List,Finding pointers in a single linked list,Insertion in a Single Linked List..contd,Deletion in a Single Linked List,Reversing a Single Linked List,Linked List Quiz A,Doubly linked list,Insertion in a doubly linked List,Deletion from doubly linked list,Reversing a doubly linked list,Circular linked list,Insertion in a circular Linked List,Deletion in a circular linked list,Concatenation,Linked List with Header Node,Sorted linked list,Merging of sorted Linked lists,Sorting a Linked list using Bubble Sort,Sorting a Linked list using Merge Sort,Finding and Removing a cycle in a Linked list,Linked List Quiz B,Introduction,Stack,Array Implementation of Stack,Linked List Implementation of Stack,Queue,Array Implementation of Queue,Linked List implementation of Queue,Queue through Circular Linked List,Circular Queue,Deque,Priority Queue,Checking validity of an expression containing nested parentheses,Function calls,Evaluating Arithmetc Expressions,Polish Notations,Converting infix expression to postfix expression,Evaluation of postfix expression,Stack and Queue Quiz,Introduction,Flow of control in Recursive functions,Winding and unwinding phase,Factorial,Printing numbers from 1 to n,Sum of digits of an integer,Base conversion,Finding nth power of a number,Euclids Algorithm,Fibonacci Series,Tower of Hanoi,Tail recursion,Recursion vs. Iteration,Recursion Quiz,Intoduction to Trees,Binary Tree,Strictly Binary Tree and Extended Binary Tree,Full binary tree and Complete Binary Tree,Array Representation of Binary trees,Linked Representation of Binary Trees,Binary Tree Quiz A,Traversal in Binary Tree,Preorder Traversal,Inorder Traversal,Level order traversal,Finding height of a Binary tree,Binary Tree in C,Constructing Binary tree from Traversals,Cosntructing binary tree from inorder and preorder traversals,Constructing binary tree from postorder and inorder traversals,Binary Tree Quiz B,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,Data Structures and Algorithms,Measuring Running time of Algorithms,Asymptotic Analysis,Big O Notation,Finding Big O,Tight and Loose Upper Bounds,Introduction Quiz A,Big O analysis of Algorithms,Finding Time Comlexity,Big O analysis of Algorithms: Examples,Worst case, Best case and Average Case Analysis,Common Complexities,Abstract Data Types,Introduction Quiz B,Introduction,Traversing and Searching a Single Linked List,Finding pointers in a single linked list,Insertion in a Single Linked List..contd,Deletion in a Single Linked List,Reversing a Single Linked List,Linked List Quiz A,Doubly linked list,Insertion in a doubly linked List,Deletion from doubly linked list,Reversing a doubly linked list,Circular linked list,Insertion in a circular Linked List,Deletion in a circular linked list,Concatenation,Linked List with Header Node,Sorted linked list,Merging of sorted Linked lists,Sorting a Linked list using Bubble Sort,Sorting a Linked list using Merge Sort,Finding and Removing a cycle in a Linked list,Linked List Quiz B,Introduction,Stack,Array Implementation of Stack,Linked List Implementation of Stack,Queue,Array Implementation of Queue,Linked List implementation of Queue,Queue through Circular Linked List,Circular Queue,Deque,Priority Queue,Checking validity of an expression containing nested parentheses,Function calls,Evaluating Arithmetc Expressions,Polish Notations,Converting infix expression to postfix expression,Evaluation of postfix expression,Stack and Queue Quiz,Introduction,Flow of control in Recursive functions,Winding and unwinding phase,Factorial,Printing numbers from 1 to n,Sum of digits of an integer,Base conversion,Finding nth power of a number,Euclids Algorithm,Fibonacci Series,Tower of Hanoi,Tail recursion,Recursion vs. Iteration,Recursion Quiz,Intoduction to Trees,Binary Tree,Strictly Binary Tree and Extended Binary Tree,Full binary tree and Complete Binary Tree,Array Representation of Binary trees,Linked Representation of Binary Trees,Binary Tree Quiz A,Traversal in Binary Tree,Preorder Traversal,Inorder Traversal,Level order traversal,Finding height of a Binary tree,Binary Tree in C,Constructing Binary tree from Traversals,Cosntructing binary tree from inorder and preorder traversals,Constructing binary tree from postorder and inorder traversals,Binary Tree Quiz B,Introduction,Traversal in Binary Search Tree,Searching in a Binary Search Tree,Nodes with Minimum and Maximum key,Insertion in a Binary Search Tree,Deletion in a Binary Search Tree,Binary Search Tree Quiz,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")
    
    for index,item in udemy.iterrows():
        q=(item["detail"])
        for i in bad_chars : 
            q = q.replace(i, '')
            y = y.replace(i,'')
        item1.append(q)
    for item in item1:
        q=item
        q=stemSentence(q)
        item2.append(q)
    y=stemSentence(y)
    
    
    str2=""
    import nltk
    from nltk.stem import 	WordNetLemmatizer
    wordnet_lemmatizer = WordNetLemmatizer()
    
    for item in item2 :
        text = item
        tokenization = nltk.word_tokenize(text)
        str1=""
        for w in tokenization:
            str1 = str1 + wordnet_lemmatizer.lemmatize(w)+" "
        item3.append(str1)
    
    text = y
    tokenization = nltk.word_tokenize(text)
    for w in tokenization:
        str2 += wordnet_lemmatizer.lemmatize(w)+" "
    
    for item in item3 :
        Token_set_Ratio = fuzz.token_set_ratio(item,str2)
        print(Token_set_Ratio)
        detail_score.append(Token_set_Ratio)
    d1 = [name, rating,difficulty,match,enrollment_number,link,detail,detail_score,view,time,instructor,norating,noreviews]
    export_data1 = zip_longest(*d1, fillvalue = '')
    
    with open('udemy1.csv', 'w', encoding="utf-8", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("Name", "Rating","Difficulty","Match","enrollment-number","link","detail","detail_score","view","time","instructor","no_rating","no_reviews"))
        wr.writerows(export_data1)
    myfile.close()

prevsize=0
data123=pd.read_csv(r"C:\Users\Harsh\Desktop\mech.csv")
for index,item in data123.iterrows():
        name1=item['Name']
        coursedetail=item['Detail']
        coursecode=item['Code']
        t1 = Thread(target=coursera,args=(name1,3,))
        t2 = Thread(target=udemy,args=(name1,1,))
        t3 = Thread(target=edxCourses,args=(name1,))
        t4 = Thread(target=futureLearnCourses,args=(name1,))
        t5 = Thread(target=youtubeCourses,args=(name1,"mechanical",))
        t6 = Thread(target=lyndaCourses,args=(name1,))
        t7 = Thread(target=mitcourses,args=(name1,))

        #t1.start()
        t3.start()
        t2.start()
        t4.start()
        t5.start()
        t6.start()
        t7.start()

        #t1.join()
        t2.join()
        t4.join()
        t5.join()
        t6.join()
        t7.join()
        t3.join()
        
        nextsize=len(courseraname)+len(udemyname)+len(edxname)+len(youtubename)+len(lyndaname)+len(mitname)+len(futurename)
        size123=nextsize-prevsize
        for i in range(0,nextsize):
            finalCoursename.append(name1)
            finalcoursedetail.append(coursedetail)
            finalcoursecode.append(coursecode)
        prevsize = nextsize
        for i in courseraname:
            finalname.append(i)
        for i in courserasite:
            finalsite.append(i)
        for i in courseralink:
            finallink.append(i)
        for i in courseradetail:
            finaldetail.append(i)
        
        
        for i in udemyname:
            finalname.append(i)
        for i in udemysite:
            finalsite.append(i)
        for i in udemylink:
            finallink.append(i)
        for i in udemydetail:
            finaldetail.append(i)
            
            
        for i in edxname:
            finalname.append(i)
        for i in edxsite:
            finalsite.append(i)
        for i in edxlink:
            finallink.append(i)
        for i in edxdetail:
            finaldetail.append(i)
            
            
        for i in youtubename:
            finalname.append(i)
        for i in youtubesite:
            finalsite.append(i)
        for i in youtubelink:
            finallink.append(i)
        for i in youtubedetail:
            finaldetail.append(i)
            
            
        for i in lyndaname:
            finalname.append(i)
        for i in lyndasite:
            finalsite.append(i)
        for i in lyndalink:
            finallink.append(i)
        for i in lyndadetail:
            finaldetail.append(i)
            
            
        for i in mitname:
            finalname.append(i)
        for i in mitsite:
            finalsite.append(i)
        for i in mitlink:
            finallink.append(i)
        for i in mitdetail:
            finaldetail.append(i)
            
        
        for i in futurename:
            finalname.append(i)
        for i in futuresite:
            finalsite.append(i)
        for i in futurelink:
            finallink.append(i)
        for i in futuredetail:
            finaldetail.append(i)
        mitname.clear()
        mitdetail.clear()
        mitsite.clear()
        mitlink.clear()
        
        lyndaname.clear()
        lyndadetail.clear()
        lyndasite.clear()
        lyndalink.clear()
        
        edxname.clear()
        edxdetail.clear()
        edxsite.clear()
        edxlink.clear()
        
        
        futurename.clear()
        futuredetail.clear()
        futuresite.clear()
        futurelink.clear()
        
        youtubename.clear()
        youtubedetail.clear()
        youtubesite.clear()
        youtubelink.clear()
        
        
        courseraname.clear()
        courseradetail.clear()
        courserasite.clear()
        courseralink.clear()
        
        udemyname.clear()
        udemydetail.clear()
        udemysite.clear()
        udemylink.clear()




with open('mech1.csv', 'w', encoding="utf-8", newline='') as myfile:
      wr = csv.writer(myfile)
      
      wr.writerow(("Name","Detail","Site","Link","Code","Cdetail","Cname"))
      wr.writerows(export_data)
myfile.close()


    
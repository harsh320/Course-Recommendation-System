import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mp1.settings')

import django
django.setup()

from course.models import Content,Subjects,Branch
import pandas as pd
def subject_add():
    data = pd.read_csv(r"/home/ashutosh/PycharmProjects/mp1/test.csv")
    Subjects.objects.all().delete()
    branch = Branch.objects.get(branch_name='CSE')
    c=1
    h=[]
    for index, item in data.iterrows():
        name1 = str(item['Name'])
        code = str(item['Code'])
        t = Subjects.objects.get_or_create(course_code=code, course_name=name1, branch_name1=branch)[0]
        if(t==True):
            print(name1)
        print(c)
        c += 1
        t.save()
    h=set(h)
    print(len(h))
def content_add():
    data=pd.read_csv(r"/home/ashutosh/PycharmProjects/mp1/finalfinalfinalfinal1.csv")
    Content.objects.all().delete()
    branch=Branch.objects.get(branch_name='CSE')
    for index,item in data.iterrows():
        name1=item['Name']
        if name1=="":
         continue
        url1=item['Link']
        site1=item['Site']
        percent_similar1=item['Ratio']

        if percent_similar1 == "0":
            continue
        keywords2=item['WordsMatch']
        code=str(item["Code"])
        y = Subjects.objects.get(course_code=code)
        t=Content.objects.get_or_create(subject1=y,name=name1,url=url1,site=site1,percent_similar=percent_similar1,keywords1=keywords2,branch_name1=branch)[0]
        t.save()

if __name__=='__main__':
    print("polpulating script!")
    content_add()
    print("polpulating complete!")

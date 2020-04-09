import xlrd

# Give the location of the file
loc = ("/home/lavi_singla/Downloads/cse_syllabus_1(1).xlsx")

wb = xlrd.open_workbook(loc)


topic=[]
topic_page_detail=[]
syllabus=[]


#making a list of all course codes
for page in range(0,wb.nsheets):
    sheet = wb.sheet_by_index(page)
    # if course_id_start == 0 :
    for i in range(sheet.nrows):
            cell = sheet.cell_type(i,0)
            cell1=sheet.cell_type(i,1)
            if cell != xlrd.XL_CELL_EMPTY or cell1 != xlrd.XL_CELL_EMPTY :
                if sheet.cell_value(i,0) == "Course Code" or sheet.cell_value(i,1) == "Course Code":
                    for j in range(2,20):
                        try:
                            cell = sheet.cell_type(i,j)
                        except:
                            continue

                        if cell != xlrd.XL_CELL_EMPTY:
                            if len(sheet.cell_value(i,j)) == 6 or len(sheet.cell_value(i,j)) == 7 :
                                topic.append(sheet.cell_value(i,j))
                                topic_page_detail.append([page,i])
                        else:
                            continue


#function that find syllabus of all courses line wise
def add_syllabus(page,row):
    text=""
    diff=2
    sheet = wb.sheet_by_index(page)
    if sheet.nrows <= row+2:
        diff = diff - (sheet.nrows-row)
        page = page + 1

    start=1
    while True:
        sheet=wb.sheet_by_index(page)
        if start==1:
            for i in range(row+diff,sheet.nrows):
                try:

                    if sheet.cell_value(i,0) == "Sr." or sheet.cell_value(i,0) == "List of Experiments:" :
                        return text
                    else:
                        cell=sheet.cell_type(i,1)
                        if cell == xlrd.XL_CELL_EMPTY:
                            text=text+ str(sheet.cell_value(i,2))
                            text=text+ " "
                        else:
                            text=text+ str(sheet.cell_value(i,1))
                            text=text+ " "
                except:
                    pass
            start=0
            page=page+1
        else:
            for i in range(sheet.nrows):
                try:

                    if sheet.cell_value(i,0) == "Sr." or sheet.cell_value(i,0).find("List of Experiments:")!=-1 or sheet.cell_value(i,0).find("Course Outcomes")!= (-1):
                        return text
                    else:
                        cell=sheet.cell_type(i,1)
                        if cell == xlrd.XL_CELL_EMPTY:
                            text=text+ str(sheet.cell_value(i,2))
                            text=text+ " "
                        else:
                            text=text+ str(sheet.cell_value(i,1))
                            text=text+ " "
                except:
                    pass
            page=page+1




#finding syllabus of courses
for page in range(0,wb.nsheets):
    sheet = wb.sheet_by_index(page)
    # if course_id_start == 0 :
    for i in range(sheet.nrows):
            cell = sheet.cell_type(i,0)
            if cell != xlrd.XL_CELL_EMPTY :
                if sheet.cell_value(i,0) == "Lecture wise breakup":
                    syllabus.append(add_syllabus(page,i))

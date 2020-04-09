from datetime import date, time,datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Cast
from django.db.models import IntegerField
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from course.forms import QuestionForm, CommentForm, UserProfileInfoForm, UserForm
from .models import Branch,Subjects,Content,Tags,Thread,Comment,ItemTag
def index(request):
    return render(request,'index.html')
# Create your views here.
def search_course(request,query ='' ):

    if(request.method=='GET'):
            x =request.GET.get('q')
            if x is None:
                x=''
            course=Subjects.objects.filter(Q(course_name__icontains=x)|Q(course_code__icontains=x))
            return render(request,'Search_course.html',{'courses':course})
    return render(request,'Search_course.html')


def course(request):
    branchs = Branch.objects.all().order_by('branch_full_name')
    return render(request,'course.html',{'branchs':branchs})


def about_project(request):
    return render(request,'about_project.html')


def about_us(request):
    return render(request,'about-us.html')


def all_courses(request,pk = 1):
    branch = Branch.objects.get(pk=pk)
    course = Subjects.objects.filter(branch_name1=branch)
    return render(request,'all_courses.html',{'course':course})


def online_courses(request,pk=1,branchid = 1):
    x = Subjects.objects.get(pk=pk)
    y = Branch.objects.get(pk=branchid)
    content = Content.objects.annotate(percert_similar_int=Cast('percent_similar',output_field=IntegerField())).filter(subject1=x,branch_name1=y).order_by('percert_similar_int').reverse()
    return render(request,'best_online_courses.html',{'content':content})


def forum(request):


    logged_in = False

    if request.user.is_authenticated:
        logged_in = True

    threads = Thread.objects.order_by('no_of_likes').reverse()
    tags = Tags.objects.order_by('tag_count')
    if len(tags) > 10:
        tags = tags[:10]

    thread = []
    for t in threads:
        detail = []
        detail.append(t.question)
        detail.append(t.description[:325])
        detail.append(t.id)
        thread.append(detail)
    print(threads)
    return render(request, 'forum.html', {'thread': threads, 'tags': tags, 'logged_in': logged_in})


def add_question(request):

    questionForm = QuestionForm
    logged_in= False
    if request.user.is_authenticated:
        logged_in = True
        if request.method == 'POST':
            question = QuestionForm(data=request.POST)

            if question.is_valid:

                #saving new question to database
                q = question.save(commit=False)
                q.no_of_likes=0
                q.no_of_views=0
                q.date = date.today()
                x = datetime.now()
                q.time = x.strftime("%H:%M:%S")
                q.save()

                #adding tags to database from new question
                tags = question['tags'].value().split()
                for tag in tags:
                    tagObj = Tags.objects.filter(tag_name=tag)
                    print(tagObj)
                    if tagObj.exists():
                        obj = Tags()
                        obj = tagObj[0]
                        count = tagObj[0].tag_count
                        obj.tag_count = count + 1
                        print(count,obj)
                        obj.save()
                        itemtagObj = ItemTag()
                        itemtagObj.tagId = tagObj[0].id
                        itemtagObj.thread_id = q.id
                        itemtagObj.tag_name = tag
                        itemtagObj.save()
                    else:
                        tagObj = Tags()
                        tagObj.tag_name=tag
                        tagObj.tag_count=1
                        tagObj.save()
                        itemtagObj = ItemTag()
                        itemtagObj.tagId = tagObj.id
                        itemtagObj.thread_id = q.id
                        itemtagObj.tag_name = tag
                        itemtagObj.save()
                return render(request,'addQuestion.html',{'questionform':questionForm,
                'logged_in':logged_in})
            else:
                pass

        else:
            pass

        context={
        'questionform':questionForm,
        'logged_in':logged_in
        }
        return render(request,'addQuestion.html',context)
    else:
        messages.add_message(request, messages.INFO, "register to add question...")
        return redirect('register')



def tags_view(request,tag_name):
    logged_in= False
    if request.user.is_authenticated:
        logged_in = True
    data = ItemTag.objects.filter(tag_name=tag_name)
    print(data)
    threads=[]
    for t in data:
        threads.append(Thread.objects.filter(id=t.thread_id)[0])
    print(threads)
    return render(request,'forum/tag_page.html',context={'threads':threads,'logged_in':logged_in})

def thread_view(request,thread_id):
    logged_in= False
    if request.user.is_authenticated:
        logged_in = True

    if request.method=='POST':
        if logged_in==False:
            return HttpResponse("this is wrong. u need to login first")
        comment = CommentForm(data = request.POST)

        if comment.is_valid:
            q = comment.save(commit=False)
            q.likes=0
            q.views=0
            thread = Thread.objects.filter(id=thread_id)[0]
            q.thread = thread
            q.date = date
            q.time = time
            q.save()

    thread = Thread.objects.filter(id=thread_id)[0]
    comments = Comment.objects.filter(thread=thread).order_by('likes')
    commentForm = CommentForm
    return render(request,'forum/thread_page.html',{'thread':thread,'comments':comments,'commentForm':commentForm,'logged_in':logged_in})


def course_details(request,name=1 ,branchid = 1,pk=1 ):
    subject = Subjects.objects.get(id=name)
    branch = Branch.objects.get(id = branchid)
    content = Content.objects.get(subject1=subject,branch_name1=branch,pk=pk)
    return render(request,'course_details.html',{'content':content})


#
#
def logout_view(request):
    logout(request)
    return redirect('/course/')


def register_view(request):
    registered=False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered=True
            return redirect('/course')
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=UserForm
        profile_form=UserProfileInfoForm

    context={
    'user_form':user_form,
    'profile_form':profile_form,
    'registered':registered,
    }
    return render(request,'user_auth/register.html',context)


def login_view(request):
        if request.user.is_authenticated:
            return redirect("/course/")

        if request.method == 'POST':
            # First get the username and password supplied
            username = request.POST.get('username')
            password = request.POST.get('password')
            print("They used username: {} and password: {}".format(username,password))

            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)

            # If we have a user
            if user:

                #Check it the account is active
                if user.is_active:

                    # Log the user in.
                    login(request,user)
                    return redirect("/course/")


                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                x="Wrong Credentials"
                return render(request,'user_auth/login.html',{"error":x})

        else:
            #Nothing has been provided for username or password.
            return render(request, 'user_auth/login.html', {})

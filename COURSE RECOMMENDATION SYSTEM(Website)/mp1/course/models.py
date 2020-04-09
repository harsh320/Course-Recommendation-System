from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.urls import reverse

# Create your models here.
class Branch(models.Model):
    branch_name = models.CharField(max_length=256)
    branch_full_name = models.CharField(max_length=256)

    def __str__(self):
        return self.branch_name

    def get_absolute_url(self):
        return reverse("content1:Subject",kwargs={'pk':self.pk,'branch_name12':self.branch_name})


class Subjects(models.Model):
    course_code = models.CharField(max_length=256)
    course_name = models.CharField(max_length=256)
    branch_name1 = models.ForeignKey(Branch,on_delete=models.CASCADE,related_name='subject123')

    def __str__(self):
        return self.course_code

    def get_absolute_url(self):
        return reverse("content1:Contentlist",kwargs={'pk':self.pk,'pk1':branch_name1.pk})


class Content(models.Model):
    subject1 = models.ForeignKey(Subjects,on_delete=models.CASCADE,related_name='content56')
    name = models.CharField(max_length=256)
    url = models.URLField()
    site = models.CharField(max_length=256)
    percent_similar = models.CharField(max_length=256)
    keywords1 = models.CharField(max_length=1000,default="")
    branch_name1 = models.ForeignKey(Branch,on_delete=models.CASCADE,related_name='content57')

    def get_absolute_url(self):
        return reverse("content1:detail",kwargs={'pk':self.pk,'pk1':subject1.pk,'pk2':branch_name1.pk})


    def __str__(self):
       return self.name


class Thread(models.Model):
    date = models.DateField( null=True)
    time = models.TimeField( null=True)
    no_of_views = models.IntegerField()
    question = models.CharField( max_length=200)
    description = models.CharField( max_length=10000)
    tags = models.CharField( max_length=100)
    no_of_likes = models.IntegerField()
    #created_by =

class Comment(models.Model):
    thread = models.ForeignKey(Thread,  on_delete=models.CASCADE)
    #comment_by =
    likes = models.IntegerField()
    date = models.DateField( null=True)
    time = models.TimeField( null=True)
    description = models.CharField( max_length=10000)

class Tags(models.Model):
    tag_name = models.CharField( max_length=50)
    tag_count = models.IntegerField()



class ItemTag(models.Model):
    thread_id = models.IntegerField()
    tagId= models.IntegerField()
    tag_name = models.CharField(max_length=40)

class user_verify(models.Manager):
    def check_user(self,username):
        return self.filter(user__username=username)

    def get_merchant_details(self,merchant_id):
        return self.filter(user__username=merchant_id)

    def get_user_details(self,user_id):
        return self.filter(user__username=user_id)



class user_info(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact=models.IntegerField()
    no_of_ques_posted = models.IntegerField(default=0)
    no_of_comments = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username

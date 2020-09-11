from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User 

# Create your models here.
#

# '''
# django model field :
#     - html widget
#     - validation
#     - db size
# 

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'), 

)

def image_upload(instance,filename):
    imagename , extentions = filename.split(".")
    return  "jobs/%s.%s"%(instance.id,extentions)



class job(models.Model): #table 
    owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title = models.CharField(max_length=100) #column
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    descriptions = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(blank=True, null=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(job,self).save(*args, **kwargs)


    def __str__(self):
        return self.title

class category(models.Model): #table 
    name = models.CharField(max_length=25) #column
    
    
    def __str__(self):
        return self.name



class apply(models.Model):
    job = models.ForeignKey(job,related_name='apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
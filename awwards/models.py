from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    technologies_used =models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    project_image = CloudinaryField('image')
    repo_link = models.URLField(max_length=256)
    live_link = models.URLField(max_length=256)
    user = models.ForeignKey(User,on_delete = models.CASCADE)

    @classmethod
    def display_projects(cls):
        projects = cls.objects.all()
        return projects

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_projects(cls, title):
        return cls.objects.filter(title__icontains=title).all()

    @classmethod
    def get_projects(cls):
        return cls.objects.all()

    def __str__(self):
        return f'{self.title}'

class Profile(models.Model):
    profile_image = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=10,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    # @receiver(post_save , sender = User)
    def create_profile(instance,sender,created,**kwargs):
        if created:
            Profile.objects.create(user = instance)

    # @receiver(post_save,sender = User)
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()

    def __str__(self):
      return "%s profile" % self.user

class Rating(models.Model):
    content_wise = models.IntegerField(blank=True,default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
    content_wise_average = models.FloatField(default=0.0,blank=True)
    usability_wise = models.IntegerField(blank=True,default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
    usability_wise_average = models.FloatField(default=0.0,blank=True)
    design_wise = models.IntegerField(blank=True,default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
    design_wise_average = models.FloatField(default=0.0,blank=True)
    aggregate_average_rate = models.FloatField(default=0.0,blank=True)
    project = models.ForeignKey(Project,on_delete=CASCADE)
    user = models.ForeignKey(User,on_delete=CASCADE)


    def save_rating(self):
        self.save()

    @classmethod
    def get_ratings(cls, id):
        ratings = Rating.objects.filter(project_id=id).all()
        return ratings

    def __str__(self):
        return f'{self.project} Rating'

# class Rating(models.Model):
#     rating = (
#         (1, '1'),
#         (2, '2'),
#         (3, '3'),
#         (4, '4'),
#         (5, '5'),
#         (6, '6'),
#         (7, '7'),
#         (8, '8'),
#         (9, '9'),
#         (10, '10'),
#     )

#     design = models.IntegerField(choices=rating,  blank=True)
#     usability = models.IntegerField(choices=rating, blank=True)
#     content = models.IntegerField(choices=rating, blank=True)
#     score = models.FloatField(blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
   

#     def save_rating(self):
#         self.save()


#     @classmethod
#     def get_project_ratings(cls, id):
#         ratings = Rating.objects.filter(project_id=id).all()
#         return ratings

#     def __str__(self):
#         return str(self.id)
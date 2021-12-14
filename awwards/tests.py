from django.test import TestCase
from .models import Profile,Project, Rating
from django.contrib.auth.models import User

# Create your tests here.
class ProjectTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Caleb')
        self.project = Project.objects.create(id=1, title='Minute Pitch', description='An application where users can submit a one minute pitches and other users will vote on them and leave comments to give their feedback on them',technologies_used='Python',post_date='2021,12,12',project_image='https://cloudinary url', repo_link='http://github.com',live_link='http://heroku.com',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.project, Project))

    def test_display_projects(self):
        self.project.save()
        projects = Project.get_projects()
        self.assertTrue(len(projects) > 0)

    def test_save_post(self):
        self.project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)

    def test_delete_post(self):
        self.project.delete_project()
        project = Project.search_projects('random_project')
        self.assertTrue(len(project) < 1)

    def test_search_projects(self):
        self.project.save()
        project = Project.search_projects('random_project')
        self.assertTrue(len(project) >= 0)


class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Calebbii', password='1234')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()
        

class RatingTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='Calebbii')
        self.project = Project.objects.create(id=1, title='Nifty Design', description='This website showcases designers work and what their brands have produced.',technologies_used='HTML',post_date='2021,6,19',project_image='https://cloudinary url', repo_link='http://github.com',live_link='http://heroku.com',user=self.user)
        self.rating = Rating.objects.create(id=1, design_wise=8, usability_wise=8, content_wise=7, user=self.user, project=self.project)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

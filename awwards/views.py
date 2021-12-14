from django.contrib.auth.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
import datetime
from .forms import ProjectPostForm, RatingsForm, UpdateProfile, UpdateUser
from awwards.models import Project
from .models import Project,Rating,Profile
import random
from django.contrib import messages

# Create your views here.
# def home(request):
#     return render(request, 'home.html')
def home(request):
    post_form = ProjectPostForm()
    all_users = User.objects.all()
    projects = Project.display_projects()

    return render (request,'home.html',{"projects":projects,"post_project":post_form,"all_users":all_users})

def profile(request):
    current_user = request.user
    all_users = User.objects.all()
    projects = Project.objects.all().order_by('-post_date')
    user_projects = Project.objects.filter(user_id = current_user.id).all().order_by('-post_date')
    
    return render(request,'profile.html',{"current_user":current_user,'all_users':all_users,'projects':projects,'user_projects':user_projects,})


def detail(request,project_id):
    current_user = request.user
    all_ratings = Rating.objects.filter(project_id=project_id).all()
    project = Project.objects.get(pk = project_id)
    ratings = Rating.objects.filter(user=request.user,project=project_id).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.project = project
            rate.save()
            post_ratings = Rating.objects.filter(project=project_id)

            design_ratings = [design.design_wise for design in post_ratings]
            design_wise_average = sum(design_ratings) / len(design_ratings)

            usability_ratings = [usability.usability_wise for usability in post_ratings]
            usability_wise_average = sum(usability_ratings) / len(usability_ratings)

            content_ratings = [content.content_wise for content in post_ratings]
            content_wise_average = sum(content_ratings) / len(content_ratings)

            aggregate_average_rate = (design_wise_average + usability_wise_average + content_wise_average) / 3
            print(aggregate_average_rate)
            rate.design_wise_average = round(design_wise_average, 2)
            rate.usability_wise_average = round(usability_wise_average, 2)
            rate.content_wise_average = round(content_wise_average, 2)
            rate.aggregate_average_rate = round(aggregate_average_rate, 2)
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    return render(request, 'details.html', {'current_user':current_user,'all_ratings':all_ratings,'project':project,'rating_form': form,'rating_status': rating_status})

def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUser(request.POST,instance=request.user)
        profile_form = UpdateProfile(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'Your Profile account has been updated successfully')
        return redirect('profile')
    else:
        user_form = UpdateUser(instance=request.user)
        profile_form = UpdateProfile(instance=request.user.profile) 
    params = {
        'user_form':user_form,
        'profile_form':profile_form
    }
    return render(request,'update.html',params)
  
def search(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        search_projects = Project.search_projects(search_term)
        message = f"{search_term}"

        return render(request,'search.html', {"message":message,"projects":search_projects})
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message})


def users_profile(request,pk):
    user = User.objects.get(pk = pk)
    projects = Project.objects.filter(user = user)
    current_user = request.user
    
    return render(request,'users_profile.html',{"user":user,"projects":projects,"current_user":current_user})

def post_project(request):
    if request.method == 'POST':
        post_form = ProjectPostForm(request.POST,request.FILES) 
        if post_form.is_valid():
            new_post = post_form.save(commit = False)
            new_post.user = request.user
            new_post.save()
        return redirect('home')

    else:
        post_form = ProjectPostForm()
    return render(request,'post_project.html',{"post_form":post_form})


def delete(request,project_id):
    current_user = request.user
    project = Project.objects.get(pk=project_id)
    if project:
        project.delete_project()
    return redirect('home')
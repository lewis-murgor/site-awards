from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Project,Profile
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm,UpdateProfileForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all()

    return render(request, 'index.html',{"projects":projects})

@login_required(login_url='/accounts/login/')
def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        title = request.GET.get("project")
        searched_projects = Project.search_by_title(title)
        message = f"{title}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except Project.DoesNotExist:
        raise Http404()

    return render(request,"single_project.html", {"project":project})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user_id = current_user)
    profile = Profile.objects.filter(user_id = current_user)
    

    return render(request, 'profile.html',{"projects":projects, "profile":profile})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('profile')

    else:
        form = UpdateProfileForm()
    return render(request, 'update_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('profile')

    else:
        form = ProjectForm()
    return render(request, 'project.html', {"form": form})

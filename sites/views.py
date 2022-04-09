from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Project
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.objects.all()

    return render(request, 'index.html',{"projects":projects})

@login_required(login_url='/accounts/login/')
def project(request,project_id):
    try:
        project = Project.objects.get(id = project_id)
    except Project.DoesNotExist:
        raise Http404()

    return render(request,"single_project.html", {"project":project})

@login_required(login_url='/accounts/login/')
def profile(request):
    

    return render(request, 'profile.html')

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

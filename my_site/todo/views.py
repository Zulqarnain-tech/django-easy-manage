from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from . forms import AddTaskForm, AddProjectForm
from django.contrib.auth.decorators import login_required
from . import models


# Create your views here.
@login_required
def add_task(request,project_id):
    project = get_object_or_404(models.Project,id=project_id)
    form = AddTaskForm()
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('/todo/dashboard')
    return render(request, "todo/add_task.html", {'form': form})

@login_required
def project_delete(request,project_id):
    project_object=get_object_or_404(models.Project,id=project_id,account=request.user.id)
    if request.method == 'POST':
        project_object.delete()
        return redirect('dashboard')
    context = {'project_object': project_object}
    return render(request, "todo/delete_project.html",context)

@login_required
def project_detail(request, project_id):
    project_object = get_object_or_404(models.Project, id=project_id,account=request.user.id)
    task_list = models.Task.objects.filter(project__id=project_id)
    context = {'project_object': project_object, 'task_list': task_list}
    return render(request, "todo/detail_project.html", context)

@login_required
def project_edit(request,project_id):
    project_list = models.Project.objects.filter(account__user=request.user)
    task_list = models.Task.objects.filter(project__account=request.user.id)
    project_object = get_object_or_404(models.Project,id=project_id,account = request.user.id)
    form = AddProjectForm(instance=project_object)
    if request.method == 'POST':
        form = AddProjectForm(request.POST, instance=project_object)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {'form': form, 'project_list': project_list,'project_object':project_object,'task_list':task_list}
    return render(request, "todo/dashboard.html", context)

@login_required
def index(request):
    project_list = models.Project.objects.filter(account__user=request.user)
    task_list = models.Task.objects.filter(project__account=request.user.id)
    project_count = models.Project.objects.filter(account__user=request.user).count()
    task_count = models.Task.objects.filter(project__account=request.user.id).count()
    form = AddProjectForm()
    if request.method == 'POST':
        form = AddProjectForm(request.POST)
        
        if form.is_valid():
            add_project = form.save(commit=False)
            account_user = get_object_or_404(models.Account, user = request.user)
            add_project.account = account_user
            add_project.save()
            return redirect('dashboard')
    context = {'form': form, 'project_list': project_list,
               'task_list': task_list,'project_count':project_count,'task_count':task_count}
    return render (request,"todo/dashboard.html",context)



@login_required
def task_delete(request, task_id):
    task_object = get_object_or_404(models.Task, id=task_id, project__account=request.user.id)
    if request.method == 'POST':
        task_object.delete()
        return redirect('dashboard')
    context = {'task_object': task_object}
    return render(request, "todo/delete_task.html", context)

@login_required
def task_detail(request, project_id, task_id):
    task_object = get_object_or_404(models.Task, id=task_id, project__account = request.user.id)
    context = {'task_object': task_object}
    return render(request, "todo/detail_task.html", context)

@login_required
def task_edit(request, task_id):
    task_object = get_object_or_404(models.Task, id=task_id, project__account=request.user.id)
    form = AddTaskForm(instance=task_object)
    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task_object)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    return render(request, "todo/edit_task.html", {'form':form})

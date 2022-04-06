from urllib import request
from django.shortcuts import redirect, render
from testapp.models import Student
from testapp.forms import Add_Student_form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def home_page(request):
    return render(request, 'testapp/home.html')

@login_required
def register(request):
    form = Add_Student_form()
    if request.method == 'POST':
        form = Add_Student_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/new/list/')

    return render(request, 'testapp/register.html', {'form': form})

@login_required
def student_list(request):
    obj = Student.objects.all()
    return render(request, 'testapp/list.html', {'obj': obj})


@login_required
def update_record(request, id):
    obj = Student.objects.get(pk = id)
    form = Add_Student_form(instance=obj)
    if request.method == 'POST':
        form = Add_Student_form(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/new/list/')

    return render(request, 'testapp/update.html', {'form': form})   

@login_required
def delete_record(request, id):
    obj = Student.objects.get(pk = id)
    obj.delete()
    return redirect('/new/list/')

def create_account(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    return render(request, 'testapp/create_account.html',{'form':form})
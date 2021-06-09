from  .models import Users
from django.db.models import base
from django.shortcuts import HttpResponseRedirect, redirect, render
from .forms import UsersForm
from django.views.generic.list import ListView

# Create your views here.
def home(request):
    return render(request, 'register/base.html')

class UsersListView(ListView):
    model = Users
    template_name= 'register/student.html'
    context_object_name = 'stu'


def add_show(request):
    if request.method =='POST':
        fm = UsersForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('retrive')
            

    fm= UsersForm()
      
    # stud= Users.objects.all()
    # context2= {'stu':stud}
    return render(request, 'register/create.html',{'form': fm})
    
def edit(request, id):
    if request.method == 'POST':
        pi = Users.objects.get(pk=id )
        fm = UsersForm(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
    pi = Users.objects.get(pk=id )
    fm = UsersForm(instance = pi)

    return render(request, 'register/update.html', {'form':fm})

def delete_data(request, id):
    if request.method =='POST':
        pi = Users.objects.get(pk=id)
        print(pi)
        pi.delete()
        return render(request, 'register/student.html',{'stu': pi})

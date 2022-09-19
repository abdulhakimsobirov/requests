from ast import Delete
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Objects, Brigadir, Requests
from .forms import BrigadirForm, ObjectsForm, RequestsForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def user_login(request):

    if request.method == "POST":
        username = request.POST['username']
        passw = request.POST['password']

        user = authenticate(request, username=username, password=passw)
        if user is not None:
            login(request, user)
            return redirect('requests')
        
        else:
            return redirect('login')
    
    return render(request, 'login.html')

@login_required
def base(request):
    return render(request, 'base.html')

def menu(request):
    return render(request, 'menu.html')
# **********************************************Requests**************************************
def requests(request):
    requests = Requests.objects.filter(is_active=True)

    context = {'requests': requests}
    
    return render(request, 'request/request.html', context=context)


def create_requests(request):
    requestForm = RequestsForm()

    if request.method == "POST":
        myrequest = RequestsForm(request.POST)
        if myrequest.is_valid():
            myrequest.save()
            return redirect('requests')
        
    context = {'requestForm': requestForm}

    return render(request, 'request/create_request.html', context)

def update_requests(request, rid):
    requests = Requests.objects.get(id=rid)
    requestForm = RequestsForm(instance=requests)

    if request.method == "POST":
        myrequests = RequestsForm(request.POST, instance=requests) 
        if myrequests.is_valid():
            myrequests.save()
            return redirect('requests')

    context = {'requestForm': requestForm}
    return render(request, 'request/update_request.html', context)  

# def deactivate_request(request, pk):

#     requestForm = RequestsForm(instance=requests)

#     if request.method == "POST":
#         myrequests = RequestsForm(request.POST, instance=requests) 
#         if myrequests.is_valid():
#             r = myrequests.save()
#             r.is_active = 'False'
#             r.save()
#             return redirect('requests')



def delete_request(request, rid):
    requests = Requests.objects.get(id=rid)
    requestForm = RequestsForm(instance=requests)

    if request.method == "POST":
        ia = request.POST.getlist('is_active')
        if requestForm.is_valid():
            r = requestForm.save()
            if ia == 'is_active':
                r.ia = False
            return redirect('requests')

    context = {'requests': requests}

    return render(request, 'request/delete_request.html', context)


# **********************************************Objects*************************************



def objects(request):
    objects = Objects.objects.all()

    context = {'objects': objects}
    
    return render(request, 'object/objects.html', context=context)


def create_objects(request):
    objectForm = ObjectsForm()

    if request.method == "POST":
        myobject = ObjectsForm(request.POST)
        if myobject.is_valid():
            myobject.save()
            return redirect('objects')
        
    context = {'objectForm': objectForm}

    return render(request, 'object/create_object.html', context)

def update_objects(request, oid):
    object = Objects.objects.get(id=oid)
    objectForm = ObjectsForm(instance=object)

    if request.method == "POST":
        myrobject = ObjectsForm(request.POST, instance=object) 
        if myrobject.is_valid():
            myrobject.save()
            return redirect('objects')

    context = {'objectForm': objectForm}
    return render(request, 'object/update_object.html', context)   


# ***********************************************Brigadirs*****************************************


def brigadirs(request):
    brigadirs = Brigadir.objects.all()

    context = {'brigadirs': brigadirs}
    
    return render(request, 'brigadir/brigadir.html', context=context)

def create_brigadirs(request):
    brigadirForm = BrigadirForm()

    if request.method == "POST":
        mybrigadir = BrigadirForm(request.POST)
        if mybrigadir.is_valid():
            mybrigadir.save()
            return redirect('brigadirs')
        
    context = {'brigadirForm': brigadirForm}

    return render(request, 'brigadir/create_brigadir.html', context)

def update_brigadirs(request, bid):
    brigadir = Brigadir.objects.get(id=bid)
    brigadirForm = BrigadirForm(instance=brigadir)

    if request.method == "POST":
        mybrigadir = BrigadirForm(request.POST, instance=brigadir) 
        if mybrigadir.is_valid():
            mybrigadir.save()
            return redirect('brigadirs')

    context = {'brigadirForm': brigadirForm}
    return render(request, 'brigadir/update_brigadir.html', context)   


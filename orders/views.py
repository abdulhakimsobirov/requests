from ast import Delete
from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Objects, Brigadir, Requests
from .forms import BrigadirForm, ObjectsForm, RequestsForm, RequestIsActiveForm, ObjectIsActiveForm, BrigadirIsActiveForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .filters import RequestFilter

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
    if request.method == "POST":
        username = request.POST['username']
        passw = request.POST['password']

        user = authenticate(request, username=username, password=passw)
        if user is not None:
            login(request, user)
            return redirect('requests')
    
        else:
            return redirect('login')


    return render(request, 'base.html')

@login_required
def menu(request):
    return render(request, 'menu.html')
# **********************************************Requests**************************************
@login_required
def requests(request):
    requests = Requests.objects.filter(is_active=1)

    rfilter = RequestFilter(request.GET, queryset=requests)
    requests = rfilter.qs


    context = {'requests': requests,'rfilter': rfilter}
    
    return render(request, 'request/request.html', context=context)

@login_required
def create_requests(request):
    requestForm = RequestsForm()

    if request.method == "POST":
        myrequest = RequestsForm(request.POST)
        if myrequest.is_valid():
            myrequest.save()
            return redirect('requests')
        
    context = {'requestForm': requestForm}

    return render(request, 'request/create_request.html', context)
@login_required
def update_requests(request, rid):
    requests = Requests.objects.get(id=rid)
    requestForm = RequestsForm(instance=requests)

    if request.method == "POST":
        myrequests = RequestsForm(request.POST, instance=requests) 
        print(myrequests)
        if myrequests.is_valid():
            print(myrequests)
            myrequests.save()
            
            return redirect('requests')

    context = {'requestForm': requestForm}
    return render(request, 'request/update_request.html', context)  
@login_required
def delete_request(request, rid):
    requests = Requests.objects.get(id=rid)
    requestForm = RequestIsActiveForm(instance=requests)

    if request.method == "POST":
        myrequests = RequestIsActiveForm(request.POST, instance=requests) 
        if myrequests.is_valid():
            myrequests.save()
            return redirect('requests')

    context = {'requestForm': requestForm}

    return render(request, 'request/delete_request.html', context)

@login_required
def deleted_requests(request):
    requests = Requests.objects.filter(is_active=3)

    context = {'requests': requests}

    return render(request, 'request/deleted_requests.html', context)


# **********************************************Objects*************************************


@login_required
def objects(request):
    objects = Objects.objects.filter(is_active=1)

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
@login_required
def update_objects(request, oid):
    object = Objects.objects.get(id=oid)
    objectForm = ObjectsForm(instance=object)

    if request.method == "POST":
        myobject = ObjectsForm(request.POST, instance=object) 
        if myobject.is_valid():
            myobject.save()
            return redirect('objects')

    context = {'objectForm': objectForm}
    return render(request, 'object/update_object.html', context)   

@login_required
def delete_object(request, oid):
    object = Objects.objects.get(id=oid)
    objectForm = ObjectIsActiveForm(instance=object)

    if request.method == "POST":
        myobject = ObjectIsActiveForm(request.POST, instance=object) 
        if myobject.is_valid():
            myobject.save()
            return redirect('objects')

    context = {'objectForm': objectForm}
    return render(request, 'object/delete_object.html', context) 

@login_required
def deleted_objects(request):
    objects = Objects.objects.filter(is_active=3)

    context = {'objects': objects}

    return render(request, 'object/deleted_objects.html', context) 


# ***********************************************Brigadirs*****************************************

@login_required
def brigadirs(request):
    brigadirs = Brigadir.objects.filter(is_active=1)

    context = {'brigadirs': brigadirs}
    
    return render(request, 'brigadir/brigadir.html', context=context)
@login_required
def create_brigadirs(request):
    brigadirForm = BrigadirForm()

    if request.method == "POST":
        mybrigadir = BrigadirForm(request.POST)
        if mybrigadir.is_valid():
            mybrigadir.save()
            return redirect('brigadirs')
        
    context = {'brigadirForm': brigadirForm}

    return render(request, 'brigadir/create_brigadir.html', context)
@login_required
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
@login_required
def delete_brigadir(request, bid):
    brigadir = Brigadir.objects.get(id=bid)
    brigadirForm = BrigadirIsActiveForm(instance=brigadir)

    if request.method == "POST":
        mybrigadir = BrigadirIsActiveForm(request.POST, instance=brigadir) 
        if mybrigadir.is_valid():
            mybrigadir.save()
            return redirect('brigadirs')

    context = {'brigadirForm': brigadirForm}
    return render(request, 'brigadir/delete_brigadir.html', context)    

@login_required
def deleted_brigadirs(request):
    brigadirs = Brigadir.objects.filter(is_active=3)

    context = {'brigadirs': brigadirs}

    return render(request, 'brigadir/deleted_brigadirs.html', context)


from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Pet, TypeofPet


def hi(request):
    return HttpResponse("Hello is me!!")


def dog_registration(request):
    title = "Register Dog"
    # content_header = "Pending Request"
    type_of_pet = TypeofPet.objects.all()
    template = "base/dog_registration.html"

    content = {
        'title': title,
        'breed_type': type_of_pet
    }
    return render(request, template, content)


def index(request):
    title = "Login"
    # contentheader = "Pending Request"
    # data = Requests.objects.filter(trash=0, status=0).order_by('date_created')
    template = "base/login.html"

    content = {
        'title': title,
        # 'data': data
    }
    return render(request, template, content)



def registration(request):
    title = "Create"
    # contentheader = "Pending Request"
    # data = Requests.objects.filter(trash=0, status=0).order_by('date_created')
    template = "requests/all-pending-request.html"

    content = {
        'title': title,
        # 'data': data
    }
    return render(request, template, content)


def login(request):
    title = "Create"
    # contentheader = "Pending Request"
    # data = Requests.objects.filter(trash=0, status=0).order_by('date_created')
    template = "requests/all-pending-request.html"

    content = {
        'title': title,
        # 'data': data
    }
    return render(request, template, content)

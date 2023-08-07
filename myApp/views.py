from django.shortcuts import render, redirect
from myApp.models import Member, Course


# Create your views here.
def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        username=request.POST['username'], password=request.POST['password'])
        member.save()
        return redirect('/login')
    # elif request.method == 'POST':
    #     course = Course(coursecode=request.POST['coursecode'], coursename=request.POST['coursename'],
    #                     intake=request.POST['intake'], studymode=request.POST['studymode'])
    #     course.save()
    #     return redirect('/login')

    else:
        return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


# def home(request):
#     if request.method == 'POST':
#         if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
#             member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
#             return render(request, 'home.html', {'member': member})
#     else:
#         return render(request, 'login.html')
def home(request):
    return render(request, 'home.html')


def course(request):
    return render(request, 'Courses.html')


def aboutus(request):
    return render(request, 'About Us.html')


def main(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'main.html', {'member':member})
    else:
        return render(request, 'login.html')

    # {'member': member}, {'course': course;}

from django.http.response import HttpResponse
from django.shortcuts import render

from trivia_app.models import Student

# Create your views here.
def home(request):
    return render(request,'Ques1.html')

def Ques1(request):
    if request.method=='POST':
        username = request.post.get('username')
        ob = Student(username=username)
        ob.save()
        return render(request,'Ques2.html',{'username':username})
    else:
        return HttpResponse("Invalid Selection")
    
def Ques2(request):
    if request.method=='POST':
        username = request.post.get('username')
        ans1 = request.post.get('op')
        ob = Student.objects.get(pk=username)
        ob.ans1 = ans1
        ob.save()
        return render(request,'Ques2.html',)
    else:
        return HttpResponse("Invalid Selection")

def Ques2_save(request):
    if request.method=='POST':
        username = request.post.get('username')
        ans2 = request.post.getlist('op')
        print(ans2)
        ob = Student.objects.get(pk=username)
        ob.ans2 = ans2
        ob.save()
        return render(request,'home.html',{'message':'Data Saved Successfully'})
    else:
        return HttpResponse("Invalid Selection")

def history(request):
    ob = Student.objects.all()
    return render(request,'result.html',{'ob':ob})

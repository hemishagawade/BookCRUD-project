from django.shortcuts import render, redirect
from BookApp.models import Book

# Create your views here.
def homepage(request):
    # fetch data from database and display on homepage
    data = Book.objects.all()
    context = {}
    context['books'] = data
    return render(request,'home.html',context)

def addbook(request):
    if request.method=="GET":
        return render(request,'addbook.html')
    else:
        # 1) fetch FORM data 
        t = request.POST['title'] 
        a = request.POST['author'] 
        p = request.POST['price'] 
        # 2) inserting data into database
        b = Book.objects.create(title=t,author=a,price=p)
        b.save()
        # 3) return to home page
        # return render(request,'home.html') ===> sends to homepage, dose not display data
        return redirect('/home')

def deletebook(request,bookid):
    b = Book.objects.filter(id=bookid)
    b.delete()
    return redirect('/home')

def updatebook(request,bookid):
    if request.method=="GET":
        b = Book.objects.filter(id=bookid)
        context = {}
        context['book'] = b[0]
        return render(request,'updatebook.html',context)
    else: 
        t = request.POST['title'] 
        a = request.POST['author'] 
        p = request.POST['price']
        b = Book.objects.filter(id=bookid)
        b.update(title=t,author=a,price=p)
        return redirect('/home')
    
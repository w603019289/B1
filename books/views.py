from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import book,Author
# Create your views here.
def time(request):
    now = datetime.datetime.now()
    return render_to_response('time.txt',{'name':now})
def test(request):
    return render_to_response('test.html',{'name':"WYF"})
def search_form(request):
    return render_to_response('search_form.html')
def search(request):
    if 'q' in request.GET and request.GET['q'] and Author.objects.filter(Name=request.GET['q']):
        q=request.GET['q']
        Athor=Author.objects.get(Name=q)
        books=book.objects.filter(AuthorID__contains=Athor.AuthorID)
        return render_to_response('search_results.html',{'books':books,'query':q})
    else:
        return HttpResponse('No such Author!')
def Delete(request):
        b=book.objects.filter(Title=request.GET['p'])
        b.delete()
        book.objects.all()
        return render_to_response('search_form.html') 
def add(request):
        return render_to_response('add.html')
def addbook(request):
    j=request.GET['p']
    k=request.GET['q']
    l=request.GET['i']
    if Author.objects.filter(Name=j):
        Athor=Author.objects.get(Name=j)
        p1=book(AuthorID=Athor.AuthorID,Title=k)
        p1.save()
        return render_to_response('search_form.html')
    else:
        if Author.objects.filter(AuthorID=l):
            return HttpResponse("The ID already exists!")
        else:
            p2=Author(Name=j,AuthorID=l)
            p2.save()
            p=book(AuthorID=l,Title=k)
            p.save()
            return render_to_response('search_form.html')
def up(request):
    HAHA=request.GET['q']
    return render_to_response('updata.html',{"name":HAHA})
def update(request):
    N=request.GET['q']
    Name=request.GET['f']
    Per=request.GET['b']
    Pda=request.GET['c']
    Pr=request.GET['d']
    bok=book.objects.get(Title=N)
    bok.Name=Name
    bok.Publisher=Per
    bok.Publishdata=Pda
    bok.Price=Pr
    bok.save()
    return render_to_response('search_form.html')
def check(request):
    p=request.GET['k']
    bok=book.objects.get(Title=p)
    ID=bok.AuthorID
    Athor=Author.objects.get(AuthorID=ID)
    #{"Title":book.Title},
    #{"Name":Athor.Name},
    
    dic={"Title":bok.Title,
    "Name":Athor.Name,     
    "ID":ID,
    "Age":Athor.Age,
    "country":Athor.Country,
    "Publisher":bok.Publisher,
    "Publishdate":bok.PublishData,
    "ISBN":bok.ISBN,
    "Price":bok.Price}
    return render_to_response('check.html',dic)    
        
                
                                                                                                                                                                                                                                                        
    

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

def members(request):
    data={
       
     }
    try:
        num=request.GET['email']
    except:
        pass

    return render(request, 'index.html',data)

def mem(request):

    return HttpResponse("pardha  give up")


def prac(request):
    
    
    return render(request,'prac.html')

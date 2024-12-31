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

@csrf_protect
def prac(request):
    try:
        if request.method=='POST':
            email=request.POST['email']
            password=request.POST['password']
            return HttpResponse(email)
    except:
        pass
    
    return render(request,'prac.html')

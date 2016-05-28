from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

# Create your views here.
def home(request):
    try:
        f = urlopen("http://mejorando.la")
        g = f.read()
        f.close()
    except HTTPError as e:
        print( "Error!!!")
        print (e.code)
    except URLError as e:
        print ("Error!!!")
        print (e.code)
    
        
    return HttpResponse(g)
    
def home2(request):
    return HttpResponse("segunda pantalla de inicio")
    
def home3(request):
    return HttpResponse("TErcera")
    
def post(request,id_post):
    return HttpResponse("este es el post %s" % id_post)
    
def curso(request,id1,id2):
    return HttpResponse("Curso %s clase %s" % (id1, id2) )
    
def request(request):
    return HttpResponse("Datos del request %s" % request)
    

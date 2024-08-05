'''
Created on 2024. 4. 25.

@author: PC-02
'''
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("방탄 소년단")

def param(request):
    menu = request.GET['menu']
    print("menu" , menu)
    return HttpResponse("PARAM :"+menu)

@csrf_exempt
def post(request):
    # menu = request.POST.get['menu']
    menu = request.POST['menu']
    return HttpResponse("POST :"+ menu)

def forw(request):
    a= "홍길동"
    b = ["전우치" , "변우석"]
    c = [
        {'e_id':'1','e_name':'1','gen':'1','addr':'1'},    
        {'e_id':'2','e_name':'2','gen':'2','addr':'2'},    
        {'e_id':'3','e_name':'3','gen':'3','addr':'3'},    
        {'e_id':'4','e_name':'4','gen':'3','addr':'4'}    
    ]
    # return render(request, 'forw.html' , {'a':a, 'b':b} )
    return render(request, 'forw.html' , {'c': c } )
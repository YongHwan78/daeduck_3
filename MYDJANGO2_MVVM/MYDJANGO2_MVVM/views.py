'''
Created on 2024. 4. 25.

@author: PC-02
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import pymysql
from test.test_xmlrpc import ADDR

def index(request):
    return render(request, 'index.html')

def ses_in(request):
    request.session.set_expiry(30) 
    request.session['e_id'] = '개똥이의 이름'
    request.session['e_name'] = '똥이'

    return HttpResponse("ses_in")

def ses_del(request):
    # del request.session['e_id']
    request.session.clear()   #전체 삭제
    return HttpResponse("ses_del")
# python manage.py makemigrations
# python manage.py migrate
def ses_view(request):
    e_id = request.session.get('e_id', ' ')
    e_name = request.session.get('e_name', ' ')
    return HttpResponse("ses_view<br>"+str(e_id)+" "+str(e_name))


def coo_in(request):
    hr = HttpResponse('Coo_in')
    hr.set_cookie('e_id', 'kookie')
    # hr.set_cookie('e_id', '꾸키'.encode('utf-8'))
    return hr

def coo_del(request):
    hr = HttpResponse("coo_del")
    hr.delete_cookie('e_id')
    return hr

def coo_view(request):
    e_id = request.COOKIES.get("e_id","")
    # try:
    #     e_id= request.COOKIES['e_id']
    # except:
    #     e_id=''
    return  HttpResponse("coo_view <br>"+str(e_id))

def coo(request):
   
    return  render(request, 'coo.html')

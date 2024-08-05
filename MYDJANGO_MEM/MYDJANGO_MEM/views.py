'''
Created on 2024. 4. 25.

@author: PC-02
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import pymysql
from test.test_xmlrpc import ADDR
from MYDJANGO_MEM.daomem import DaoMem

def main(request):
    return redirect('/mem_list')

def mem_list(request):
    de = DaoMem()
    list = de.selectList()
    return render(request, 'mem_list.html', {'list':list })

def mem_detail(request ):
    de = DaoMem()
    m_id = request.GET['m_id']
    vo = de.selectOne(m_id);
    return render(request , 'mem_detail.html', {'vo':vo} )


def mem_mod(request):
    de = DaoMem()
    m_id = request.GET['m_id']
    vo = de.selectOne(m_id);
    return render(request , 'mem_mod.html' , vo)

@csrf_exempt
def mem_mod_act(request):
    de = DaoMem()
    m_id = request.POST['m_id']
    m_name = request.POST['m_name']
    tel = request.POST['tel']
    email = request.POST['email']
    cnt = de.update(m_id, m_name, tel, email)
    return render(request , 'mem_mod_act.html', {'cnt':cnt} )

def mem_add(request):
    de = DaoMem()
    return render(request , 'mem_add.html')

@csrf_exempt
def mem_add_act(request):
    de = DaoMem()
    m_id = request.POST['m_id']
    m_name = request.POST['m_name']
    tel = request.POST['tel']
    email = request.POST['email']
    
    check = de.check(m_id)
    
    if check == 1:
        cnt = de.insert(m_id, m_name, tel, email)
        return render(request , 'mem_add_act.html', {'cnt':cnt } )
    else :
        cnt = 0
        return render(request , 'mem_add_act.html', {'cnt': cnt } )

    
@csrf_exempt
def mem_delete_act(request):
    de = DaoMem()
    m_id = request.POST['m_id']
    cnt = de.delete(m_id)
    return render(request, 'mem_list.html', {'cnt':cnt })
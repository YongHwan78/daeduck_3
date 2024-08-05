'''
Created on 2024. 4. 25.

@author: PC-02
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import pymysql
from MYDJANGO_MVC.daoemp import DaoEmp
from test.test_xmlrpc import ADDR

def main(request):
    return redirect('/emp_list')

def emp_list(request):
    de = DaoEmp()
    list = de.selectList();
    
    return render(request, 'emp_list.html' , {'list' : list})
def emp_detail(request):
    e_id = request.GET['e_id']
    de = DaoEmp()
    vo = de.selectOne(e_id)
    return render(request, 'emp_detail.html' , {'vo': vo } )
    
def emp_mod(request):
    e_id = request.GET['e_id']
    de = DaoEmp()
    vo = de.selectOne(e_id)
    return render(request, 'emp_mod.html' , {'vo': vo } )

@csrf_exempt
def emp_mod_act(request):
    e_id = request.POST['e_id'];
    e_name = request.POST['e_name'];
    gen = request.POST['gen'];
    addr = request.POST['addr'];
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
    return render(request, 'emp_mod_act.html' , {'cnt': cnt } )

def emp_add(request):
    de = DaoEmp()
    return render(request, 'emp_add.html' )

@csrf_exempt
def emp_del_act(request):
    e_id = request.POST['e_id'];
    de = DaoEmp()
    cnt = de.delete(e_id)
    # list = de.selectList();
    return render(request, 'emp_del_act.html' , {'cnt' : cnt} )


@csrf_exempt
def emp_add_act(request):
    e_id = request.POST['e_id'];
    e_name = request.POST['e_name'];
    gen = request.POST['gen'];
    addr = request.POST['addr'];
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    return render(request, 'emp_add_act.html' , {'cnt': cnt } )
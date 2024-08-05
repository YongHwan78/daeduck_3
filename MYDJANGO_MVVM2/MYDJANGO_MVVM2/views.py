'''
Created on 2024. 4. 25.

@author: PC-02
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import pymysql
from test.test_xmlrpc import ADDR
from django.http.response import JsonResponse
from django.db.models.functions.comparison import JSONObject
import json

from MYDJANGO_MVVM2.daoemp import DaoEmp

def main(request):
    return redirect('/static/ajax.html')

@csrf_exempt
def ajax(request):
    jsonObject = json.loads(request.body)
    print(jsonObject.get('menu'))
    context = {
        'messages' : 'ok'
    }
    return JsonResponse(context)


@csrf_exempt
def ajax_emp_list(request):
    de = DaoEmp()
    list = de.selectList();
    context = {
        'list' : list
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_detail(request):
    jsonObject = json.loads(request.body)
    de = DaoEmp()
    vo = de.selectOne(int(jsonObject.get('e_id')));
    context = {
        'vo' : vo
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_add(request):
    param = json.loads(request.body)
    de = DaoEmp()
    
    e_id = int(param['e_id'])
    e_name = int(param['e_name'])
    gen = int(param['gen'])
    addr = int(param['addr'])
    
    cnt = de.insert(e_id, e_name, gen ,addr )
    
    context = {
        'cnt' : cnt
    }
    return JsonResponse(context)

@csrf_exempt
def ajax_emp_mod(request):
    param = json.loads(request.body)
    de = DaoEmp()
    
    e_id = param['e_id']
    e_name = param['e_name']
    gen = param['gen']
    addr = param['addr']
    
    print(e_id, e_name, gen, addr)
    cnt = de.update(e_id, e_name, gen, addr)
    
    context = {
        'cnt' : cnt
    }
    return JsonResponse(context)
@csrf_exempt
def ajax_emp_del(request):
    param = json.loads(request.body)
    de = DaoEmp()
    e_id = param['e_id']
    print(e_id)
    cnt = de.delete(e_id)
    context = {
        'cnt' : cnt
    }
    return JsonResponse(context)


@csrf_exempt
def fetch(request):
    
    jsonObject = json.loads(request.body)
    print(jsonObject.get('menu'))
    context = {
        'messages' : 'ok'
    }
    return JsonResponse(context)


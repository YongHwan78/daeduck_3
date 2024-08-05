'''
Created on 2024. 4. 25.
@author: PC-02
'''
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import json
from MYDJANGO_FET.daoemp import DaoEmp


def main(request):
    return redirect('/static/ajax.html')


@csrf_exempt
def ajax(request):
    jsonObject = json.loads(request.body)
    print(jsonObject.get('menu'))
    context = {
        'messages': 'ok'
    }
    return JsonResponse(context)


@csrf_exempt
def ajax_emp_list(request):
    de = DaoEmp()
    emp_list = de.selectList()
    context = {
        'list': emp_list
    }
    return JsonResponse(context)


@csrf_exempt
def ajax_emp_one(request):
    param = json.loads(request.body)
    de = DaoEmp()
    emp_detail = de.selectOne(int(param.get('e_id')))
    context = {
        'vo': emp_detail
    }
    return JsonResponse(context)


@csrf_exempt
def ajax_emp_add(request):
    param = json.loads(request.body)
    de = DaoEmp()

    e_id = int(param['e_id'])
    e_name = param['e_name']
    gen = param['gen']
    addr = param['addr']

    cnt = de.insert(e_id, e_name, gen, addr)

    context = {
        'cnt': cnt
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
        'cnt': cnt
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
        'cnt': cnt
    }
    return JsonResponse(context)


@csrf_exempt
def fetch(request):
    jsonObject = json.loads(request.body)
    print(jsonObject.get('menu'))
    context = {
        'messages': 'ok'
    }
    return JsonResponse(context)

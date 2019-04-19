#! /usr/bin/env python# -*- coding: utf-8 -*-


from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render
from datetime import datetime
import os

# Create your views here.
from django.template import Template, Context


def msgproc(request):
    datalist =[]
    if request.method == "POST":
        userA = str(request.POST.get("userA",None))
        userB =str(request.POST.get("userB", None))
        msg = str(request.POST.get("msg",None))
        time = datetime.now()
        with open("F:/Python程序/flaskr/djiango/cloudms/msgdata.txt",'w') as f:
            f.write("{}--{}--{}--{}--\n".format(userB,userA, msg,time.strftime("%Y-%m-%d %H:%M:%S")))
    if request.method == "GET":
        userC = request.GET.get("userC",None)
        if userC !=None:
            with open("F:/Python程序/flaskr/djiango/cloudms/msgdata.txt",'r',encoding='utf-8') as f:
                cnt = 0
                linedatas= f.readlines()
                for line in linedatas:
                    linedata = str(line.split('--',4))
                    if linedata[0] == userC:
                        cnt = cnt +1
                        d = {"userA":linedata[1],"msg":linedata[2],"time":linedata[3]}
                        datalist.append(d)
                    if cnt >= 10:
                        break
    return  render(request,"web.html",{"data":datalist})
def homeproc(request):
    response = HttpResponse()
    response.write("<h1>这是首页，具体功能实现请访问<a href='./msggate'>这里</a></h1>")
    response.write("<h1>这是第二行</h1>")
    return response

def homeproc1(request):
    response = JsonResponse({'key':'valuel'})
    return  response

def homeproc2(request):
    cwd =os.path.dirname(os.path.dirname(os.path.abspath))
    response = Context(open(cwd + "msgapp/tempaltes/db.png","rb"))
    response['Content -Type'] = 'application/octet - stream '
    response['Content - Disposition'] = 'attachment;filename="db.png""'
    return response

def pgproc(request):
    template = Template("<h1>这个程序的名字是{{name}}</h1>")
    context = Context({"name":"实验平台"})
    return HttpResponse(template.render(context))
# -*- coding: utf-8 -*-
from django.shortcuts import render , render_to_response
from django import template
from .models import User, Node, Product,Prder
# Create your views here.
import os ,random
#生成二维码用
import base64
from django.http import HttpResponse,HttpResponseRedirect
import qrcode
from cStringIO import StringIO

from django.contrib.auth.decorators import login_required
########################
def index(requset):
    title = '世界门'
    return render_to_response('index.html',{'title':title,})

#################
#用户中心
#@login_required(login_url="/ss/login/")
@login_required(login_url="/ss/login/?next=%s")
def user(requset):
    '''
    if not requset.user.is_authenticated():
        #转到登陆页面，登陆完之后，反回原来页面
        return HttpResponseRedirect('/ss/login/?next=%s' % requset.path)
        '''
    title = '用户中心'
    if  requset.user.is_authenticated():
        user_id = requset.user.id
        user_name = requset.user.username
        print user_id
        print user_name
        user = User.objects.all().get(id=user_id)
    return render_to_response('ss/user.html',{'user':user,'title':title})

#我的信息
def myinfo(requset):
    info = User.objects.values('email','pass_field','passwd').get(id=3)
    title = '我的信息'
    print info
    return render_to_response('ss/myinfo.html',{'title':title,
                                                'info':info})

#节点
def node(requset):
    title = "节点列表"
    #当前用户ID
    user_id = requset.user.id
    node1 = Node.objects.values("id",'node_name','node_type','node_ip')
    user = User.objects.values('port','passwd').get(id=user_id)
    '''
    ii =    {
      "server": "106.186.115.151",
      "server_port": 1439,
      "password": "W8VP8e",
      "method": "rc4-md5",
      "remarks": "jp",
      "auth": false
    }
    '''
    #print user['passwd']
    '''
    #ss://method:password@hostname:port
    for ip in node1['node_server']:
        i ="rc4-md5:"+ user['passwd']+@ip:user['port']
        print i
    '''
    return render_to_response('ss/node.html',{'node':node1,
                                                'port':user['port'],
                                              'title':title })


#产品
def Prod(requset):
    title = "产品"
    #product = Product.objects.all().values("id", "product_name","description","price")
    product = Product.objects.values('id','product_name','description','price')

    #print product[0]['description']
    return render_to_response("ss/Product.html",{"Product":product ,
                                                 'title':title})


#订单
def prder(requset):
    title = "订单"
    user_id = requset.user.id
    user = User.objects.values('id').get(id=2)
    print user
   # pr = Prder.objects.get(order_user="2")
    return render_to_response('ss/prder.html', {'title':title, 'user':user_id,
                                                #'Pr':pr,
                                                })

import datetime
def create_prder(requset):
    title = "订单"
    #当前时间
    now_datetime = datetime.datetime.now().strftime('%Y%m%d%H%M%S');

    product = Product.objects.get(id=1)
    user = User.objects.get(id=2)
    #生成
    Prder.objects.create(order_number=now_datetime,order_product=product,order_user=user)
    return render_to_response('ss/prder.html', {'title':title,
                                                })


#生成二维码
def generate_qrcode(request, data):
    img = qrcode.make(data)
    #img = qrcode.make(ii)
    buf = StringIO()
    img.save(buf)
    image_stream = buf.getvalue()

    response = HttpResponse(image_stream, content_type="image/png")
    response['Last-Modified'] = 'Mon, 27 Apr 2015 02:05:03 GMT'
    response['Cache-Control'] = 'max-age=31536000'
    return response



#用户注册
###################
from form import RegisterForm
def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render_to_response('register.html',RequestContext(request,{'form':form,}))
    #注册提交
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            password1 = request.POST.get('password1','')
            email = request.POST.get('email','')
            user = auth.authenticate(username=username,password=password,email=email)
            user1 = auth.authenticate(username=username)
            if user is  None :
                #取id最大用的port
                port_id = User.objects.values('port').latest('id')
                #新用户post 最大用的port +1
                port = port_id['port']+1
                #将表单写入数据库
                #User.objects.get_or_create(username=username,email=email,password=password,port=port)
                user = User.objects.create_user(username=username,password=password,email=email,port=port)
                #print user.is_staff #True
                user.save()
                #返回注册成功页面
                return render_to_response('success.html',{'username':username})
            else:
                return render_to_response('register.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
        else:
            return render_to_response('register.html',RequestContext(request,{'form':form,}))
        return render_to_response('register.html')

############################
from django.contrib import auth
from django.template.context import RequestContext
from form import LoginForm

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('login.html', RequestContext(request, {'form':form, }))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            #email = request.POST.get('email')
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            user = auth.authenticate(username=username ,password=password)
            #print email
            #print password
            #print user
            if user is not None and user.is_active:
                auth.login(request,user)
            #    return render_to_response('index.html',RequestContext(request))
                return HttpResponseRedirect('/ss/user')
            else:
                return render_to_response('login.html',RequestContext(request,{'form':form,'password_is_wrong':True}))
        else:
            return render_to_response('login.html',RequestContext(request,{'form':form,}))
        return render_to_response('login.html')


############################
def logout(request):
    auth.logout(request)
    return render_to_response('index.html')
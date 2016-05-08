# coding:utf-8
from django.shortcuts import render,render_to_response,redirect
from door_windows.settings import STORAGE_PATH,USERRES_URLBASE
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.template import RequestContext
from django.contrib import messages
from models import Products
import os

# Create your views here.
def product_list(request):
    products = Products.objects.all().order_by("-last_update_timestamp")
    return render_to_response("product_list.html",
                              {"products":products},
                              context_instance=RequestContext(request))

def add_products(request):
    if request.method == 'GET':
        return render_to_response('add_products.html',context_instance=RequestContext(request))
    else:
        title = request.POST['title'].strip()
        content = request.POST['content'].strip()
        if not title or not content:
            messages.add_message(request,messages.ERROR,u'标题内容均不能为空')
            return render_to_response('add_products.html',{"title":title,"content":content},context_instance=RequestContext(request))
        owner = User.objects.all()[0]
        avatar = "http://res.myform.com/05271590.jpg"
        new_product = Products(owner=owner,avatar=avatar,title=title,content=content)
        new_product.save()
        messages.add_message(request,messages.INFO,u"成功发布产品！")
        return redirect(reverse("product_list"))

def uploadavatar(request,product_id):  # 根据产品 id 更换图像
    product_id = int(product_id)
    product = Products.objects.get(id=product_id)
    if request.method == 'GET':
        return render_to_response('uploadavatar.html',{'product':product},context_instance=RequestContext(request))
    else:
        avatar_file = request.FILES.get("avatar",None)
        if avatar_file.size > 1048576:
            messages.add_message(request,messages.WARNING,u'图像大小不能超过2M')
            return render_to_response('uploadavatar.html',{'product':product},context_instance=RequestContext(request))
        file_path = os.path.join(STORAGE_PATH,avatar_file.name)
        with open(file_path,'wb+')as destination:
            for chunk in avatar_file.chunks():
                destination.write(chunk)
        url = "%s%s" % (USERRES_URLBASE,avatar_file.name)
        product.avatar = url
        product.save()
        # messages.add_message(request,messages.INFO,u"成功上传图像！")
        return redirect(reverse("product_list"))

def product_detail(request,product_id):
    product_id = int(product_id)
    product = Products.objects.get(id=product_id)
    return render_to_response("product_detail.html",
                              {'product':product},
                              context_instance=RequestContext(request))



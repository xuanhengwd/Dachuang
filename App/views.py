from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from App import models


def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = models.User.objects.get(user_name__contains=username)
        except:
            data = {"error_code": 0, 'msg': '用户名不存在'}

            return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
        if user.user_password == password:
            data = {"error_code": 1, 'msg': '登录成功'}
            return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
        else:
            data = {"error_code": 0, 'msg': '密码错误'}
            return JsonResponse(data, json_dumps_params={"ensure_ascii": False})

    return HttpResponse('none')


def userregist(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        same_name = models.User.objects.filter(user_name__contains=username)
        same_email = models.User.objects.filter(user_mail__contains=email)
        if same_name or same_email:
            data = {"error_code": 0, 'msg': '用户名或邮箱已经存在'}
            meg = "用户名或邮箱已经存在"
            return JsonResponse(data)

        newuser = models.User.objects.create()
        newuser.user_name = username
        newuser.user_password = password
        newuser.user_mail = email
        newuser.save()
        data = {"error_code": 1, 'msg': '创建成功'}
        meg = '创建成功'
        return JsonResponse(data)

    return HttpResponse("none")
